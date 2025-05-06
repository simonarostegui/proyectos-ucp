#include <stdio.h>
#include <string.h>

int main(void){
    char nombre[50];
    char apellido[50];

    printf("Ingrese su nombre:\n");
    gets(nombre);
    printf("Ingrese su apellido:\n");
    gets(apellido);

    printf("\nNombre Completo:\n%s %s\n%c. %c.\n", nombre, apellido, nombre[0], apellido[0]);
}
