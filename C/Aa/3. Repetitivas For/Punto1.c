#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i, num, numMayor=0, numMenor=0;

    for (i=0;i<15;i++){
        printf("Ingrese el numero %i:\n", i+1);
        scanf("%i", &num);

        if(num>numMayor){
            numMayor = num;
        }
        if(num<numMenor || numMenor == 0){
            numMenor = num;
        }
        
    }

    /*int randNum;
    for (i=0;i<15;i++){
        randNum = rand()%101;
        printf("%i\n",randNum);

        if(randNum>numMayor){
            numMayor = randNum;
        }else if(randNum<numMenor || numMenor == 0){
            numMenor = randNum;
        }
    }*/
    
    printf("Numero Mayor: %i\nNumero Menor: %i", numMayor, numMenor);
}
