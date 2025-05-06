#include <stdio.h>

int main()
{
    int aumento, salario, nuevoSalario, aux1;

    printf("Ingrese su salario:\n");
    scanf("%d", &salario);
    if(salario >900){
        if(salario >1500){
            if(salario >2000){
                aumento = 2;
            }else
            {
                aumento = 5;
            }
        }else
        {
            aumento = 10;
        }
    }else{
        aumento = 20;
    }
    aux1 = (aumento * salario) / 100;
    nuevoSalario = salario + aux1;
    printf("Su nuevo salario es $%d, felicidades.", nuevoSalario);
}
