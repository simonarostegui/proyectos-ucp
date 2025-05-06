#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, num, aux, total;

    printf("Ingrese el numero:\n");
    scanf("%i", &num);

    aux=num;
    total = num;
    for (i=0;i<aux-1;i++)
    {
        num--;
        total = total * num;
    }
    printf("Factorial: %i", total);
}
