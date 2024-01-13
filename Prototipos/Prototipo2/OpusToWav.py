#Si pongo esto en el cmd anda joya
#Linea 1: "C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo2/Audios"
#Linea 2: "ffmpeg -i HolaComoEstas0.opus HolaComoEstas0.wav"

my_list = [f'ffmpeg -i HolaComoEstas{i}.opus HolaComoEstas{i}.wav' for i in range(57)]

with open("CopiarEnCMD.txt", "w") as file:
    for item in my_list:
        file.write(f"{str(item)}/n")

#copiar y pegar cada renglon de este txt 