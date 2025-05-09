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
    fechas_datetime = [datetime.strptime(fecha, '%d/%m/%Y') for fecha in transacciones.keys()] # Convertir fechas a datetime para ordenar
    fechas_ordenadas = shell(fechas_datetime) # Ordenar fechas usando Shell
    nuevo_dict = {} # Crear nuevo diccionario ordenado
    for fecha in fechas_ordenadas:
        fecha_str = fecha.strftime('%d/%m/%Y')
        nuevo_dict[fecha_str] = transacciones[fecha_str]
    transacciones = nuevo_dict
    return transacciones

def ordernarMonto():
    global transacciones
    items = [(monto, fecha) for fecha, monto in transacciones.items()] # Convertir a lista de tuplas (monto, fecha) para ordenar por monto
    montos_ordenados = shell([monto for monto, _ in items]) # Ordenar montos usando Shell
    nuevo_dict = {} # Crear nuevo diccionario ordenado
    for monto in montos_ordenados:
        for fecha, m in transacciones.items():
            if m == monto and fecha not in nuevo_dict:
                nuevo_dict[fecha] = monto
                break
    transacciones = nuevo_dict
    return transacciones

def buscarFecha(fecha):
    global transacciones
    fecha = str(fecha)
    fecha_buscar = datetime.strptime(fecha, '%d/%m/%Y') # Convertir fecha a datetime para búsqueda
    fechas_lista = [datetime.strptime(f, '%d/%m/%Y') for f in transacciones.keys()] # Convertir todas las fechas a datetime para búsqueda
    posicion = BusquedaSecuencial(fechas_lista, fecha_buscar) # Buscar usando búsqueda secuencial
    if posicion != -1:
        fecha_encontrada = list(transacciones.keys())[posicion]
        return f"La fecha {fecha} se encuentra en la posición {posicion} con monto ${transacciones[fecha_encontrada]}"
    return f"La fecha {fecha} no se encuentra en la lista"

def buscarMonto(monto):
    global transacciones
    monto = int(monto)
    montos_lista = list(transacciones.values()) # Convertir montos a lista para búsqueda
    posicion = BusquedaSecuencial(montos_lista, monto) # Buscar usando búsqueda secuencial
    if posicion != -1:
        fecha_encontrada = list(transacciones.keys())[posicion]
        return f"El monto ${monto} se encuentra en la posición {posicion} con fecha {fecha_encontrada}"
    return f"El monto ${monto} no se encuentra en la lista"

def main():
    while True:
        print("\nBienvenido al sistema de transacciones")
        print("Transacciones actuales:")
        for fecha, monto in transacciones.items():
            print(f"Fecha: {fecha}, Monto: ${monto}")
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
                    print(f"Fecha: {fecha}, Monto: ${monto}")
            case 2:
                print("\nTransacciones ordenadas por monto:")
                for fecha, monto in ordernarMonto().items():
                    print(f"Fecha: {fecha}, Monto: ${monto}")
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
