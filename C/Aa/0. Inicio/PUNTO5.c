#include <stdio.h>
#include <string.h>

int main()
{
    
    char nombrecompleto[30];
    int nota1, nota2, nota3, nota4, promedio, auxiliar, dni;
    
    promedio = 0;
    printf("Ingrese su nombre completo:\n");
    scanf("%s", &nombrecompleto);
    printf("Ingrese su DNI sin numeros:\n");
    scanf("%i", &dni);
    while (promedio == 0){ 
        printf("Ingrese su nota del Trabajo Practico 1: \n");
        scanf("%d", &nota1);
        printf("Ingrese la nota del Trabajo Practico 2: \n");
        scanf("%d", &nota2);
        printf("Ingrese la nota del Parcial: \n");
        scanf("%d", &nota3);
        printf("Ingrese la nota del Trabajo Practico Integrador: \n");
        scanf("%d", &nota4);
        
        //Verifica si alguna de las notas es mayor a 10, por las dudas
        if(nota1 > 10 || nota2 > 10 || nota3 > 10 || nota4 > 10){
            printf("Una de sus notas es mayor a 10! Intente denuevo.\n\n");
        }else{
        auxiliar = nota1 + nota2 + nota3 + nota4;
        promedio = auxiliar / 4;} // Rompe el bucle calculando el promedio
    }
    
    printf("Nombre Completo: %s\nDNI: %i\nPromedio:%d.", nombrecompleto, dni, promedio);
}
