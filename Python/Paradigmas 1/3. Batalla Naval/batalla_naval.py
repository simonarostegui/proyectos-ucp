import random
import os
clear = lambda: os.system('cls')

"""Recursos usados:
https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
https://stackoverflow.com/questions/63569902/whats-the-meaning-of-print-end-in-python
https://www.reddit.com/r/learnpython/comments/f973yq/how_to_add_ships_to_a_python_battleship_game/
https://stackoverflow.com/questions/75934801/simplifying-code-for-placing-ships-in-battleship-game-in-python-and-conducting-u
"""
# Códigos de color ANSI
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

barcos = { 
    "fragata 1": 1,
    "fragata 2": 1,
    "fragata 3": 1,
    "destructor 1": 2,
    "destructor 2": 2,
    "submarino": 3,
}

tablero = [[" " for _ in range(8)] for _ in range(8)]
tablero_enemigo_descubierto = [[" " for _ in range(8)] for _ in range(8)]
tablero_enemigo = [[" " for _ in range(8)] for _ in range(8)]

def mostrar_tablero(tablero):
    print(f"{bcolors.HEADER}Tablero de usuario:{bcolors.ENDC}")
    print("  0 1 2 3 4 5 6 7")
    for i, fila in enumerate(tablero):
        print(f"{i} ", end="")
        for celda in fila:
            if celda == "X":  # Barco golpeado
                print(f"{bcolors.FAIL}{bcolors.BOLD}X{bcolors.ENDC} ", end="") # end="" para que no se salte de linea
            elif celda == "O":  # Disparo fallado
                print(f"{bcolors.OKBLUE}O{bcolors.ENDC} ", end="")
            elif celda in [b[0].upper() for b in barcos]:  # Barco no golpeado
                print(f"{bcolors.BOLD}{celda}{bcolors.ENDC} ", end="")
            else:  # Espacio vacío
                print(f"{celda} ", end="")
        print()

def mostrar_tablero_enemigo(tablero):
    print(f"{bcolors.HEADER}Tablero Enemigo Descubierto:{bcolors.ENDC}")
    print("  0 1 2 3 4 5 6 7")
    for i, fila in enumerate(tablero):
        print(f"{i} ", end="")
        for celda in fila:
            if celda == "X":  # Barco golpeado
                print(f"{bcolors.FAIL}{bcolors.BOLD}X{bcolors.ENDC} ", end="")
            elif celda == "O":  # Disparo fallado
                print(f"{bcolors.OKBLUE}O{bcolors.ENDC} ", end="")
            else:  # Espacio vacío
                print(f"{celda} ", end="")
        print()

def colocar_barcos(tablero):
    for barco, tamaño in barcos.items():
        while True:
            try:
                print(f"\n{bcolors.OKGREEN}Colocando {barco} (tamaño: {tamaño}){bcolors.ENDC}")
                fila = int(input("Ingrese la fila inicial (0-7): "))
                columna = int(input("Ingrese la columna inicial (0-7): "))
                direccion = input("Ingrese la dirección (H para horizontal, V para vertical): ").upper()
                
                if direccion not in ['H', 'V']:
                    print(f"{bcolors.FAIL}Dirección inválida. Use H para horizontal o V para vertical.{bcolors.ENDC}")
                    continue
                
                # Verificar si el barco cabe en la dirección elegida
                if direccion == 'H' and columna + tamaño > 8:
                    print(f"{bcolors.FAIL}El barco no cabe horizontalmente en esa posición.{bcolors.ENDC}")
                    continue
                if direccion == 'V' and fila + tamaño > 8:
                    print(f"{bcolors.FAIL}El barco no cabe verticalmente en esa posición.{bcolors.ENDC}")
                    continue
                
                # Verificar si los espacios están disponibles
                espacios_disponibles = True
                for i in range(tamaño):
                    if direccion == 'H':
                        if tablero[fila][columna + i] != " ":
                            espacios_disponibles = False
                            break
                    else:  # V
                        if tablero[fila + i][columna] != " ":
                            espacios_disponibles = False
                            break
                
                if not espacios_disponibles:
                    print(f"{bcolors.FAIL}Hay barcos en el camino. Intente otra posición.{bcolors.ENDC}")
                    continue
                
                # Colocar el barco
                for i in range(tamaño):
                    if direccion == 'H':
                        tablero[fila][columna + i] = barco[0].upper() # Uso i para que se pueda colocar el barco en la misma fila pero columna diferente
                    else:  # V
                        tablero[fila + i][columna] = barco[0].upper() # Lo mismo pero para la dirección vertical
                
                clear()
                mostrar_tablero(tablero)
                break
                
            except ValueError:
                print(f"{bcolors.FAIL}Por favor ingrese números válidos.{bcolors.ENDC}")

