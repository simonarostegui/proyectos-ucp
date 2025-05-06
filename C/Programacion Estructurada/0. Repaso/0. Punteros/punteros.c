#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int enteros[50] = {0};
    int i, k, v, x, y =0;

    srand(time(NULL));

    for (k = 0; k < 50; k++){
        int isRepeating;
        while (isRepeating){
            isRepeating = 0;
            i = rand()%101;
            for (v = 0; v < k; v++){
                if (enteros[v] == i){
                    isRepeating = 1;
                    break;
                }
             
            
            }
        }
        enteros[k] = i;
        
        
        printf("%i. %i\n",k, enteros[k]); //Genera los numeros en posicion i dentro del arreglo.
    }


    
    printf("Ingrese un numero para buscar en la matriz.\n");
    scanf("%i", &x); //Guarda el valor ingresado en x

    for (i = 0; i < 50; i++){
        if (enteros[i] == x){ // Si el numero dentro de la posicion i dentro del arreglo 'enteros' es igual a la variable x, muestra el siguiente mensaje
            printf("El numero %i se encuentra en la posicion %i\n",x, i);
            y++; //Acumula la cantidad de veces que aparece x dentro de y
        }
    }
    
    
    if(y!=0){
        printf("El numero %i se encuentra en la lista %i veces.\n", x, y); // Si la variable y no es cero, es decir, x aparece mas de una vez, corre el siguiente mensaje. 
    }else{
        printf("Su numero no se encuentra en la matríz.\n"); 
    }

}
