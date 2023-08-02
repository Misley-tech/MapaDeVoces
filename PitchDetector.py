from scipy import signal
import numpy as np
import soundfile as sf

def f(x):
    f_0=1 
    return np.sin(x*np.pi*2*f_0)

def ACF(f,W,t,lag):
    return np.sum(f[t:t+W]*f[lag+t:lag+t+W])

def detect_pitch(f,W,t,sample_rate,bounds):
    ACF_vals = [ACF(f,W,t,i) for i in range(*bounds)]
    sample = np.argmax(ACF_vals)+bounds[0]
    return sample_rate / sample

def main():
    sample_rate=500
    start=0
    end=5
    num_samples=int(sample_rate*(end-start)+1)
    Window_size = 200
    bounds = [20,num_samples//2]

    x=np.linspace(start,end,num_samples)
    print(detect_pitch(f(x),Window_size,1,sample_rate,bounds))

def DF(f,W,t,lag):
    return ACF(f,W,t,0)+ACF(f,W,t+lag,0)-(2*ACF(f,W,t,lag))

def detect_pitch(f,W,t,sample_rate,bounds):
    DF_vals = [DF(f,W,t,i) for i in range(*bounds)]
    sample = np.argmin(DF_vals) + bounds[0]
    return sample_rate/sample

def CMNDF(f,W,t,lag):
    if lag == 0:
        return 1
    return DF(f,W,t,lag)/np.sum([DF(f,W,t,j+1) for j in range(lag)])*lag

def detect_pitch(f,W,t,sample_rate,bounds):
    CMNDF_vals = [CMNDF(f,W,t,i) for i in range(*bounds)]
    sample = np.argmin(CMNDF_vals)+bounds[0]
    return sample_rate/sample

main()