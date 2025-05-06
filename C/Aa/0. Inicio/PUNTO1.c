#include <stdio.h>
#include <string.h>

int main(){
    char nombre[30];
    char apellido[30];
    int edad;

    printf("Ingrese su nombre:\n");
    scanf("%s", &nombre);
    printf("Ingrese su apellido:\n");
    scanf("%s", &apellido);
    printf("Ingrese su edad: \n");
    scanf("%d", &edad);

    printf("Nombre completo: %s %s.\nEdad: %d", nombre, apellido, edad);

}

