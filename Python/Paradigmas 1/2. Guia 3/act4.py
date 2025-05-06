
"""Actividad 4: Triángulo de Pascal
Descripción:
Escribir un programa que genere y muestre el Triángulo de Pascal hasta un
número de filas especificado por el usuario.
Requisitos:
1. Solicitar al usuario el número de filas a generar
2. Calcular los valores del Triángulo de Pascal para cada posición
3. Mostrar el triángulo con un formato adecuado"""

def generar_triangulo_pascal(filas):
    triangulo = [[1]]
    for i in range(1, filas):
        fila = [1]
        for j in range(1, i):
            fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
        fila.append(1)
        triangulo.append(fila)
    return triangulo

def mostrar_triangulo(triangulo):
    for fila in triangulo:  
        print(" ".join(str(x) for x in fila))

def jugar_triangulo_pascal():
    filas = int(input("Ingrese el numero de filas para el triangulo de Pascal: "))
    triangulo = generar_triangulo_pascal(filas)
    mostrar_triangulo(triangulo)
    
#Ejecutar el juego solo si se ejecuta directamente
if __name__ == "__main__":
    jugar_triangulo_pascal()

