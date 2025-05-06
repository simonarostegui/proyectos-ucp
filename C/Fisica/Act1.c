#include <stdio.h>
#include <math.h>
#include <ctype.h>

/*PROYECTO: DISTANCIA ENTRE DOS PUNTOS
Para medir distancias, se han usado varias métricas como la distancia taxi, la distancia euclídea o la distancia del máximo. La forma de calcular cada una de esas distancias en dimensión n >= 2 para los puntos (x1, x2, . . . xn) e (y1, y2, . . . yn) se recoge en la Tabla siguiente.


DESCRIPCIÓN DE LA ACTIVIDAD
En esta actividad trabajaremos en dimensión n=2. El programa pide al usuario las coordenadas de dos puntos, las unidades de medida usadas, que pueden ser metros, kilómetros o millas, así como la distancia que se va a utilizar para medir la distancia entre esos dos puntos. La distancia puede ser: distancia taxi, distancia euclídea o distancia del máximo.
El resultado es la distancia entre los dos puntos calculada con la distancia elegida y expresada en metros.
Para ello, diseña y programa en C/C++ un algoritmo que haga las siguientes tareas:
1.	Solicite al usuario las unidades que va a utilizar. Los valores posibles son:
•	‘k’ o ‘K’ para una distancia en kilómetros
•	‘a’ o ‘A’ para una distancia en millas
•	‘m’ o ‘M’ para una distancia en metros.
2.	Si el usuario elige una opción distinta de ‘k’ o ‘K’ o ‘a’ o ‘A’ o ‘m’ o ‘M’, muestra un mensaje al usuario indicando que no es una opción válida y termina.
3.	 En otro caso, solicita la distancia que va a usar Los valores posibles son:
•	‘t’ para la distancia taxi
•	‘e’ para la distancia euclídea
•	‘m’ para la distancia del máximo
4.	 Si el usuario elige una opción distinta de ‘t’ o ‘e’ o ‘m’, muestra un mensaje al usuario indicando que no es una opción válida y termina.
5.	 En otro caso, pide al usuario que introduzca las coordenadas de dos puntos y, a continuación, calcula la distancia entre esos dos puntos, la convierte a metros y la muestra en pantalla.
Se valorará especialmente que el programa no tenga código repetido.

*/

int main() {
    char unidades = ' ', distancia = ' ';
    float x1, y1, x2, y2, distancia_metros; // fabs, sqrt, pow, fmax usan float

    printf("Introduce las unidades de medida (k, a, m):\n");
    printf("k: kilometros\na: millas\nm: metros\n");
    scanf("%c", &unidades);
    unidades = tolower(unidades);

    if (unidades != 'k' && unidades != 'a' && unidades != 'm') {
        printf("No es una opcion valida");
        return 1;
    }
    fflush(stdin);

    printf("Introduce la distancia que va a usar (t, e, m):\n");
    printf("t: distancia taxi\ne: distancia euclidea\nm: distancia del maximo\n");
    scanf("%c", &distancia);
    distancia = tolower(distancia);
    fflush(stdin);

    if (distancia != 't' && distancia != 'e' && distancia != 'm') {
        printf("No es una opcion valida");
        return 1;
    }

    printf("Introduce las coordenadas del punto 1 (x1, y1): ");
    scanf("%f %f", &x1, &y1);
    fflush(stdin);

    printf("Introduce las coordenadas del punto 2 (x2, y2): ");
    scanf("%f %f", &x2, &y2);
    fflush(stdin);
    
    switch (unidades) {
        case 'k': //kilometros a metros
            x1 *= 1000;
            y1 *= 1000;
            x2 *= 1000;
            y2 *= 1000;
            break;
        case 'a': //millas a metros
            x1 *= 1609.34;
            y1 *= 1609.34;
            x2 *= 1609.34;
            y2 *= 1609.34;
            break;
        case 'm': //metros, no se convierte
            break;
    }  

    switch (distancia) {
        case 't':
            distancia_metros = fabs(x1 - x2) + fabs(y1 - y2); //distancia taxi, suma de las diferencias absolutas de las coordenadas
            break;
        case 'e':
            distancia_metros = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)); //distancia euclidea, raiz de la suma de las diferencias al cuadrado de las coordenadas
            break;
        case 'm':
            distancia_metros = fmax(fabs(x1 - x2), fabs(y1 - y2)); //distancia del maximo, maximo de las diferencias absolutas de las coordenadas
            break;
    }

    printf("La distancia entre los dos puntos es: %i metros\n", (int)distancia_metros); //convierto a int para que no salgan decimales
}
