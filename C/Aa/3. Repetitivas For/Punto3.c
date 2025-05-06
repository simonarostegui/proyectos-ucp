#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i, randnum, total, promedio;

    for (i=0;i<20;i++)
    {
        randnum = rand()%201;
        printf("%i\n", randnum);
        total = total + randnum;
    }
    promedio = total / i;
    printf("Promedio: %i", promedio);
    
}
