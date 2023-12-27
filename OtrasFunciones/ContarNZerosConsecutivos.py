def contar_n_zeros_consecutivos(lista,n):
    count_zeros = 0
    consec_n_zeros = 0
    for num in lista:
        if num == 0:
            count_zeros += 1
            if count_zeros == n:
                consec_n_zeros += 1
                count_zeros = 0
        else:
            count_zeros = 0
    return consec_n_zeros

# Ejemplo de uso
mi_lista = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
n=6
resultado = contar_n_zeros_consecutivos(mi_lista,n)
print("Cantidad de veces que aparecen 10 ceros consecutivos: ", resultado)
