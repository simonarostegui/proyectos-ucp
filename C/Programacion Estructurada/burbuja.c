#include <stdio.h>

int main(void)
{
    
    int arreglo[5] = {5,3,4,1,2};
    int i = 0, ordenado = 1, max = 4, aux, cambiado;
    while (ordenado){ // Mantiene mi while corriendo y ordenando.
        if (i == 0) // Cada vez que se reinicie el i, cambiado es 0
        {
            cambiado = 0;
        }
        
        if (i != max){ // Si mi i no es 5 (Fuera de limites)
            if (arreglo[i] > arreglo[i+1]) // Si lugar x es mayor a lugar x+1 (Ej 0 mayor a 1)
            {
                aux = arreglo[i+1]; // Guarda 1 en aux
                arreglo[i+1] = arreglo[i]; // Mueve valor de 0 a la posicion 1
                arreglo[i] = aux; // Guarda valor de aux en posicion 0
                cambiado = 1; // Cambia 'cambiado' a 1 cada vez que hay cambio durante la iteracion de i
                i++; // Contador ++
                printf("Hubo Cambio\n");
            }else
            {
                printf("No Hubo Cambio\n");
                i++; // Si no hay cambio, Contador++
            }
            
        }else if (i == max && cambiado == 0) // Si estamos al final de la iteracion de i y no hubo cambios
        {
            ordenado =0; // Rompemos el bucle
        }else
        {
            i = 0; // Si estamos al final de la iteracion de i y hubo cambios volvemos al principio.
        }
        
    }
    
    for (i = 0; i < 5; i++) // Mostramos todo.
    {
        printf("%i ", arreglo[i]);
    }
    
}
