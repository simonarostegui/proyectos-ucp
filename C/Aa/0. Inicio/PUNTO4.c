#include <stdio.h>
#include <string.h>

int main(){
    int cantidad, descuento;
    float precio, aux1, aux2, preciototal;

    descuento = 15;

    printf("Ingrese el precio de su producto:\n");
    scanf("%f", &precio);
    printf("Ingrese la cantidad de productos en su carro:\n");
    scanf("%i", &cantidad);

    aux1 = precio * cantidad;
    aux2 = (descuento * aux1) / 100; //Regla de 3 Simple para obtener descuento
    preciototal = aux1 - aux2; 

    printf("\nCantidad: %i Unidades.\nPrecio por unidad: $%.2f\nPrecio de lista: $%.2f.\nPrecio con descuento al %d%%: $%.2f", cantidad, precio, aux1, descuento, preciototal);
    //.2f muestra un flotante con un maximo de 2 decimales
}
