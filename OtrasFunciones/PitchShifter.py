import torch
import torchaudio
import soundfile as sf

def PitchShifter(input_file_path,output_name,semi_tonos):
    audio,sr = sf.read(input_file_path)
    audio = torch.tensor(audio)
    y= torchaudio.functional.pitch_shift(
        waveform = audio,
        sample_rate = sr,
        n_steps=semi_tonos)
    output_name = f'{output_name}.wav'
    sf.write(output_name, y,samplerate=sr)

# Ejemplo
# input_file_path = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3/ExperimentoE/E0_ZP.wav'
# output_name = 'NombreDePrueba'
# semi_tonos = 8
# PitchShifter(input_file_path,output_name,semi_tonos)
