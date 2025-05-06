#include <stdio.h>

int main(){
    int n1, n2, aux1;

    printf("Ingrese un valor:\n");
    scanf("%d", &n1);
    printf("Ingrese otro valor:\n");
    scanf("%d", &n2);
    
    printf("\nA: %d, B: %d.\nPero ahora:\n", n1, n2); //Para poder visualizar el cambio
    aux1 = n1;
    n1 = n2;
    n2 = aux1;
    
    printf("A:%d, B: %d", n1, n2);

}
