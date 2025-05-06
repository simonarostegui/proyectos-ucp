#include <stdio.h>
#include <stdlib.h>

/* Escriba un programa que te permita cargar en un vector la calificación final -valor entero
entre 0 y 10 – de los 45 alumnos de la materia Introducción a la informática, e informe:
a. Cantidad de alumnos libres
b. Cantidad de alumnos regulares
c. Cantidad de alumnos promocionados
d. Cuál es la nota más alta
e. Cuál es la nota más baja
Nota: las calificaciones deberán generarse de manera aleatoria*/

int main(void)
{
    int i, nota, alumnosLib =0, alumnosReg =0, alumnosProm = 0;
    int alumnos[45] = {0}, notaMayor[2][10], notaMenor[2] = {10, 10}; // Trampa porque notaMenor no tiene asignado nada
    
    for (i = 0; i < 45; i++){
        nota = rand()%11;
        alumnos[i] = nota; 

        if(nota > 6){
            if(nota>= 8){
                alumnosProm++;
            }else{
                alumnosReg++;
            }
        }else{
            alumnosLib++;
        }

        if(nota > notaMayor[2]){
            notaMayor[1][1] = i;
            notaMayor[2][1] = nota;
        } else if (nota < notaMenor[2] && nota >=0){
            notaMenor[1] = i;
            notaMenor[2] = nota;
        }
    }

    for (i = 0; i < 45; i++)
    {
        printf("Alumno %i: %i\n", i, alumnos[i]);
    }
    
    printf("\nCantidad de Alumnos Libres: %i\nCantidad de Alumnos Regulares: %i\nCantidad de Alumnos Promocionados: %i\n", alumnosLib, alumnosReg, alumnosProm);
    printf("Nota Mayor: Alumno %i, Nota %i\nNota Menor: Alumno %i, Nota %i", notaMayor[1], notaMayor[2], notaMenor[1], notaMenor[2]);       

}

