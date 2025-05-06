#include <stdio.h>

/*Haga el programa principal y tres funciones sin paso de parámetros:

a) menú de opción

b) sumar dos números enteros

c) multiplicar dos números enteros.*/

int a, b;
void menu();
void sumar();
void multiplicar();

int main()
{
    menu();
}

void menu(){
    int opcion;

    printf("Ingrese la opcion que desea hacer: (1. Sumar - 2. Multiplicar)\n");
    scanf("%i", &opcion);

    if (opcion == 1) {
        sumar();
    } else if (opcion == 2) {
        multiplicar();
    } else {
        printf("Opcion no valida");
    }
}

void sumar(){
    printf("Ingrese el valor entero A que desea sumar.\n");
    scanf("%i", &a);
    printf("Ingrese el valor entero B que desea sumar:\n");
    scanf("%i", &b);
    printf("%i + %i = %i\n", a, b, a + b);
}

void multiplicar(){
    printf("Ingrese el valor entero A que desea multiplicar.\n");
    scanf("%i", &a);
    printf("Ingrese el valor entero B que desea multiplicar:\n");
    scanf("%i", &b);
    printf("%i * %i = %i\n", a, b, a * b);
}