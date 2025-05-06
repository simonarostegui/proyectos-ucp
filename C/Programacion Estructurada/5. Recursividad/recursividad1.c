#include <stdio.h>

// Suma de dos números: Si ninguno de los dos números es igual a cero las suma de ambos se puede expresar de la siguiente manera:
// Suma=1+suma(a,(b-1))

int sumaRec(int x,int y);

int main(void)
{
    int n, m;

    printf("Ingrese un numero.\n");
    scanf("%i", &n);
    printf("Ingrese otro numero por el cual sumar.\n");
    scanf("%i", &m);
    printf("Sumar %i + %i es igual a decir:\n", n, m);
    sumaRec(n, m);

}

int sumaRec(int x,int y){
    if (y > 1)
    {
        x = 1+sumaRec(x, y-1);
        printf("%i + 1 = %i\n", x, x+1);
        return x;
    }else
    {
        printf("%i + 1 = %i\n", x, x+1);
        return x;
    }
    
    
}