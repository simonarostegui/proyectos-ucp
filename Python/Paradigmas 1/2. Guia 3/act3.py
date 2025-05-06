import random
"""
Actividad 3: El Juego del Ahorcado
Descripción:
Desarrollar un juego de Ahorcado donde la computadora elige una palabra al azar
y el jugador debe adivinarla letra por letra dentro de un número limitado de
intentos.
Requisitos:
1. Seleccionar una palabra aleatoria de una lista predefinida
2. Mostrar la palabra oculta con guiones bajos (_)
3. Permitir al jugador ingresar letras una por una
4. Actualizar la visualización de la palabra revelando las letras acertadas
5. Controlar los intentos fallidos
6. Determinar si el jugador ganó o perdió
Extras opcionales:
● Mostrar un dibujo ASCII del ahorcado que se actualiza con cada error
● Permitir al jugador elegir la dificultad (cantidad de intentos)
● Implementar categorías de palabras (animales, países, etc.)"""

lista_palabras = {
    "paises" : ["argentina", "brasil", "chile", "colombia", "ecuador", "venezuela"],
    "animales" : ["perro", "gato", "pajaro", "tigre", "elefante", "jirafa"],
    "frutas" : ["manzana", "naranja", "banana", "uva", "pera", "fresa"],
    "colores" : ["rojo", "azul", "verde", "amarillo", "morado", "naranja"]
}

def jugar_ahorcado():
    print("Bienvenido al juego del Ahorcado")
    while True:
        categoria = random.choice(list(lista_palabras.keys()))
        palabra_secreta = random.choice(lista_palabras[categoria])
        intentos = 6
        letras_adivinadas = []

        print(f"Adivina la palabra de la categoria: {categoria}")
        print("_" * len(palabra_secreta))

        while intentos > 0:
            letra = input("Ingresa una letra: ").lower()

            if letra in letras_adivinadas:
                print("Ya has adivinado esa letra")
                continue
            
            if letra in palabra_secreta:
                letras_adivinadas.append(letra)
            else:
                intentos -= 1
                print(f"Letra incorrecta. Te quedan {intentos} intentos")
                
            palabra_mostrada = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
            print(palabra_mostrada.capitalize())

            if palabra_mostrada == palabra_secreta:
                print(f"¡Felicidades! Adivinaste la palabra {palabra_secreta.capitalize()} en {len(letras_adivinadas)} intentos")
                break
            
        if intentos == 0:
            print(f"Lo siento, has agotado tus intentos. La palabra era {palabra_secreta.capitalize()}")

        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

#Ejecutar el juego solo si se ejecuta directamente
if __name__ == "__main__":
    jugar_ahorcado()
