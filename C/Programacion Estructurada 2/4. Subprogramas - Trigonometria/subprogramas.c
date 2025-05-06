#include <stdio.h>
#include <math.h> // sqrt, pow

/*1. Conformar grupos de hasta 3 integrantes como máximo.
2. Diseñar un programa que permita calcular la superficie y perímetro de figuras
geométricas como:
a) Rectángulo
b) Circulo
c) Triangulo
3. Para cada tipo de calculo deveras definir la función correspondiente.*/

// prototipos de funciones
void calcularRectangulo(int base, int altura, float *area, float *perimetro);
void calcularCirculo(int radio, float *area, float *perimetro);
void calcularTriangulo(int base, int altura, float *area, float *perimetro);

int x, y;
int main(void)
{
    int i; // auxiliares
    float area, perimetro;

    printf("Ingrese la figura que desea calcular (1-Rectangulo, 2-Circulo, 3-Triangulo):\n");
    scanf("%d", &i);

    switch (i){
    case 1:
        printf("Ingrese la base y la altura del rectangulo: \n");
        scanf("%d %d", &x, &y);
        calcularRectangulo(x, y, &area, &perimetro);
        break;
    case 2:
        printf("Ingrese el radio del circulo: \n");
        scanf("%d", &x);
        calcularCirculo(x, &area, &perimetro);
        break;
    case 3:
        printf("Ingrese la base y la altura del triangulo: \n");
        scanf("%d %d", &x, &y);
        calcularTriangulo(x, y, &area, &perimetro);
        break;
    default:
        printf("Opcion no valida.");
        return 1;
    }

    printf("El area es: %.2f y el perimetro es: %.2f", area, perimetro);
}

// definiciones de funciones
void calcularRectangulo(int base, int altura, float *area, float *perimetro)
{
    *area = base * altura;
    *perimetro = 2 * (base + altura);
}

void calcularCirculo(int radio, float *area, float *perimetro)
{
    *area = 3.14 * pow(radio, 2);
    *perimetro = 2 * 3.14 * radio;
}

void calcularTriangulo(int base, int altura, float *area, float *perimetro)
{
    *area = (base * altura) / 2;
    *perimetro = base + altura + sqrt(pow(base, 2) + pow(altura, 2));
}
