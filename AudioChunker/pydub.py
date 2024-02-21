from pydub import AudioSegment
from pydub.silence import split_on_silence

def AudioChunker(file_name,raw_audio_path,chunk_storage_directory,min_silence_len,silence_thresh):
    """
    Toma un audio y lo separa por silencios en chunks a partir de los parámetros min_silence_len y silence_thresh
        Entradas:
            file_name (str): nombre del archivo de audio a ser seccionado en chunks (audio con el zero padding).
            raw_audio_path (str): path donde esta el archivo a ser seccionado.
            chunk_storage_directory (str): path donde se va a ubicar el archivo seccionado.
            min_silence_len (int): cualquier silencio que dure mas que este valor es recortado.
            silence_thresh (float): cualquier nivel que es menor que este umbral es considerado silencio.
    """
    sound_file = AudioSegment.from_wav(raw_audio_path)
    audio_chunks = split_on_silence(
        sound_file,
        min_silence_len,
        silence_thresh = sound_file.dBFS-silence_thresh
        )
    for i, chunk in enumerate(audio_chunks):
        out_file = f"{chunk_storage_directory}/chunk{i}_de_{file_name}.wav"
        print(f'Audio{i}', out_file)
        chunk.export(out_file, format="wav")

#Ejemplo
# file_name = 'E1'
# raw_audio_path = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3/ExperimentoE/E0_ZP.wav'
# chunk_storage_directory = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3/ExperimentoE/Chunks'
# min_silence_len = 1000
# silence_thresh = 15
# AudioChunker(file_name,raw_audio_path,chunk_storage_directory,min_silence_len,silence_thresh)
