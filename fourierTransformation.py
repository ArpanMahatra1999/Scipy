from scipy.fftpack import fft
import numpy as np

x = np.array([1,2,3,4])
print(fft(x))