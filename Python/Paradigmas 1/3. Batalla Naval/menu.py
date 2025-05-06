from batalla_naval import *
import os
clear = lambda: os.system('cls')

""" Actividad: BATALLA NAVAL
Consigna:
Los estudiantes aprenderán a diseñar y programar un juego simple ("Batalla
Naval") utilizando estructuras de datos como listas y diccionarios, funciones para
modularizar el código, y lógica para simular una competencia entre un jugador
humano y la máquina.
Para esto deberán desarrollar en Python una versión simplificada del juego
"Batalla Naval" donde un jugador humano compite contra la computadora,
teniendo en cuenta lo siguiente:
• Tablero: 8x8
• Barcos:
* 1 barco de 3 posiciones.
* 2 barcos de 2 posiciones.
* 3 barcos de 1 posición.
Lógica del juego:
* El jugador humano ingresa coordenadas (fila, columna) para
disparar.
* La máquina dispara de forma aleatoria, pero sin repetir coordenadas
* El juego termina cuando uno de los dos hunde todos los barcos del
oponente."""

def menu():
    clear()
    print(f"{bcolors.HEADER}Bienvenido al juego de Batalla Naval{bcolors.ENDC}")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            menu_juego()
        case "2":
            return False
        case _:
            print("Opción inválida")

def menu_juego():
    clear()
    print(f"{bcolors.HEADER}Juego de Batalla Naval{bcolors.ENDC}")
    print("1. Iniciar juego")
    print("2. Ver instrucciones")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            jugar()
        case "2":
            instrucciones()
        case "3":
            return False
        case _:
            print("Opción inválida")

def instrucciones():
    clear()
    print(f"{bcolors.HEADER}Instrucciones del juego de Batalla Naval{bcolors.ENDC}")
    print("1. El jugador ingresa coordenadas (fila, columna) para disparar.")
    print("2. La máquina dispara de forma aleatoria, pero sin repetir coordenadas")
    print("3. El juego termina cuando uno de los dos hunde todos los barcos del oponente.")
    input("Presione Enter para continuar...")
    menu_juego()

def jugar():
    clear()
    mostrar_tablero(tablero)
    colocar_barcos(tablero)
    generar_enemigo(tablero_enemigo)
    while True:
        clear()
        mostrar_tablero(tablero)
        print(" ") # Espacio en blanco
        mostrar_tablero_enemigo(tablero_enemigo_descubierto)
        print(" ") # Espacio en blanco
        disparar(tablero_enemigo)
        generar_enemigo_disparo(tablero)
        if verificar_barcos_hundidos(tablero_enemigo):
            print(f"{bcolors.OKGREEN}¡Has ganado!{bcolors.ENDC}")
            break
        if verificar_barcos_hundidos(tablero):
            print(f"{bcolors.FAIL}¡Has perdido!{bcolors.ENDC}")
            break
    menu_juego()

menu()
