import numpy as np

def extrema(in_data):
    flag = 1
    dsize = len(in_data)

    spmax = np.zeros((2, 1))
    spmax[0, 0] = 1
    spmax[1, 0] = in_data[0]
    jj = 2
    kk = 2

    while jj < dsize:
        if (in_data[jj - 1] <= in_data[jj]) and (in_data[jj] >= in_data[jj + 1]):
            spmax = np.append(spmax, [[jj], [in_data[jj]]], axis=1)
            kk += 1
        jj += 1

    spmax = np.append(spmax, [[dsize], [in_data[dsize - 1]]], axis=1)

    if kk >= 4:
        slope1 = (spmax[1, 1] - spmax[2, 1]) / (spmax[1, 0] - spmax[2, 0])
        tmp1 = slope1 * (spmax[0, 0] - spmax[1, 0]) + spmax[1, 1]

        if tmp1 > spmax[0, 1]:
            spmax[0, 1] = tmp1

        slope2 = (spmax[kk - 1, 1] - spmax[kk - 2, 1]) / (spmax[kk - 1, 0] - spmax[kk - 2, 0])
        tmp2 = slope2 * (spmax[kk, 0] - spmax[kk - 1, 0]) + spmax[kk - 1, 1]

        if tmp2 > spmax[kk, 1]:
            spmax[kk, 1] = tmp2
    else:
        flag = -1

    msize = in_data.shape
    dsize = max(msize)
    xsize = dsize // 3
    xsize2 = 2 * xsize

    spmin = np.zeros((2, 1))
    spmin[0, 0] = 1
    spmin[1, 0] = in_data[0]
    jj = 2
    kk = 2

    while jj < dsize:
        if (in_data[jj - 1] >= in_data[jj]) and (in_data[jj] <= in_data[jj + 1]):
            spmin = np.append(spmin, [[jj], [in_data[jj]]], axis=1)
            kk += 1
        jj += 1

    spmin = np.append(spmin, [[dsize], [in_data[dsize - 1]]], axis=1)

    if kk >= 4:
        slope1 = (spmin[1, 1] - spmin[2, 1]) / (spmin[1, 0] - spmin[2, 0])
        tmp1 = slope1 * (spmin[0, 0] - spmin[1, 0]) + spmin[1, 1]

        if tmp1 < spmin[0, 1]:
            spmin[0, 1] = tmp1

        slope2 = (spmin[kk - 1, 1] - spmin[kk - 2, 1]) / (spmin[kk - 1, 0] - spmin[kk - 2, 0])
        tmp2 = slope2 * (spmin[kk, 0] - spmin[kk - 1, 0]) + spmin[kk - 1, 1]

        if tmp2 < spmin[kk, 1]:
            spmin[kk, 1] = tmp2
    else:
        flag = -1

    return spmax, spmin, flag

# Example usage:
# Replace in_data with your actual data
# spmax, spmin, flag = extrema(in_data)
# print("spmax:", spmax)
# print("spmin:", spmin)
# print("flag:", flag)
