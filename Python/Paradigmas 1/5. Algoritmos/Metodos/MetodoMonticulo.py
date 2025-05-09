def monticulo(lista):
    n = len(lista)
    for i in range(n//2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n-1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)
    return lista

def heapify(lista, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2
    if izquierda < n and lista[i] < lista[izquierda]:
        mayor = izquierda
    if derecha < n and lista[mayor] < lista[derecha]:
        mayor = derecha
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = monticulo(lista)
    print("Lista ordenada:", lista_ordenada)


