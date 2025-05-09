def BusquedaTransformacion(lista, objetivo):
    lista_transformada = [x for x in lista if x == objetivo]
    return lista_transformada

# Ejemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    objetivo = 5
    resultado = BusquedaTransformacion(lista, objetivo)
    print(f"El objetivo {objetivo} se encuentra en la posicion {resultado} de la lista.")



