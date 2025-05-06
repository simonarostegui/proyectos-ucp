#include <stdio.h>
#include <string.h>

int main()
{
    int nota1, nota2, nota3, nota4, auxiliar, promedio;
    float asistencia; // Float por si el alumno copia y pega directamente desde la pagina de la facultad
    
    promedio = 0;
    while (promedio == 0){ 
        printf("Ingrese su nota del Trabajo Practico 1: \n");
        scanf("%d", &nota1);
        printf("Ingrese la nota del Trabajo Practico 2: \n");
        scanf("%d", &nota2);
        printf("Ingrese la nota del Parcial: \n");
        scanf("%d", &nota3);
        printf("Ingrese la nota del Trabajo Practico Integrador: \n");
        scanf("%d", &nota4);
        printf("Ingrese el porcentaje de su asistencia:\n");
        scanf("%f", &asistencia);
        
        //Verifica si alguna de las notas es mayor a 10, por las dudas
        if(nota1 > 10 || nota2 > 10 || nota3 > 10 || nota4 > 10){
            printf("Una de sus notas es mayor a 10! Intente denuevo.\n\n");
        }else{
        auxiliar = nota1 + nota2 + nota3 + nota4;
        promedio = auxiliar / 4;} // Rompe el bucle calculando el promedio
    }

    printf("\nTu promedio es %d\nTu asistencia es %d\n\n", promedio, (int)asistencia); // Quiero mostrar el valor como entero

    if (promedio >= 6){
        if(promedio >= 8){
            if ((int)asistencia > 75)
            {
                printf("Promocionaste! Felicidades!");

            }else{
                printf("No aprobaste! Faltaste demasiado, suerte en el recuperatorio");
            }
        } else {
            if ((int)asistencia > 75){
                printf("Aprobaste pero no promocionaste, suerte en el final!");
            }else{
                printf("No aprobaste! Faltaste demasiado, suerte en el recuperatorio");
            }
        } 
    } else {
        printf("Desaprobaste! Suerte en el recuperatorio.");
    }    
}
