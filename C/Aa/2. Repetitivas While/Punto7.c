#include <stdio.h>
#include <stdlib.h>ñ

int main(){
    int i, n1, n2;
    
    printf("Ingrese el numero que desea sea el menor limite:\n");
    scanf("%i", &n1);
    printf("Ingrese el numero que desea sea el mayor limite:\n");
    scanf("%i", &n2);

    i = n1;
    while(n1<=i && i<=n2){
        printf("\n%i", i);
        i++;
    }
}
