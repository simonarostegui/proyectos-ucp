#include <stdio.h>
#include <stdlib.h>

int main(){
    int i=1, promedio, aux, auxI, aux2, auxI2, randaux, suma=0;
    
    while (i<=30){
        randaux = rand()%100;

        if(aux < randaux){
            aux = randaux;
            auxI = i;
        }
        if(aux2 > randaux){
            aux2 = randaux;
            auxI2 = i;
        }
        suma = suma +randaux;
        printf("Dia %i. %imm\n", i, randaux);
        i++;
    }
    promedio = suma /i;
    printf("El dia de mayor lluvia fue el %i con %imm.\n", auxI, aux);
    printf("El dia de menor lluvia fue el %i con %imm.\n", auxI2, aux2); 
    printf("El promedio de precipitacion es %imm.", promedio);
}
