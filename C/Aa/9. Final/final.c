#include <stdio.h>
#include <stdlib.h>

int main(){
    int empleadosHoras[10];
    int i, x, y = 0;

    for (i = 0; i < 10; i++)
    {
        empleadosHoras[i] = rand()%41; 
        
    }

    for ( i = 0; i < 10; i++)
    {
        x = empleadosHoras[i] * 1250; 
        y = y + x; 
        printf("Empleado %i: Horas Trabajadas: %i, Saldo a Pagar: $%i\n", i+1, empleadosHoras[i], x); 
    }
     printf("\nEn Total: $%i", y);
}
