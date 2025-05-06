#include <stdio.h>
// Numeros Divisibles

int divisible(int x, int y);

int main(void)
{
    int i;
    printf("Ingrese un numero por el cual determinar sus divisores.\n");
    scanf("%i", &i);
    divisible(i, i-1);
}

int divisible(int x, int y){
    if (y > 0)
    {
        if (x%y == 0)
        {
            printf("%i es divisible por %i\n", x, y);
        }
        return divisible(x, y-1);
        
    }else
    {
        return 0;
    }
    
    
}