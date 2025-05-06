"""Actividad 5: Menú de Juegos
Descripción:
Integrar todas las actividades anteriores en un solo programa con un menú que
permita al usuario elegir qué juego desea jugar.
Requisitos:
1. Crear un menú principal que muestre las opciones disponibles
2. Implementar la lógica para navegar entre los diferentes juegos
3. Permitir volver al menú principal después de cada juego
4. Incluir una opción para salir del programa"""

import act1
import act2
import act3
import act4

def menu():
    while True:
        print("\nMenú de Juegos")
        print("1. Adivina el numero")
        print("2. Piedra, Papel o Tijera")
        print("3. Ahorcado")
        print("4. Triángulo de Pascal")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                act1.jugar_adivina_numero()
            case "2":
                act2.jugar_piedra_papel_tijera()
            case "3":
                act3.jugar_ahorcado() 
            case "4":
                act4.jugar_triangulo_pascal()
            case "5":
                print("¡Gracias por jugar!")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
