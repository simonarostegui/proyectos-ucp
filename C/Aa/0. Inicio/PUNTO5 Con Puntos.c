#include <stdio.h>
#include <string.h>

int main()
{
    char dni[30], nombrecompleto[30];
    int nota1, nota2, nota3, nota4, promedio, auxiliar;
    
    promedio = 0;
    printf("Ingrese su nombre completo:\n");
    scanf("%30[^\n]", nombrecompleto); //Gracias StackOverflow, no se que es [^\n] pero funciona
    printf("Ingrese su DNI:\n");
    scanf(" %30[^\n]", dni); //El espacio es necesario porque si no el espacio es tomado en el string DNI
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
    
    printf("Nombre Completo: %s\nDNI: %s\nPromedio: %d.", nombrecompleto, dni, promedio);
}
