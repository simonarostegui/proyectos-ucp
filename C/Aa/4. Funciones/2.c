#include <stdio.h>
#include <ctype.h> // para el tolower
#include <string.h> // para el strcmp

/*Desarrolle un algoritmo que permita calcular el área y el perímetro de una figura geométrica
(circulo-rectángulo). El usuario podrá elegir la figura y el cálculo.*/

double areaCirculo(double distancia){
    double radio = distancia / 2;
    return 3.14*(radio*radio);
}

double perimetroCirculo(double distancia){
    double radio = distancia / 2;
    return 2 * 3.14 * radio;
}

double areaRect(double base, double altura){
    return base * altura;
}

double perimetroRect(double base, double altura){
    return 2*(base+altura);
}

int main(void)
{
    int i, figuraRect, figuraCirculo;
    char tipo[20], circulo[] = "circulo", rectangulo[] = "rectangulo"; // strcmp necesita un string con el cual comparar
    double n1, n2;

    printf("Ingrese el tipo de formula que desea (Circulo o Rectangulo):\n"); 
    scanf("%s", tipo); 
    // El unico problema con esto es que si pone un numero, el codigo se rompe.

    while (tipo[i]){
        tipo[i] = tolower(tipo[i]);
        i++;
    }
    // Convierte tipo[] a minuscula

    figuraCirculo = strcmp(tipo, circulo);
    figuraRect = strcmp(tipo, rectangulo);
    //Compara los strings y devuelve 0 si es igual

    if (figuraCirculo == 0){
        printf("Ingrese la distancia de su circulo:\n");
        scanf("%le", &n1);
        double x = areaCirculo(n1);
        double y = perimetroCirculo(n1);
        printf("\nEl area de su circulo es: %.2f\nEl perimetro de su circulo es: %.2f\n",x,y);}
    else if (figuraRect==0){
        printf("Ingrese la base de su rectangulo:\n");
        scanf("%le", &n1);
        printf("Ingrese la altura de su rectangulo:\n");
        scanf("%le", &n2);
        double x = areaRect(n1, n2);
        double y = perimetroRect(n1, n2);
        printf("\nEl area de su rectangulo es: %.2f\nEl perimetro de su rectangulo es: %.2f\n",x,y);
    } else{
        printf("Valor ingresado incorrecto!\n");
        //Error por si no es circulo o rectangulo.
    }
    
    
}
