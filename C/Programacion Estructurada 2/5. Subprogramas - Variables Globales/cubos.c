#include <stdio.h>
#include <math.h> // incluyo libreria math.h para usar pow

/*El programa calcula el cubo de los 10 primeros números naturales con la
ayuda de una función. En la solución del problema se utiliza una variable
global, aunque esto, como veremos más adelante, no es muy recomendable*/

int i; // declaro indice como variable global
void cubos();

int main(void){
    cubos();
}

void cubos(){
    for (i = 1; i < 11; i++)
    {
        printf("%i^3 = %.0f\n", i, pow(i, 3)); // hago el calculo dentro del printf usando pow(base, potencia)
    }
}