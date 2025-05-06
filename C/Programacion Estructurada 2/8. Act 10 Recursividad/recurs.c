#include <stdio.h>
//Arostegui Simon


/*Suma de dos números: Si ninguno de los dos números es igual a cero las suma de
ambos se puede expresar de la siguiente manera:
Suma=1+suma(a,(b-1))
Por ejemplo:
Dados a=3 y b=4
La suma de 3+4, es igual a sumar 1+(3+3)
A su vez, sumar 3+3 es igual a 1+(3+2)*/

int suma(int a, int b);

int main(void)
{
    printf("%i", suma(3, 4));
}

int suma(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return 1 + suma(a, b - 1);
    }
}