def generar_enemigo(tablero_enemigo):
    for barco, tamaño in barcos.items():
        while True:
            # Elegir dirección aleatoria
            direccion = random.choice(['H', 'V'])
            
            if direccion == 'H':
                fila = random.randint(0, 7)
                columna = random.randint(0, 8 - tamaño)
            else:  # V
                fila = random.randint(0, 8 - tamaño)
                columna = random.randint(0, 7)
            
            # Verificar si los espacios están disponibles
            espacios_disponibles = True
            for i in range(tamaño):
                if direccion == 'H':
                    if tablero_enemigo[fila][columna + i] != " ":
                        espacios_disponibles = False
                        break
                else:  # V
                    if tablero_enemigo[fila + i][columna] != " ":
                        espacios_disponibles = False
                        break
            
            if espacios_disponibles:
                # Colocar el barco
                for i in range(tamaño):
                    if direccion == 'H':
                        tablero_enemigo[fila][columna + i] = barco[0].upper()
                    else:  # V
                        tablero_enemigo[fila + i][columna] = barco[0].upper()
                break

def disparar(tablero):
    while True:
        try:
            fila = int(input("Ingrese la fila para disparar (0-7): "))
            columna = int(input("Ingrese la columna para disparar (0-7): "))
            if 0 <= fila < 8 and 0 <= columna < 8:
                if tablero_enemigo[fila][columna] == " ":
                    tablero_enemigo[fila][columna] = "O"
                    tablero_enemigo_descubierto[fila][columna] = "O"
                    print(f"{bcolors.FAIL}Has fallado{bcolors.ENDC}")
                    print(" ")
                    break
                elif tablero_enemigo[fila][columna] in [b[0].upper() for b in barcos]:
                    tablero_enemigo[fila][columna] = "X"
                    tablero_enemigo_descubierto[fila][columna] = "X"
                    print(f"{bcolors.OKGREEN}Has golpeado un barco{bcolors.ENDC}")
                    print(" ")
                    break
                else:
                    print(f"{bcolors.FAIL}Ya disparaste en esa posición, intente nuevamente.{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Las coordenadas deben estar entre 0 y 7.{bcolors.ENDC}")
        except ValueError:
            print(f"{bcolors.FAIL}Por favor ingrese números válidos.{bcolors.ENDC}")

def generar_enemigo_disparo(tablero):
    while True:
        fila = random.randint(0, 7)
        columna = random.randint(0, 7)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            print(f"{bcolors.OKCYAN}El enemigo ha disparado en la posición {fila}, {columna}{bcolors.ENDC}")
            input("Presione Enter para continuar...")
            clear()
            break
        elif tablero[fila][columna] in [b[0].upper() for b in barcos]:
            tablero[fila][columna] = "X"
            print(f"{bcolors.FAIL}El enemigo ha golpeado tu barco en la posición {fila}, {columna}{bcolors.ENDC}")
            input("Presione Enter para continuar...")
            clear()
            break

def verificar_barcos_hundidos(tablero): 
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna] in [b[0].upper() for b in barcos]: # Recorre el tablero y verifica si hay barcos, si hay, retorna False
                return False
    return True #Si no hay barcos, retorna True
