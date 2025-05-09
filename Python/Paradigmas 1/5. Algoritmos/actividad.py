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

fechas = ['15/05/2024', '10/12/2025', '20/05/2024', '12/07/2024', '05/05/2024', '15/05/2025']
montos = [100, 740, 200, 1000, 400, 500]
    
#Decidi usar el metodo de shell para ordenar las fechas y los montos, ya que es un metodo logaritmico y es mas eficiente para ordenar grandes cantidades de datos
def ordernarFecha():
    global fechas
    fechas_datetime = [datetime.strptime(fecha, '%d/%m/%Y') for fecha in fechas] # Convertir las fechas a datetime
    fechas_datetime = shell(fechas_datetime) # Ordenar las fechas datetime
    fechas = [fecha.strftime('%d/%m/%Y') for fecha in fechas_datetime] # Convertir de vuelta a strings en el formato original
    return fechas

def ordernarMonto():
    global montos
    montos = shell(montos)
    return montos

#Decidi usar la busqueda secuencial para buscar las fechas y los montos, ya que es un metodo lineal y es mas eficiente para buscar pequeñas cantidades de datos
def buscarFecha(fecha):
    global fechas
    fecha = str(fecha)
    posicion = BusquedaSecuencial(fechas, fecha)
    if posicion != -1:
        return f"La fecha {fecha} se encuentra en la posición {posicion}"
    else:
        return f"La fecha {fecha} no se encuentra en la lista"

def buscarMonto(monto):
    global montos
    monto = int(monto)
    posicion = BusquedaSecuencial(montos, monto)
    if posicion != -1:
        return f"El monto {monto} se encuentra en la posición {posicion}"
    else:
        return f"El monto {monto} no se encuentra en la lista"

def main():
    while True:
        print("Bienvenido al sistema de transacciones")
        print("Fechas: ", fechas)
        print("Montos: ", montos)
        print("1. Ordenar por fecha")
        print("2. Ordenar por monto")
        print("3. Buscar por fecha")
        print("4. Buscar por monto")
        print("5. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print(ordernarFecha())
            case 2:
                print(ordernarMonto())
            case 3:
                print(buscarFecha(input("Ingrese una fecha: ")))
            case 4:
                print(buscarMonto(input("Ingrese un monto: ")))
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
        if opcion == 5:
            break

if __name__ == "__main__":
    main()
