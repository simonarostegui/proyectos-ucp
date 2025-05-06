#include <stdio.h>
#include <string.h>
int main()
{
    int n1, n2, operador, valorResultado, moduloDiv;
    valorResultado = 0;
    moduloDiv = 0;
    printf("Ingrese 2 numeros: \n");
    scanf("%d %d", &n1, &n2);
    printf("Ingrese su operacion deseada \nValores reconocidos: \n1 = Suma\n2 = Resta\n3 = Multiplicacion\n4 = Division\n");
    scanf("%d", &operador);
    switch (operador){
    case 1:
        /*Caso Suma*/
        valorResultado = n1 + n2;
        printf("La suma entre %d y %d es %d", n1, n2, valorResultado);
        break;
    case 2:
        /*Caso Resta*/
        valorResultado = n1 - n2;
        printf("La resta entre %d y %d es %d", n1, n2, valorResultado);
        break;
    case 3:
        /*Caso Multiplicacion*/
        valorResultado = n1 * n2;
        printf("La multiplicacion entre %d y %d es %d", n1, n2, valorResultado);
        break;
    case 4:
        /*Caso Division*/
        valorResultado = n1 / n2;
        moduloDiv = n1 % n2;
        /*Si el resto es mayor a 0 da con resto*/
        if (moduloDiv > 0){
            printf("La division entre %d y %d es %d y su resto es %d", n1, n2, valorResultado, moduloDiv);
        } else{
            printf("La division entre %d y %d es %d", n1, n2, valorResultado);
        }
        break;
    default:
        printf("Su operador no es reconocido!");
        break;
    }
}
