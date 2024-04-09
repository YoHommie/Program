import numpy as np
from scipy.interpolate import interp1d

def eemd(Y, Nstd, NE):
    xsize = len(Y)
    dd = np.arange(1, xsize + 1)
    Ystd = np.std(Y)
    Y = Y / Ystd

    TNM = int(np.fix(np.log2(xsize))) - 1
    TNM2 = TNM + 2

    allmode = np.zeros((xsize, TNM2))

    for iii in range(NE):
        X1 = Y + np.random.randn(xsize) * Nstd

        mode = np.zeros((xsize, TNM + 1))
        mode[:, 0] = Y

        xorigin = X1
        xend = xorigin

        nmode = 1
        while nmode <= TNM:
            xstart = xend.copy()
            iter_count = 1

            while iter_count <= 10:
                spmax, spmin = extrema(xstart)
                upper = interp1d(spmax[:, 0], spmax[:, 1], kind='linear', fill_value='extrapolate')(dd)
                lower = interp1d(spmin[:, 0], spmin[:, 1], kind='linear', fill_value='extrapolate')(dd)
                mean_ul = (upper + lower) / 2
                xstart = xstart - mean_ul
                iter_count += 1

            xend = xend - xstart
            nmode += 1

            mode[:, nmode] = xstart

        mode[:, nmode] = xend
        allmode += mode

    allmode = allmode / NE
    allmode = allmode * Ystd

    return allmode


def extrema(data):
    d = np.diff(data)
    maxima = (d[:-1] > 0) & (d[1:] <= 0)
    minima = (d[:-1] < 0) & (d[1:] >= 0)

    spmax = np.column_stack((np.where(maxima)[0] + 1, data[maxima]))
    spmin = np.column_stack((np.where(minima)[0] + 1, data[minima]))

    return spmax, spmin

# def extrema(data):
#     d = np.diff(data)
#     maxima = (d[:-1] > 0) & (d[1:] <= 0)
#     minima = (d[:-1] < 0) & (d[1:] >= 0)

#     # Ensure that maxima and minima indices are within the valid range
#     spmax = np.column_stack((np.where(maxima)[0] + 1, data[maxima]))[:len(data)-1]
#     spmin = np.column_stack((np.where(minima)[0] + 1, data[minima]))[:len(data)-1]

#     return spmax, spmin


# Example usage:
# Replace Y, Nstd, and NE with your data and parameters
# result = eemd(Y, Nstd, NE)
# print(result)











