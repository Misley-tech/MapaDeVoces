import numpy as np
import soundfile as sf

f=1000
fs=44100
n=100

t=np.linspace(0,1,fs)
f1=np.sin(2*np.pi*f*t)
sf.write(f'sonido_ref_{f}Hz.wav',f1,fs)
for i in range(n):
    cte=[round(np.random.uniform(0,1),1),round(np.random.uniform(0, 1),1)]
    f2=cte[1]*np.sin(2*np.pi*f*cte[1]*t) 
    sf.write(f'sonido{i}_{f}Hz.wav',f1+f2,fs)