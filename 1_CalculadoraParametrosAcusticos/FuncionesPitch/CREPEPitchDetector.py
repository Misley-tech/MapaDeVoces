# pip install --upgrade tensorflow
# pip install crepe
# La red esta entrenada con audios de sample rate de 16kHz
import crepe
from scipy.io import wavfile

audio_path = 'C:/Users/Asus/Desktop/programitas/UMAP prueba/PruebaConVoces/VozNorma_F#4_370.wav'
sr, audio = wavfile.read(audio_path)
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
print(f'time:{time}')
print(f'frequency:{frequency}')
