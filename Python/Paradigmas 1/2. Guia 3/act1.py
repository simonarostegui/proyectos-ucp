import random
""" Actividad 1: Adivina el Número
Descripción:
Desarrollar un juego donde la computadora elija un número aleatorio entre 1 y 10,
y el jugador debe adivinarlo. El programa proporcionará pistas indicando si el
número ingresado es mayor o menor que el número secreto, y al final mostrará la
cantidad de intentos realizados.
Requisitos:
1. Generar un número aleatorio entre 1 y 10
2. Solicitar al usuario que ingrese un número
3. Comparar el número ingresado con el número secreto
4. Mostrar pistas ("El número es mayor" o "El número es menor")
5. Contar los intentos y mostrarlos al finalizar el juego
Extras opcionales:
● Permitir que el jugador defina el rango de números (por ejemplo, de 1 a
100)
● Implementar un límite de intentos (por ejemplo, 5 intentos máximo)
● Añadir la opción de jugar nuevamente sin reiniciar el programa"""

def adivina_el_numero(max_intentos, rango_min, rango_max):
    numero_secreto = random.randint(rango_min, rango_max)
    intentos = 0

    print("Bienvenido al juego de adivinar el número")

    while intentos < max_intentos:
        try:
            numero_usuario = int(input("Ingresa un número: "))

            if numero_usuario == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos + 1} intentos.")
                break

            elif numero_usuario < numero_secreto:
                print("El número es mayor")

            else:
                print("El número es menor")
        
        except ValueError: #gracias stackoverflow, si no es un numero, no se puede jugar
            print("Por favor, ingresa un número válido.")

        intentos += 1

    if intentos == max_intentos:
        print(f"Lo siento, has agotado tus intentos. El número secreto era {numero_secreto}.")

def jugar_adivina_numero():
    while True:
        rango_min = int(input("¿Cuál es el rango mínimo? (ejemplo: 1) "))
        rango_max = int(input("¿Cuál es el rango máximo? (ejemplo: 100) "))
        max_intentos = int(input("¿Cuántos intentos quieres tener? (ejemplo: 5) "))
        adivina_el_numero(max_intentos, rango_min, rango_max)
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        
        if respuesta != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

#Ejecutar el juego solo si se ejecuta directamente
if __name__ == "__main__":
    jugar_adivina_numero()

        
    
