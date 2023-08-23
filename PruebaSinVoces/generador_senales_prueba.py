import numpy as np
import soundfile as sf

# f=1000
# freq = [250,500,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500]
# fs=96000
# n=100
# for i in range():
#     t=np.linspace(0,1,fs)
#     f1=np.sin(2*np.pi*f*t)
#     sf.write(f'sonido_ref_{f}Hz.wav',f1,fs)
# for i in range(n):
#     cte=[round(np.random.uniform(0,1),1),round(np.random.uniform(0, 1),1)]
#     f2=cte[1]*np.sin(2*np.pi*f*cte[1]*t) 
#     sf.write(f'sonido{i}_{f}Hz.wav',f1+f2,fs)

import librosa
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from scipy.signal import find_peaks

def AutocorrPitchDetector(path_file):
    data, sampling_frequency = librosa.load(str(path_file))

    # Get some useful statistics
    T = 1/sampling_frequency # Sampling period
    N = len(data) # Signal length in samples
    t = N / sampling_frequency # Signal length in seconds

    Y_k = np.fft.fft(data)[0:int(N/2)]/N # FFT
    Y_k[1:] = 2*Y_k[1:] # Single-sided spectrum
    Pxx = np.abs(Y_k) # Power spectrum

    f = sampling_frequency * np.arange((N/2)) / N; # frequencies

    auto = sm.tsa.acf(data, nlags=1000)

    peaks = find_peaks(auto)[0] # Find peaks of the autocorrelation
    lag = peaks[0] # Choose the first peak as our pitch component lag
    pitch = sampling_frequency / lag # Transform lag into frequency
    return pitch

freq = [250,500,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500]
fs=96000
n=100
A=[]
for f in freq:
    AutocorrPitchDetector('C:/Users/Asus/Desktop/programitas/UMAP prueba/Cluster/cluster_ref/sonido_ref_{f}Hz.wav')
print(A)