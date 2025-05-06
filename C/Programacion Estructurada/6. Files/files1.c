#include <stdio.h>
// Numeros Divisibles
FILE * divFile; // Variable divFile global.

int divisible(int x, int y); // Prototipo

int main(void)
{
    int i;
    divFile = fopen("C:\\Users\\simon\\OneDrive\\Escritorio\\divisores.txt", "w"); // Abre o crea un archivo utilizando variable global divFile a MI escritorio. Cambiar la dirección a SU escritorio.
    printf("Ingrese un numero por el cual determinar sus divisores.\n");
    scanf("%i", &i);
    divisible(i, i-1);
    fclose(divFile); // Cerrar divFile.
}

int divisible(int x, int y){ // Recursividad
    if (y > 0)
    {
        if (x%y == 0)
        {
            fprintf(divFile, "%i es divisible por %i\n", x, y); // Ingresa el texto.
        }
        return divisible(x, y-1);
        
    }else
    {
        return 0;
    }
    
    
}