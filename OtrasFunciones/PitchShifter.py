import torch
import torchaudio
import soundfile as sf

def PitchShifter(input_file_path,output_file_path,semi_tonos):
    audio,sr = sf.read(input_file_path)
    audio = torch.tensor(audio)
    y= torchaudio.functional.pitch_shift(
        waveform = audio,
        sample_rate = sr,
        n_steps=semi_tonos)
    sf.write(output_file_path, y,samplerate=sr)

input_file_path = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3/AudiosWordSplitterManual/Crudo/E_crudo.wav'
output_file_path = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/Gohan.wav'
semi_tonos = 8
PitchShifter(input_file_path,output_file_path,semi_tonos)
