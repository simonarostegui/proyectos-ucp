#include <stdio.h>
#include <string.h>

int main(){
    
    int n1, n2;
    int aux1, aux2, aux3;

    printf("Ingrese el primer valor:\n");
    scanf("%d", &n1);
    printf("Ingrese el segundo valor:\n");
    scanf("%d", &n2);
    
    aux1 = n1 * n2;
    aux2 = n1 + n2;
    aux3 = aux1 * 2;
    //Spaghetti porque no quiero hacer 50 prints ni un warp
    printf("\nVariables elegidas: %d, %d.\n%d * %d: %d.\n%d + %d: %d\n%d * 2: %d", n1, n2, n1, n2, aux1, n1, n2, aux2, aux2, aux3);
}
