#include <stdio.h>

/*Se necesita almacenar los kg diarios vendidos de un producto durante la primera
quincena del mes. Para ello deberá:
a. Crear un vector para almacenar la cantidad vendida por día en la primera
quincena.
b. Para la carga del vector deberá utilizar una variable de tipo puntero que
permita, leer los datos ingresados y guardarlos en el vector.
c. Mostrar el vector cargado utilizando la misma variable puntero creada*/

int main(void) {
    float ventas[15];
    float *ptr = ventas;
    
    // Carga del vector
    for (int i = 0; i < 15; i++) {
        printf("Ingrese cantidad para el día %d: ", i + 1);
        scanf("%f", ptr + i);
    }
    
    // Mostrar el vector cargado
    printf("\nCantidades vendidas por día:\n");
    for (int i = 0; i < 15; i++) {
        printf("Día %d: %.2f kg\n", i + 1, *(ptr + i));
    }
    
    return 0;
}