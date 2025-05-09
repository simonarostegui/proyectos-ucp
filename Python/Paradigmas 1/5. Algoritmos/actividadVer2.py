from datetime import datetime

import sys
sys.path.insert(0, "./Metodos") # Reconoce el directorio de los métodos
sys.path.insert(0, "./Busquedas") # Reconoce el directorio de las búsquedas

from Metodos.MetodoShell import shell # Importa el método de Shell
from Metodos.MetodoQuicksort import quicksort # Importa el método de Quicksort, no es usado en este programa
from Busquedas.BusquedaSecuencial import BusquedaSecuencial # Importa la búsqueda secuencial
from Busquedas.BusquedaBinaria import busquedaBinaria # Importa la búsqueda binaria, no es usado en este programa

"""
Consigna:
Un emprendimiento de venta online guarda información de las transacciones realizadas por fecha y monto. Necesita:
• ordenar los datos por fecha o monto
• mostrar los datos ordenados por fecha o monto
• buscar por fecha o monto, e informar si se encuentra o no

Deberán elegir un algoritmo de ordenamiento:
Logarítmicos:
* Método de Shell (Inserción con incrementos decrecientes)
* Método de QuickSort (Clasificación Rápida)

Y un algoritmo de búsqueda
• Búsqueda secuencial o lineal
• Búsqueda binaria

Elaborar una propuesta de la solución al problema, en Python, utilizando los algoritmos seleccionados.
"""

transacciones = {'15/05/2024': 100,
                 '10/12/2025': 740, 
                 '20/05/2024': 200, 
                 '12/07/2024': 1000, 
                 '05/09/2024': 400, 
                 '25/03/2025': 500}

def ordernarFecha():
    global transacciones
    items = list(transacciones.items()) # Convertir el diccionario a una lista de tuplas (fecha, monto)
    items.sort(key=lambda x: datetime.strptime(x[0], '%d/%m/%Y')) # Convertir las fechas a datetime para ordenar, key es el valor de la tupla que se va a ordenar y lambda es una funcion anonima que recibe x y devuelve x[0] que es la fecha
    transacciones = dict(items) # Reconstruir el diccionario ordenado
    return transacciones

def ordernarMonto():
    global transacciones
    items = list(transacciones.items()) # Convertir el diccionario a una lista de tuplas (fecha, monto)
    items.sort(key=lambda x: x[1]) # Ordenar por monto, key es el valor de la tupla que se va a ordenar y lambda es una funcion anonima que recibe x y devuelve x[1] que es el monto
    transacciones = dict(items) # Reconstruir el diccionario ordenado
    return transacciones

def buscarFecha(fecha):
    global transacciones
    fecha = str(fecha)
    fecha_buscar = datetime.strptime(fecha, '%d/%m/%Y')# Convertir las fechas a datetime para comparación
    for i, (fecha_dict, monto) in enumerate(transacciones.items()): #enumerate es una funcion que devuelve un iterador de tuplas (indice, valor), i es el indice y fecha_dict es la fecha y monto es el monto
        if datetime.strptime(fecha_dict, '%d/%m/%Y') == fecha_buscar:
            return f"La fecha {fecha} se encuentra en la posición {i} con monto {monto}"
    return f"La fecha {fecha} no se encuentra en la lista"

def buscarMonto(monto):
    global transacciones
    monto = int(monto)
    for i, (fecha, monto_dict) in enumerate(transacciones.items()):
        if monto_dict == monto:
            return f"El monto {monto} se encuentra en la posición {i} con fecha {fecha}"
    return f"El monto {monto} no se encuentra en la lista"

def main():
    while True:
        print("\nBienvenido al sistema de transacciones")
        print("Transacciones actuales:")
        for fecha, monto in transacciones.items():
            print(f"Fecha: {fecha}, Monto: {monto}")
        print("\n1. Ordenar por fecha")
        print("2. Ordenar por monto")
        print("3. Buscar por fecha")
        print("4. Buscar por monto")
        print("5. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print("\nTransacciones ordenadas por fecha:")
                for fecha, monto in ordernarFecha().items():
                    print(f"Fecha: {fecha}, Monto: {monto}")
            case 2:
                print("\nTransacciones ordenadas por monto:")
                for fecha, monto in ordernarMonto().items():
                    print(f"Fecha: {fecha}, Monto: {monto}")
            case 3:
                fecha = input("Ingrese una fecha (formato dd/mm/yyyy): ")
                print(buscarFecha(fecha))
            case 4:
                monto = input("Ingrese un monto: ")
                print(buscarMonto(monto))
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
        if opcion == 5:
            break

if __name__ == "__main__":
    main()
