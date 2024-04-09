import numpy as np
from scipy.signal import hilbert
from scipy.fftpack import fftshift
from scipy.interpolate import interp2d
from scipy.io import loadmat
import matplotlib.pyplot as plt
from eemd import eemd


def EPSDParam(EWa, dt):
    bb = len(EWa)
    fs = 1 / dt

    StandevData = np.std(EWa)

    if StandevData > 50:
        NstdSet = [0.1, 0.2, 0.3, 0.5, 0.7]
    elif 10 <= StandevData <= 50:
        NstdSet = [0.01, 0.05, 0.09, 0.1, 0.2]
    elif 1 <= StandevData <= 10:
        NstdSet = [0.005, 0.009, 0.01, 0.05, 0.1]
    elif StandevData <= 1:
        NstdSet = [0.001, 0.003, 0.005, 0.009, 0.01]

    VarP = 0

    for n in range(len(NstdSet)):
        Nstd = NstdSet[n]
        allmode = eemd(EWa, Nstd, 3)
        varData = np.var(allmode[:, 0])
        lend, wid = allmode.shape
        PerVar = np.zeros((wid - 1,))

        for m in range(1, wid - 1):
            PerVar[m - 1] = (np.var(allmode[:, m]) / varData) * 100

        VarTotal = np.sum(PerVar)

        if 85 <= VarTotal <= 115:
            VarP = VarTotal
            break

    if VarP == 0:
        Nstd = 0.81
        allmode = eemd(EWa, Nstd, 3)
        varData = np.var(allmode[:, 0])
        lend, wid = allmode.shape
        PerVar = np.zeros((wid - 1,))

        for m in range(1, wid - 1):
            PerVar[m - 1] = (np.var(allmode[:, m]) / varData) * 100

        VarP = np.sum(PerVar)

    IMF = allmode[:, 1:]
    Time = bb * dt

    AF = np.zeros_like(IMF, dtype=np.complex128)
    Cj = np.abs(AF)
    Thetaj = np.unwrap(np.angle(AF))
    IF = np.diff(Thetaj, axis=0) / (2 * np.pi * dt)

    IF = np.concatenate((IF, np.zeros((1, wid - 2))))

    for k in range(1, wid - 1):
        for k1 in range(bb):
            if IF[k1, k] < 0:
                IF[k1, k] = 0

    Ws = np.linspace(0, fs / 2, wid - 1)
    Ts = np.linspace(0, Time, bb)
    GTW = np.zeros((bb, wid - 1))

    for x in range(bb):
        for imf in range(1, wid - 1):
            freqid = round(IF[x, imf], 1)
            freqidx = int(np.where(np.round(Ws, 1) == freqid)[0])

            if 1 <= freqidx <= len(Ws):
                tx = x
                GTW[tx, freqidx] += Cj[x, imf] ** 2 * 0.5

    Ws, Ts = np.meshgrid(Ws, Ts)
    GTW = np.flipud(np.rot90(GTW))

    Param = {
        'GTW': GTW,
        'Ws': Ws,
        'Ts': Ts
    }

    return Param

# Example usage:
# Replace EWa and dt with your data

file_path = r"C:/Users/adity/OneDrive/Desktop/Sixth Semester/CE6018 Seismic Data Analytics/Program/sda_Python Program/RSN1_X.mat"
data = loadmat(file_path)


EWa= data["resampledSignal"][0]
dt=0.02
result = EPSDParam(EWa, dt)
print(result)
plt.pcolormesh(result['Ts'], result['Ws'], result['GTW'])
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
