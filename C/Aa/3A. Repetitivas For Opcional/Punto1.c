#include <stdio.h>
#include <string.h>

int main()
{
    float valor;
    int aux1;

    aux1 = 0;
    while(aux1 == 0){ //Bucle por si el usuario ingresa nota menor a 0 o mayor a 10
    printf("Ingrese su promedio:\n");
    scanf("%f", &valor);
    if(valor < 0){
        printf("Tu promedio no puede ser menor a 0!\n");
    }else if (valor > 10)
    {
        printf("Tu promedio no puede ser mayor a 10!\n");
    }else
    {
        aux1=1; // Que rompa el bucle
    }
    }

    if (valor > 3.5){
        if (valor > 5){
            if(valor > 6){
                if(valor > 7){
                    if(valor > 8.5){
                        printf("Sobresaliente!"); 
                    }else
                    {
                        printf("Notable!");
                    }
                }else{
                    printf("Bien!");
                }
            }else{
                printf("Suficiente!");
            }
        }else{
            printf("Insuficiente!");
        }
    }else{
        printf("Muy deficiente,");
    }    
}
