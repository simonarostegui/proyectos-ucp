#include <stdio.h>
#include <string.h>

int main()
{
    char nombre[50];

    printf("Ingrese su nombre:\n");
    gets(nombre);

    strrev(nombre); //Función de string.h que reverse un string, el unico problema es que directamente lo asigna.
    
    printf("Nombre: %s\n", nombre);
}
