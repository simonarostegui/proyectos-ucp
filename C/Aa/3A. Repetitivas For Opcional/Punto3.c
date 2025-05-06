#include <stdio.h>
#include <string.h>

int main(){
    char dia[30], domingo[] = "Domingo";
    int incremento, horas, horaComienzo, salario, aux1;

    incremento = 0;
    printf("Ingrese el dia que usted trabaja:\n");
    scanf("%s", &dia);
    printf("En formato 24hs, ingrese la hora de comienzo de su jornada:\n");
    scanf("%d", &horaComienzo);
    printf("Ingrese la cantidad de horas trabajadas:\n");
    scanf("%d", &horas);

    aux1 = strcmp(dia, domingo);
    if (aux1 == 0){    
        if(horaComienzo >= 18 || horaComienzo <= 6){
            incremento = 600;}
        else{
            incremento = 400;}
    }

    if(horaComienzo >= 18 || horaComienzo <= 6){
        salario = 1600;} 
    else{
        salario = 1000;
    }

    printf("Su nuevo salario es $%d por hora.\nTotal por hora trabajada: $%d", salario+incremento, horas*(salario+incremento));

}
