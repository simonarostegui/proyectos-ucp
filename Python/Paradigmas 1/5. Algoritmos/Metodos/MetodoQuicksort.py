def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2] #se elige el pivote como el valor de la posicion central de la lista
    izquierda = [x for x in lista if x < pivot] #se crea la lista de los valores menores que el pivote
    medio = [x for x in lista if x == pivot] #se crea la lista de los valores iguales al pivote
    derecha = [x for x in lista if x > pivot] #se crea la lista de los valores mayores que el pivote
    return quicksort(izquierda) + medio + quicksort(derecha) #se llama recursivamente a la funcion quicksort para ordenar las listas izquierda y derecha

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = quicksort(lista)
    print("Lista ordenada:", lista_ordenada)




