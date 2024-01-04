from pydub import AudioSegment
from pydub.silence import split_on_silence

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

def RecortarTodasLasPalabras(cant_audios,raw_audio_path_main,chunk_storage_directory_main,chunk_name_folder,min_silence_len,silence_thresh):
    """
    Toma varios audios ubicados en una carpeta y a cada uno de los audios lo secciona por silencios en chunks y luego los ubica en distintas carpetas.
    Utiliza la funcion AudioChunker. Ejemplo: si los audios son E1_ZP,E2_ZP,...,E30_ZP 
    Arguments:
        cant_audios (int): cantidad de audios a ser segmentados
        raw_audio_path_main (str): path de la carpeta donde estan ubicados totos los audios a ser segmentados
        chunk_storage_directory_main (str): path de la carpeta donde van a ser ubicados los archivos
        chunk_name_folder (str): nombre de la subcarpeta donde se va a ubicar el i-esimo chunk. Ej: los chunks del audio E15_ZP van ubicados en la carpeta ChunkE15_ZP.
        min_silence_len (int): cualquier silencio que dure mas que este valor es recortado.
        silence_thresh (list de floats): cualquier nivel que es menor que este umbral es considerado silencio
    """
    for i in range(cant_audios):
        raw_audio_path = f'{raw_audio_path_main}/{file_names[i]}.wav'
        chunk_storage_directory = f'{chunk_storage_directory_main}/{chunk_name_folder}{file_names[i]}'
        AudioChunker(file_names[i],raw_audio_path,chunk_storage_directory,min_silence_len,silence_thresh[i])

# Ejemplo.
# El jerarquia de las carpetas es asi:
# ExperimentosE
# |-- Chunks
# |   |-- ChunksE0_ZP
# |   |   |-- chunk0_de_E0_ZP.wav
# |   |   |-- chunk1_de_E0_ZP.wav
# |   |   |-- chunk2_de_E0_ZP.wav
# |   |   |-- . ..
# |   |   |-- chunk23_de_E0_ZP.wav
# |   |-- ChunksE1_ZP
# |   |   |-- chunk0_de_E1_ZP.wav
# |   |   |-- chunk1_de_E1_ZP.wav
# |   |   |-- chunk2_de_E1_ZP.wav
# |   |   |-- ...
# |   |   |-- chunk14_de_E1_ZP.wav
# |   |-- ChunksE2_ZP
# |   |   |-- chunk0_de_E2_ZP.wav
# |   |   |-- chunk1_de_E2_ZP.wav
# |   |   |-- chunk2_de_E2_ZP.wav
# |   |   |-- ...
# |   |   |-- chunk20_de_E2_ZP.wav
# |   |     ...
# |   |-- ChunksE28_ZP
# |   |   |-- chunk0_de_E28_ZP.wav
# |   |   |-- chunk1_de_E28_ZP.wav
# |   |   |-- chunk2_de_E28_ZP.wav
# |   |   |-- ...
# |   |   |-- chunk11_de_E28_ZP.wav
# |
# |-- ZP
# |   |-- E0_ZP.wav
# |   |-- E1_ZP.wav
# |   |-- ...
# |   |-- E28_ZP.wav
# |
# |-- ZP_pitcheados
# |   |-- E0_ZP_pitcheado.wav
# |   |-- E1_ZP_pitcheado.wav
# |   |-- ...
# |   |-- E28_ZP_pitcheado.wav

cant_audios=29
file_names = [f'E{i}_ZP' for i in range(cant_audios)]
raw_audio_path_main = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3/ExperimentoE/ZP'
chunk_storage_directory_main = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo3/AudiosPrototipo3/ExperimentoE/ZP_pitcheados'
chunk_name_folder = 'Chunk'
min_silence_len = 1000
silence_thresh = [15]*cant_audios
RecortarTodasLasPalabras(cant_audios,raw_audio_path_main,chunk_storage_directory_main,chunk_name_folder,min_silence_len,silence_thresh)
