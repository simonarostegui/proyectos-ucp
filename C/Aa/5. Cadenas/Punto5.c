#include <stdio.h>
#include <string.h>

int main(void){
    int i, cantidad=0;
    char palabra[50];
    char letra; // Un solo caracter no necesita ser array.
    
    printf("Ingrese una texto:\n");
    gets(palabra);

    printf("Ingrese la letra que desea contar:\n");
    scanf("%c", &letra);
    
    while(palabra[i]){
        if(letra == palabra[i]){ // Casi me rompo la cabeza con este codigo hasta que me di cuenta que no inicialicé la var cantidad.
            cantidad++;
        }
        i++;
    }
    printf("La letra %c se encuentra %i veces en el texto: %s", letra, cantidad, palabra);
}
