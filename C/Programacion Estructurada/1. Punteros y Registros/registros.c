#include <stdio.h>
#include <stdlib.h> // rand
#include <time.h> // srand time null
#include <string.h> // strcpy

//Arostegui Simon

struct alumno{
    char nombre[100];
    char apellido[100];
    long int legajo;
    int nota[4];
    int notaFinal;
    float asistencia;
};

int main(void){
    srand(time(NULL));
    int i, x, suma = 0;
    char nombreLista[14][40] = {"Fernando", "Jorge", "Nicolas", "Matias", "Juan", "Enzo", "Rodrigo", "Miguel", "Pedro", "Ivan", "Gabriel", "Damian", "Fabian", "Angel"};
    char apellidoLista[13][100] = {"Rodriguez", "Fernandez", "Figueredo", "Ayala", "Cabrera", "Montero", "Porta", "Perani", "Acevedo", "Weiteder", "Riquelme", "Moreno", "Larretta"};

    struct alumno alum[5];
    for (i = 0; i < 5; i++)
    {
        strcpy(alum[i].nombre, nombreLista[rand()%14]); //Genera un nombre de la lista de nombres escritas arriba asi no todos los estudiantes tienen el mismo nombre.
        strcpy(alum[i].apellido, apellidoLista[rand()%13]);
        alum[i].legajo = rand()%100001;
        for (x = 0; x < 4; x++)
        {
            alum[i].nota[x] = rand()%11;
            suma = suma + alum[i].nota[x];
        }
        alum[i].notaFinal = suma/4;
        alum[i].asistencia = ((float)rand()/(float)(RAND_MAX)) * 1.0; // gracias stackoverflow

        suma = 0;
        
    }
    // Elegí separar los getters de los setters, es posible hacerlo con un solo for loop pero me parece mejor hacerlo de esta manera para diferenciar los codigos.
    for (i = 0; i < 5; i++)
    {
        printf("Nombre del alumno: %s\nApellido del alumno: %s\nNumero de Legajo: %li\nPromedio: %i\nAsistencia: %.2f\n", alum[i].nombre, alum[i].apellido, alum[i].legajo, alum[i].notaFinal, alum[i].asistencia);
        if (alum[i].notaFinal > 7 && alum[i].asistencia >= 0.75){ // Si el promedio del alumno es mayor a 7 (es decir 8+) y su asistencia es mayor o igual a 0.75% entonces promociona.
            printf("Alumno promociona.\n");
        }else
        {
            printf("Alumno no promociona.\n");
        }
        printf("\n");
    }   

}