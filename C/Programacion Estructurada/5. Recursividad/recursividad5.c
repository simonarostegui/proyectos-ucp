#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Recursión en estructura de Arreglos 

int sumArr(int x[], int y);

int mulArr(int x[], int y);

int parArr(int x[], int y);

int main(void)
{
    srand(time(NULL));
    int arreglo[30];
    int i, j;
    

    for (i = 0; i < 30; i++)
    {
        arreglo[i] = rand()%100;
        printf("%i\n", arreglo[i]);
    }
    printf("\n");
    j = sizeof(arreglo) / sizeof(arreglo[0]);
    printf("La suma de los elementos es: %d\n", sumArr(arreglo, j));
    printf("La cantidad de elementos multiplos de 3 es: %d\n", mulArr(arreglo, j));
    printf("La cantidad de elementos pares en posiciones impares es: %d\n", parArr(arreglo,j));
}






int sumArr(int x[], int y){
    if (y == 0) {
        return 0;
    }
    return x[y-1] + sumArr(x, y-1);
}

int mulArr(int x[], int y){
    if (y == 0) {
        return 0;
    }
    if (x[y-1] % 3 == 0) {
        return 1 + mulArr(x, y-1);
    } else {
        return mulArr(x, y-1);
    }
}

int parArr(int x[], int y){
    if (y <= 1) {
        return 0;
    } 
    if (x[y-2] % 2 == 0) {
        return 1 + parArr(x, y-2);
    } else {
        return parArr(x, y-2);
    }
}
