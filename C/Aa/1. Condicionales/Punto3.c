#include <stdio.h>
#include <string.h>

int main(){
    int valor, i, aux;

    printf("Ingrese un numero:\n");
    scanf("%d", &valor);

    for (i=1; i<11; i++){
        aux = valor * i;
        printf("\n%d x %d = %d", valor, i, aux);
        aux = 0;
    }
}
