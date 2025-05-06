#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i, num, total, promedio;

    for (i=0;i<20;i++)
    {
        printf("Ingrese el Numero %i:\n", i+1);
        scanf("%i", &num);
        total = total + num;
    }
    promedio = total / i;
    printf("Promedio: %i", promedio);
    
}
