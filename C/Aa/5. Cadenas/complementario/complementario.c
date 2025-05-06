#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    int i,cif;
    char diccionario[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char palabra[50];

    printf("Ingrese su texto:\n");
    gets(palabra);
    printf("Ingrese la cantidad de numeros por el cual adelantar:\n");
    scanf("%i", &cif);

    while(palabra[i]){
        palabra[i]= diccionario[i+cif];
        i++;
    }
    printf("%s\n", palabra);
}
