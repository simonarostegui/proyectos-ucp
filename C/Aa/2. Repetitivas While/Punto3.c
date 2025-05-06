#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i=0,cantidad=0;

    while(i<=150){
        if(i>=20 && i%2==0){
            printf("%i es un numero par.\n", i);
            cantidad++;
        }
        i++;
    }
    printf("La cantidad de numeros pares es: %i.", cantidad);
}
