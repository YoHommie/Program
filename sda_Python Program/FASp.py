import numpy as np

def FASp(dt, xgtt):
    # Nyquist frequency (highest frequency)
    Ny = (1 / dt) / 2
    # number of points in xgtt
    L = len(xgtt)
    # Next power of 2 from length of xgtt
    NFFT = 2**int(np.ceil(np.log2(L)))
    # frequency spacing
    df = 1 / (NFFT * dt)
    # Fourier amplitudes
    U = np.abs(np.fft.fft(xgtt, NFFT)) * dt
    # Single sided Fourier amplitude spectrum
    U = U[1:int(Ny/df) + 1]
    # frequency range
    f = np.linspace(df, Ny, int(Ny/df))

    return f, U

# Example usage:
# Replace dt and xgtt with your actual values
# dt = 0.005
# xgtt = np.random.randn(1000)  # Replace with your data
# f, U = FASp(dt, xgtt)
# print("f:", f)
# print("U:", U)
