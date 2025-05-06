#include <stdio.h>
#include <stdlib.h>

int main(void){
    int matriz[8] = {0,0,0,0,0,0,0,0}; // Vector de tamaño 8 inicializada con 0
    int i=7, num, aux; // i=7 porque mi condicion es hasta que i sea 0

    printf("Ingrese el numero que quiere convertir a Binario:\n");
    scanf("%i", &num);

    while(i >= 0){
        aux = num%2; // El resto de la division es guardada en aux
        num= num/2; // La division es hecha y guardada para ser dividida en la proxima iteración
        matriz[i] = aux; // El Vector está programado para alojar de atras para adelante, comenzando por el espacio 7 hasta llegar al 0
        i--; 
    }

    for (i=0;i<8;i++){
        printf("%i", matriz[i]); // Muestra los valores de adelante para atras en suseción, sin \n
    }
    
}
