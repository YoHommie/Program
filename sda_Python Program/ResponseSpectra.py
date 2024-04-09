import numpy as np
import matplotlib.pyplot as plt

def responsespectrum(accel, ee, dt):
    Tn = 10
    y = 0.5
    b = 0.25
    uo = 0
    vo = 0
    m = 1
    z = ee / 100
    
    na = len(accel)
    nl = 2 * na
    
    T = np.array([0.01, 0.015, 0.02, 0.03, 0.04, 0.05, 0.06, 0.075, 0.09, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75,
                  0.8, 0.9, 1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 7.5, 8, 9, 10])
    
    accel = np.concatenate((accel, np.zeros(nl - na)))
    p = -m * accel
    
    A = np.zeros(len(T))  # acceleration response spectrum - total acceleration
    V = np.zeros(len(T))  # velocity response spectrum - relative velocity
    D = np.zeros(len(T))  # displacement response spectrum - relative displacement
    
    for j in range(len(T)):
        fn = 1 / T[j]
        wn = 2 * np.pi * fn
        k = m * wn**2
        c = 2 * m * wn * z
        
        u = np.zeros(nl)
        v = np.zeros(nl)
        ac = np.zeros(nl)
        
        u[0] = uo
        v[0] = vo
        ac[0] = (p[0] - c * vo - k * uo) / m
        
        kf = k + y * c / (b * dt) + m / (b * dt**2)
        a = m / (b * dt) + y * c / b
        b2 = m / (2 * b) + dt * (y / (2 * b) - 1) * c
        
        for i in range(nl - 1):
            p1 = p[i]
            p2 = p[i + 1]
            dpf = (p2 - p1) + a * v[i] + b2 * ac[i]
            du = dpf / kf
            dv = y / (b * dt) * du - (y / b) * v[i] + dt * (1 - y / (2 * b)) * ac[i]
            da = du / (b * dt**2) - v[i] / (b * dt) - ac[i] / (2 * b)
            u[i + 1] = u[i] + du
            v[i + 1] = v[i] + dv
            ac[i + 1] = ac[i] + da
        
        asd = ac + accel
        A[j] = np.max(np.abs(asd))
        V[j] = np.max(np.abs(v))
        D[j] = np.max(np.abs(u))
    
    A = np.concatenate(([np.max(np.abs(accel))], A))
    V = np.concatenate(([0], V))
    D = np.concatenate(([0], D))
    
    PSV = (2 * np.pi / T) * D[1:]  # pseudo spectral velocity
    PSV = np.concatenate(([PSV[0]], PSV))
    PSA = ((2 * np.pi / T)**2) * D[1:]  # pseudo spectral acceleration
    PSA = np.concatenate(([PSA[0]], PSA))
    
    T = np.concatenate(([0], T))
    
    plt.figure()
    plt.plot(T, A)
    plt.xlabel('Time Period (seconds)')
    plt.ylabel('Spectral Acceleration')
    
    plt.figure()
    plt.plot(T, V)
    plt.xlabel('Time Period (seconds)')
    plt.ylabel('Spectral Velocity')
    
    plt.figure()
    plt.plot(T, D)
    plt.xlabel('Time Period (seconds)')
    plt.ylabel('Spectral Displacement')
    
    plt.figure()
    plt.plot(T, PSV)
    plt.xlabel('Time Period (seconds)')
    plt.ylabel('Pseudo Spectral Velocity')
    
    plt.figure()
    plt.plot(T, PSA)
    plt.xlabel('Time Period (seconds)')
    plt.ylabel('Pseudo Spectral Acceleration')
    
    plt.show()

# Example usage:
# Replace accel, ee, and dt with your actual values
# accel = np.random.randn(1000)
# ee = 5
# dt = 0.005
# responsespectrum(accel, ee, dt)
