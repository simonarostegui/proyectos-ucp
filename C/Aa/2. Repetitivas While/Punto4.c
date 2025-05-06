#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int i=0, confirmar=0, total=0, listaTotal=0;
    char producto[10][30];
    int cantidad[30], precio[30];

    while(confirmar!=1){
        printf("Ingrese el producto que desea facturar:\n");
        scanf("%s", producto[listaTotal]);
        printf("Ingrese la cantidad de su producto:\n");
        scanf("%i", &cantidad[listaTotal]);
        printf("Ingrese el precio de su producto:\n");
        scanf("%i", &precio[listaTotal]);
        printf("Desea generar su factura? 1 = Si.\n");
        scanf("%i", &confirmar);
        listaTotal++;
    }   

    while(i<listaTotal){
        printf("\n%i. %s x %i ($%i c/u)", i+1, producto[i], cantidad[i], precio[i]);
        total = total + precio[i] * cantidad[i];
        i++;
    }
    printf("\nTotal: $%i", total);
}
