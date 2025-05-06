#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*Elaborar un algoritmo que permita:

Crear un arreglo de enteros de 5X5
Cargar valores enteros comprendidos entre 0 y 100. Utilizar la función RAND
Mostrar por pantalla el resultado de la suma de los valores por fila
Ahora vamos a considerar que los datos cargados en la tabla representan las ventas semanales (Lunes a Viernes) de los 5 vendedores de una empresa. Sabiendo que el precio unitario del producto vendido es de $1500, se pide que el sistema calcule e informe:

Monto total vendido en la semana por vendedor
Monto total general vendido en la semana
Si cada vendedor recibe un premio que representa el 10% del monto total vendido en la semana, siempre que las ventas superen las 30 unidades.  Se pide informar quienes superaron esa cantidad y que monto de premio recibieron.
Promedio de ventas semanal por vendedor*/

int main(){
    srand(time(NULL));

    int matriz[5][5] = {0};
    int i, j, k, l, x = 0, isRepeating = 1;

    for (i = 0; i < 5; i++){
        for (j = 0; j < 5; j++){
            matriz[i][j] = rand()%101;
        }
    }

    while (isRepeating){
        x = 0;
        for (i = 0; i < 5; i++){
            for (j = 0; j < 5; j++){
                for (k = 0; k < i; k++){
                    for (l = 0; l < j; l++){
                        if (matriz[i][j] == matriz[i][l] || matriz[i][j] == matriz[k][l] || matriz[i][j] == matriz[k][j]){
                            printf("Hubo un cambio en %i %i\n", i, j);
                            matriz[i][j] = rand()%101;
                            x++;
                        }                    
                    }
                }
            }
        }

        if (x == 0){
            isRepeating = 0;
        }
        
        
    }

    for (i = 0; i < 5; i++){
        printf("| ");
        for (j = 0; j < 5; j++){
            printf("%i | ", matriz[i][j]);
        }
        printf("\n");
    }
    
}
