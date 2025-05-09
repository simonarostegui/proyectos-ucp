def insercion(lista):
    n = len(lista)
    for i in range(1, n):
        key = lista[i] #se guarda el valor de la posicion i
        j = i - 1 #se guarda el valor de la posicion j
        while j >= 0 and key < lista[j]: #mientras j sea mayor o igual a 0 y key sea menor que el valor de la posicion j
            lista[j + 1] = lista[j] #se reemplaza el valor de la posicion j + 1 con el valor de la posicion j
            j -= 1 #se decrementa el valor de j
        lista[j + 1] = key #se guarda el valor de key en la posicion j + 1
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = insercion(lista)
    print("Lista ordenada:", lista_ordenada)


