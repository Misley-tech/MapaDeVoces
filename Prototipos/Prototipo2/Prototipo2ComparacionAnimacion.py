import matplotlib.pyplot as plt
import pandas as pd

file_path = 'C:/Users/Asus/OneDrive/Escritorio/MapaDeVoces/Prototipos/Prototipo2/dfPrototipo2.csv'
df = pd.read_csv(file_path)

def update_plot(x):
    plt.plot(x)
    plt.xlabel('Muestras',fontsize = 20)
    plt.xticks(fontsize = 18)
    plt.ylabel('Pitch',fontsize = 20)
    plt.yticks(fontsize = 18)
    plt.pause(0.5)

accumulated_curvas_pitch = []

plt.ion() 
plt.figure(figsize=(18,12))

cant_audios = 57*2
for i in range(cant_audios):
    curvas_pitch = df['curva_pitch'].tolist()
    curva_pitch = curvas_pitch[i][1:-1] 
    curva_pitch = curva_pitch.split(',')
    x = [float(char) for char in curva_pitch]
    accumulated_curvas_pitch.append(x)
    update_plot(x)

plt.pause(5)

plt.ioff()
plt.show()