from pydub import AudioSegment
from pydub.silence import split_on_silence

def WordSplitter(chunk_name,raw_audio_path,chunk_storage_directory,min_silence_len,silence_thresh):
    sound_file = AudioSegment.from_wav(raw_audio_path)
    audio_chunks = split_on_silence(
        sound_file,
        min_silence_len,
        silence_thresh = sound_file.dBFS-silence_thresh
        )
    for i, chunk in enumerate(audio_chunks):
        out_file = f"{chunk_storage_directory}/chunk{i}_de_{chunk_name}.wav"
        print(f'Audio{i}', out_file)
        chunk.export(out_file, format="wav")

chunk_name = 'HolaComoEstasPitched2'
raw_audio_path = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo2/Audios/HolaComoEstasPitched51.wav'
chunk_storage_directory = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3'
min_silence_len = 11 # must be silent for at least half a second
silence_thresh=-25 # consider it silent if quieter than -16 dBFS    

WordSplitter(chunk_name,raw_audio_path,chunk_storage_directory,min_silence_len,silence_thresh)
