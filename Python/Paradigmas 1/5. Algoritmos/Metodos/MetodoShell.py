def shell(lista):
    n = len(lista)
    gap = n // 2 #se calcula el gap
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i] #se guarda el valor de la posicion i
            j = i
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap] #se reemplaza el valor de la posicion j con el valor de la posicion j - gap
                j -= gap
            lista[j] = temp #se reemplaza el valor de la posicion j con el valor de temp
        gap //= 2 #se divide el gap por 2
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = shell(lista)
    print("Lista ordenada:", lista_ordenada)
