# pip install --upgrade tensorflow
# pip install crepe

import crepe
from scipy.io import wavfile

sr, audio = wavfile.read('C:/Users/Asus/Desktop/programitas/UMAP prueba/piano_prueba.wav')
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
print(f'time:{time}')
print(f'frequency:{frequency}')