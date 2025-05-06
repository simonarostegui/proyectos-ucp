#include <stdio.h>

/*Desarrolle un algoritmo que a partir de dos valores cualquiera ‘n1’ y ‘n2’ positivos,
ingresados por teclado, permita realizar las siguientes operaciones matemáticas:
a) Suma
b) Resta
c) Multiplicación
d) División
Tener en cuenta que previamente deberá verificar si los valores ingresados son positivos. */

int suma(int A, int B){
    int rpta = A + B;
    return rpta;
}

int resta(int A, int B){
    int rpta = A - B;
    return rpta;
}

int multiplicacion(int A, int B){
    int rpta = A * B;
    return rpta;
}

int division(int A, int B){
    int rpta = A / B;
    return rpta;
}

int main(void){
    int i =0, n1, n2;
    while(i<1){
        printf("Ingrese el primer numero:\n");
        scanf("%i", &n1);
        printf("Ingrese el segundo numero:\n");
        scanf("%i", &n2);
        if(n1 < 0 || n2 < 0){
            printf("Su numero no puede ser menor a 0.\n");
        }else{
            i++;
        }
    }

    int w = suma(n1, n2);
    int x = resta(n1, n2);
    int y = multiplicacion(n1,n2);
    int z = division(n1, n2);

    printf("La suma entre %i y %i es: %i\nLa resta entre %i y %i es: %i\nLa multiplicacion entre %i y %i es: %i\nLa division entre %i y %i es: %i\n", n1, n2, w, n1, n2, x, n1, n2, y, n1, n2, z);

}
