#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,numero, size=0, suma=0, promedio, aux=0;

    printf("Valores Generados:\n");

    /*for (i=0;i<50; i++){
        numero = rand()%101;
        printf("%i\n",numero);
        if(numero>=50){
            size++;
            aux = aux+numero;
        } else{
            suma = suma +numero;
        }
    } */

    while (i<=50){
        numero = rand()%101;
        printf("%i\n",numero);
        if(numero>=50){
            size++;
            aux = aux+numero;
        } else{
            suma = suma +numero;
        }
        i++;
    }
    
    
    promedio = aux/size;
    printf("\nPromedio de los valores mayores a 50: %i\nSuma de los valores menores a 50: %i", promedio, suma);

}
