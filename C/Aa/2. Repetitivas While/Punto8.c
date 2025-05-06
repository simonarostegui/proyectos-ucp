#include <stdio.h>
#include <stdlib.h>

int main(){
    int i=0, sueldo, sexo, hombres = 0, mujeres = 0, totalMujeres=0, totalHombres=0, sueldoMayorHombres=0, sueldoMenorHombres=0, sueldoMayorMujeres=0, sueldoMenorMujeres=0;

    /*Decidí automatizar los legajos para facilitar el testeo del codigo en lugar de hacerlo correr 10 veces.*/

    while(i<10){
        sexo = rand()%2+1;
        if(sexo ==1){
            mujeres++;
        }else{
            hombres++;
        }
        sueldo = (rand() %(200000 - 75000 +1)) + 75000;

        if(sexo==1){
            if(sueldoMenorMujeres>sueldo || sueldoMenorMujeres == 0){
                sueldoMenorMujeres = sueldo;
            } else if (sueldoMayorMujeres<sueldo){
                sueldoMayorMujeres = sueldo;
            }
            totalMujeres = totalMujeres+sueldo;
        }else{
            if(sueldoMenorHombres>sueldo || sueldoMenorHombres == 0){
                sueldoMenorHombres = sueldo;
            } else if (sueldoMayorHombres<sueldo){
                sueldoMayorHombres = sueldo;
            }
            totalHombres = totalHombres + sueldo;
        }
        i++;
    }

    printf("Total Hombres: %i\nTotal de Sueldo: $%i\nTotal Mujeres: %i\nTotal de Sueldo: $%i\n", hombres, totalHombres, mujeres ,totalMujeres);
    printf("Sueldo Mayor de los Hombres: $%i\nSueldo Menor de los Hombres: $%i\n", sueldoMayorHombres, sueldoMenorHombres);  
    printf("Sueldo Mayor de las Mujeres: $%i\nSueldo Menor de las Mujeres: $%i\n", sueldoMayorMujeres, sueldoMenorMujeres);
  

}
