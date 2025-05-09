def seleccion(lista):
    n = len(lista)
    for i in range(n-1): #se recorre la lista
        min_idx = i #se guarda el valor de la posicion en la que se encuentra el minimo
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]: #si el valor de la posicion j es menor que el valor de la posicion min_idx
                min_idx = j #se guarda el valor de la posicion j
        lista[i], lista[min_idx] = lista[min_idx], lista[i] #se intercambian los valores de la posicion i y la posicion min_idx
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = seleccion(lista)
    print("Lista ordenada:", lista_ordenada)


