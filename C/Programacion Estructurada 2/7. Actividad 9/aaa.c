#include <stdio.h>

int xT(int b, int e){
    if(e==0){
        return 1;
    }else
    {
        return b*xT(b,e-1);
    }
    
}

int main(void)
{
    int x, y;
    printf("Ingrese la base: ");
    scanf("%i",&x);
    printf("Ingrese el exponente: ");
    scanf("%i",&y);
    printf("El resultado es %i", xT(x,y));
}