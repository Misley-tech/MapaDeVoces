import numpy as np
import soundfile as sf

def GeneradorSenalesF0Definida(fref,fs,n):
    t=np.linspace(0,1,fs)
    f1=np.sin(2*np.pi*fref*t)
    sf.write(f'Tono_{fref}Hz.wav',f1,fs)

    for i in range(n):
        cte=[round(np.random.uniform(0,1),1),round(np.random.uniform(0, 1),1)]
        f2=cte[1]*np.sin(2*np.pi*fref*cte[1]*t) 
        sf.write(f'SonidoComplejo{i}_{fref}Hz.wav',f1+f2,fs)

fref=1000
fs=96000
n=10
GeneradorSenalesF0Definida(fref,fs,n)

