#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i=0, n1, n2, aux=0, resta;

    while(i< 1){
        printf("Ingrese un diviendo:\n");
        scanf("%i", &n1);
        printf("Ingrese un divisor:\n");
        scanf("%i", &n2);
        if(n1 >= n2){
            i++;
        }else{
            printf("Su divisor no puede ser mayor al dividendo.\nIntente nuevamente.\n\n");
        }
    }

    printf("%i/%i=\n\n", n1, n2);
    while (resta>0){
        if((n1-n2)<0){
            break;
        }
        aux++;
        resta = n1 - n2;
        printf("%i. %i - %i = %i\n", aux, n1, n2, resta);
        n1 = resta;
    }
    printf("Resultado %i, Resto %i", aux, resta);
}
