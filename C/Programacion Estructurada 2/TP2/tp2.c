#include <stdio.h>
#include <stdlib.h>

//Arostegui Simon 4406601


/*Hacer un programa que permita ingresar la información de los alumnos de una determinada
institución (10 alumnos). Los datos se almacenarán en un arreglo con el siguiente formato:
struct alumnos {
int legajo;
char apNom [35];
char carrera [40];
}
Luego de realizada la carga, el programa debe ordenar los datos utilizando el método de burbuja,
en base al número de legajo. Todos los números de legajo comienzan con el numero de 1,
correspondiente a la sede Corrientes, seguido del 2 correspondiente a la carrera ISI y seguido
finalmente por el número de alumno.
Al finalizar mostrar los datos ordenados (legajo y apNom)
*/

struct alumnos {
int legajo;
char apNom [35];
char carrera [40];
};

int main(void)
{
    struct alumnos alumnos[10];
    int i, j;
    struct alumnos aux;
    for (i = 0; i < 10; i++)
    {
        int valido = 0; // valida el ingreso del legajo como numero y se vuelve cero cada iteracion
        do {
            printf("Ingrese el legajo del alumno %d (Formato: 12XXX, donde XXX es el numero de alumno): \n", i + 1);
            if (scanf("%d", &alumnos[i].legajo) == 1) {
                valido = 1;
            } else {
                printf("Error: Ingrese solo numeros.\n");
                fflush(stdin);
            }
        } while (!valido);
        fflush(stdin);
        printf("Ingrese el apellido y nombre del alumno %d: \n", i + 1);
        gets(alumnos[i].apNom); // gets para leer la cadena de caracteres con espacios
        fflush(stdin);
        printf("Ingrese la carrera del alumno %d: \n", i + 1);
        gets(alumnos[i].carrera);
        fflush(stdin);
        printf("\n");
    }
    for (i = 0; i < 10; i++)
    {
        for (j = i + 1; j < 10; j++)
        {
            if (alumnos[i].legajo > alumnos[j].legajo) // compara los legajos y los ordena de mayor a menor
            {
                aux = alumnos[i]; // guarda el valor de alumnos[i] en un auxiliar
                alumnos[i] = alumnos[j]; // guarda el valor de alumnos[j] en alumnos[i]
                alumnos[j] = aux; // guarda el valor de aux en alumnos[j]
            }
        }
    }
    for (i = 0; i < 10; i++)
    {
        printf("Legajo: %d\n", alumnos[i].legajo);
        printf("Apellido y nombre: %s\n", alumnos[i].apNom);
        printf("Carrera: %s\n", alumnos[i].carrera);
        printf("\n");
    }
}