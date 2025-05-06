#include <stdio.h>

void intercambio(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int x = 10;
    int y = 20;

    printf("Antes del intercambio: x = %d, y = %d\n", x, y);
    intercambio(&x, &y);
    printf("Despues del intercambio: x = %d, y = %d\n", x, y);
}