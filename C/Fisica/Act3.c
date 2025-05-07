#include <stdio.h>
#include <math.h>
#include <ctype.h>

/*PROYECTO: LONGITUD DE UN CAMINO

Vamos a medir la longitud de un camino usando alguna de las métricas que hemos usado en la tarea anterior: la distancia taxi, la distancia euclídea o la distancia del máximo.

DESCRIPCIÓN DE LA ACTIVIDAD
En esta actividad trabajaremos en dimensión n=2. El programa pide al usuario las unidades de medida usadas, que pueden ser metros, kilómetros o millas, así como la distancia que se va a utilizar para medir la longitud del camino. La distancia puede ser: distancia taxi, distancia euclídea o distancia del máximo. Finalmente, el programa pide las coordenadas de los puntos de un camino. No admitiremos que un nuevo punto del camino esté en la recta que une los dos puntos anteriores del camino. El final del camino se indica con el punto (0, 0) y este punto no pertenece al camino
El resultado es la longitud del camino calculada con la distancia elegida y expresada en metros.
Para ello, diseña y programa en C/C++ un algoritmo que haga las siguientes tareas:
1.	 Solicite al usuario las unidades que va a utilizar. Los valores posibles son:
•	‘k’ o ‘K’ para una distancia en kilómetros
•	‘a’ o ‘A’ para una distancia en millas
•	‘m’ o ‘M’ para una distancia en metros
•	‘z’ para terminar
2.	 Si el usuario elige una opción distinta de ‘k’ o ‘K’ o ‘a’ o ‘A’ o ‘m’ o ‘M’, vuelve a solicitar el dato excepto si el valor introducido es la letra ‘z’ en cuyo caso termina.
3.	 Si no ha terminado, solicita la distancia que va a usar. Los valores posibles son:
•	‘t’ para la distancia taxi
•	‘e’ para la distancia euclídea
•	‘m’ para la distancia del máximo
•	‘z’ para terminar
4.	 Si el usuario elige una opción distinta de ‘t’ o ‘e’ o ‘m’, vuelve a solicitar el dato excepto si el valor introducido es la letra ‘z’ en cuyo caso el programa termina.
5.	 Si el programa no ha terminado, pide al usuario que introduzca las coordenadas de cada punto y, a continuación, calcula la distancia entre cada dos puntos y acumula ese valor a la longitud del camino. A partir del tercer punto del camino, no se permite que el nuevo punto esté en la recta que une los dos puntos anteriores. Si esto sucede, el programa debe pedir un nuevo punto.
6.	 El programa finaliza cuando el usuario introduce el punto (0, 0). Este punto NO pertenece al camino. A continuación, muestra la longitud del camino.
*/

// Prototipos
float distancia_taxi(float x1, float y1, float x2, float y2);
float distancia_euclidea(float x1, float y1, float x2, float y2);
float distancia_maximo(float x1, float y1, float x2, float y2);
int estan_alineados(float x1, float y1, float x2, float y2, float x3, float y3);

/// Main
int main() {
    char unidades, metrica;
    float factor = 1.0; // Para convertir a metros
    float x_ant = 0, y_ant = 0, x_act = 0, y_act = 0, x_sig = 0, y_sig = 0; // almacenar las coordenadas de los puntos
    float longitud = 0.0, d = 0.0; // almacenar la longitud del camino y la distancia entre los puntos
    int puntos = 0; // para contar el numero de puntos

    printf("Calculadora de longitudes de caminos\n");
    while (1) {
        printf("Dame las unidades: ");
        printf("k: kilometros\n");
        printf("a: millas\n");
        printf("m: metros\n");
        printf("z: terminar\n");
        scanf(" %c", &unidades);
        unidades = tolower(unidades);
        if (unidades == 'z') {
            printf("Programa terminado\n");
            return 0;
        }
        if (unidades != 'k' && unidades != 'a' && unidades != 'm') {
            printf("Opcion no valida\n");
            continue;
        }
        break;
    }
    fflush(stdin);
    if (unidades == 'k') factor = 1000.0;
    else if (unidades == 'a') factor = 1609.0;
    else factor = 1.0;

    while (1) {
        printf("Dame la métrica: ");
        printf("t: distancia taxi\n");
        printf("e: distancia euclidea\n");
        printf("m: distancia del maximo\n");
        printf("z: terminar\n");
        scanf(" %c", &metrica);
        metrica = tolower(metrica);
        if (metrica == 'z') {
            printf("Programa terminado\n");
            return 0;
        }
        if (metrica != 't' && metrica != 'e' && metrica != 'm') {
            printf("Opcion no valida\n");
            continue;
        }
        break;
    }
    fflush(stdin);

    // Primer punto
    printf("Dame el primer punto: ");
    scanf("%f %f", &x_ant, &y_ant);
    fflush(stdin);
    if (x_ant == 0 && y_ant == 0) {
        printf("Programa terminado\n");
        return 0;
    }
    puntos = 1;

    // Segundo punto
    printf("Dame el segundo punto: ");  
    scanf("%f %f", &x_act, &y_act);
    fflush(stdin);
    if (x_act == 0 && y_act == 0) {
        printf("Programa terminado\n");
        return 0;
    }
    puntos = 2;

    // Calcular distancia entre primer y segundo punto
    switch (metrica) {
        case 't': d = distancia_taxi(x_ant, y_ant, x_act, y_act); break;
        case 'e': d = distancia_euclidea(x_ant, y_ant, x_act, y_act); break;
        case 'm': d = distancia_maximo(x_ant, y_ant, x_act, y_act); break;
    }
    longitud += d * factor;

    // Siguientes puntos
    while (1) {
        printf("Dame el siguiente punto: ");
        scanf("%f %f", &x_sig, &y_sig);
        fflush(stdin);
        if (x_sig == 0 && y_sig == 0) {
            break;
        }
        // Verificar alineación a partir del tercer punto
        if (puntos >= 2 && estan_alineados(x_ant, y_ant, x_act, y_act, x_sig, y_sig)) {
            printf("El punto esta alineado con los dos anteriores, introduce otro punto.\n");
            continue;
        }
        // Calcular distancia y acumular
        switch (metrica) {
            case 't': d = distancia_taxi(x_act, y_act, x_sig, y_sig); break;
            case 'e': d = distancia_euclidea(x_act, y_act, x_sig, y_sig); break;
            case 'm': d = distancia_maximo(x_act, y_act, x_sig, y_sig); break;
        }
        longitud += d * factor;
        // Actualizar puntos
        x_ant = x_act;
        y_ant = y_act;
        x_act = x_sig;
        y_act = y_sig;
        puntos++;
    }
    printf("La longitud es %.0f metros.\n", longitud);
    return 0;
}

float distancia_taxi(float x1, float y1, float x2, float y2) {
    return fabs(x1 - x2) + fabs(y1 - y2);
}

float distancia_euclidea(float x1, float y1, float x2, float y2) {
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

float distancia_maximo(float x1, float y1, float x2, float y2) {
    float dx = fabs(x1 - x2);
    float dy = fabs(y1 - y2);
    return dx > dy ? dx : dy; //devuelve el maximo de los dos valores (dx o dy) mediante un operador ternario
}

// Devuelve 1 si están alineados, 0 si no
int estan_alineados(float x1, float y1, float x2, float y2, float x3, float y3) {
    float det = (x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2); //determinante
    return fabs(det) < 1e-6; //si el determinante es menor que 1e-6, los puntos estan alineados (1e-6 es una tolerancia)
}