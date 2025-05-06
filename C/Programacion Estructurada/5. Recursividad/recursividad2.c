#include <stdio.h>

// Secuencia Fibonacci

int fib(int x, int y, int z);

int main(void)
{
    int i;
    printf("Ingrese la cantidad de veces que desea se ejecute la secuencia fibonacci.\n");
    scanf("%i", &i);
    fib(1, 1, i);
    
}

int fib(int x, int y, int z){
    if (z > 0)
    {
        printf("%i ", x);
        return fib(y, x+y, z-1);
    }
    else
    {
        return 0;  
    }
}
