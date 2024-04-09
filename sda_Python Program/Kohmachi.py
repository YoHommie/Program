import numpy as np

def kohmachi(signal, freq_array, smooth_coeff):
    ii = np.arange(1, len(freq_array) + 1)
    
    ratio = np.repeat(freq_array, len(freq_array)).reshape(-1, len(freq_array)) / freq_array[ii - 1].reshape(-1, 1)
    rat = np.log10(ratio)
    
    w = (np.sin(rat * smooth_coeff) / (rat * smooth_coeff))**4
    w[np.isnan(w)] = 0
    
    s = np.sum(w[:, ii - 1], axis=1)
    avg = w.T / s
    y = avg[ii - 1] @ signal
    
    return y

# Example usage:
# Replace signal, freq_array, and smooth_coeff with your actual values
# signal = np.random.randn(1000, 3)  # Replace with your data
# freq_array = np.linspace(1, 10, 1000)
# smooth_coeff = 0.1
# result = kohmachi(signal, freq_array, smooth_coeff)
# print(result)
