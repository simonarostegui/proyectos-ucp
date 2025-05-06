import random
"""Actividad 2: Piedra, Papel o Tijera
Descripción:
Programar el clásico juego de "Piedra, Papel o Tijera" donde el jugador elige una
opción y la computadora selecciona otra al azar. El programa debe determinar
quién gana según las reglas del juego.
Reglas:
● Piedra gana a Tijera
● Tijera gana a Papel
● Papel gana a Piedra
● Si ambos eligen lo mismo, es un empate
Requisitos:
1. Permitir al usuario seleccionar una opción (piedra, papel o tijera)
2. Generar una selección aleatoria para la computadora
3. Determinar el ganador según las reglas
4. Mostrar las elecciones y el resultado

Extras opcionales:
● Implementar un sistema de puntuación para múltiples rondas
● Añadir las opciones "Lagarto" y "Spock" (versión extendida) <-- ni a palos
● Mostrar estadísticas (victorias, derrotas, empates)"""

def jugar_piedra_papel_tijera():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    while True:
        usuario = input("Elige una opción (piedra, papel, tijera): ").lower()
        computadora = random.choice(["piedra", "papel", "tijera"])

        print(f"El usuario eligió: {usuario}")
        print(f"La computadora eligió: {computadora}")

        if usuario == computadora:
            print("Es un empate")
        else:
            ganador = { #Uso un diccionario para definir las combinaciones ganadoras, key = lo que se tira, value = a lo que le gana
                "piedra": "tijera",
                "tijera": "papel",
                "papel": "piedra"
            }
            
            if ganador[usuario] == computadora: # es un if diccionario[k] == v basicamente
                print("¡Gana el usuario!")
            else:
                print("¡Gana la computadora!")

        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

#Ejecutar el juego solo si se ejecuta directamente
if __name__ == "__main__":
    jugar_piedra_papel_tijera()
