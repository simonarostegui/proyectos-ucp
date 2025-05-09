def BusquedaSecuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Ejemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    objetivo = 5
    resultado = BusquedaSecuencial(lista, objetivo)
    print(f"El objetivo {objetivo} se encuentra en la posicion {resultado} de la lista.")


