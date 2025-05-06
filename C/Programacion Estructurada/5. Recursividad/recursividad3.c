#include <stdio.h>

//Decimal a Binario

void aBinario(int x);

int main(void)
{
    int i;
    printf("Ingrese un numero el cual convertir a binario.\n");
    scanf("%i", &i);
    aBinario(i);
}

void aBinario(int x){
    if (x > 1)
    {
        aBinario(x/2);
        printf("%i", x%2);
    }else
    {
        printf("1");
    }
    
    
}