#include <stdio.h>
#include <string.h>

int main()
{
    int n1, n2;
    printf("Ingrese el primer valor: \n");
    scanf("%d", &n1);
    printf("Ingrese el segundo valor: \n");
    scanf("%d", &n2);
    if (n1 == n2){
        printf("Los valores ingresados son iguales!");
    } else{
        if(n1 % n2 == 0){
            printf("%d es multiplo de %d.", n1, n2);
            
        }else if (n2 % n1 == 0){
            printf("%d es divisor de %d.", n1, n2);
        }else{
            printf("Ninguno es divisor o multiplo del otro!");
        }
        
    }
}
