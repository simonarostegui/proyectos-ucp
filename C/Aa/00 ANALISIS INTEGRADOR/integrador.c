#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

// funcion para evaluar un polinomio dado un valor de x
double evaluar_polinomio(char polinomio[], char x[]) {
    double coeficiente = 0;
    int exponente = 0;
    double resultado = 0;
    int i = 0;
    int signo = 1;
    double x_num = atof(x); // convertir cadena x a numero

    // recorrer el polinomio caracter por caracter
    while (polinomio[i] != '\0') {
        // manejo de signos
        if(polinomio[i] == '-'){
            signo = -1;
            i++;
        }else if(polinomio[i] == '+'){
            signo = 1;
            i++;
        }
        
        // procesar digitos para obtener coeficiente
        if(isdigit(polinomio[i])){
            coeficiente = 0;
            while(isdigit(polinomio[i])){
                coeficiente = coeficiente * 10 + (polinomio[i] - '0');
                i++;
            }
        }
        // procesar terminos con x
        else if(polinomio[i] == 'x'){
            if(coeficiente == 0){
                coeficiente = 1; // coeficiente implicito 1
            }
            i++;
            
            // procesar exponente si existe
            if(polinomio[i] == '^'){
                i++;
                exponente = 0;
                while(isdigit(polinomio[i])){
                    exponente = exponente * 10 + (polinomio[i] - '0');
                    i++;
                }
            } else{
                exponente = 1; // si no hay exponente, se asigna 1
            } 

            // calcular y acumular el termino actual
            resultado += signo * coeficiente * pow(x_num, exponente);
            coeficiente = 0;
            exponente = 0;
        }else{
            i++; // avanzar si no es un digito ni 'x'
        }
    }
    // sumar el ultimo termino constante si existe
    resultado += coeficiente;
    return resultado;
}

// funcion para calcular limites en el infinito
double limiteInfinito(char polinomio[], char polinomio2[]){
    double coeficiente = 0;
    double coeficiente2 = 0;
    int exponente = 0;
    int exponente2 = 0;
    double resultado = 0;
    int i = 0;

    int signo = 1;
    int signo2 = 1;
    int grado = 0;
    double coef_principal = 0;
    int grado2 = 0;
    double coef_principal2 = 0;

    // procesar numerador para encontrar grado y coeficiente principal
    while(polinomio[i] != '\0'){
        // manejo de signos
        if(polinomio[i] == '-'){
            signo = -1;
            i++;
        }else if(polinomio[i] == '+'){
            signo = 1;
            i++;
        }
        
        // leer coeficiente
        coeficiente = 0;
        int digitos_leidos = 0;
        if(isdigit(polinomio[i])){
            while(isdigit(polinomio[i])){
                coeficiente = coeficiente * 10 + (polinomio[i] - '0');
                i++;
                digitos_leidos = 1;
            }
        }
        
        // procesar terminos con x
        exponente = 0;
        if(polinomio[i] == 'x'){
            if(coeficiente == 0) coeficiente = 1;
            coeficiente *= signo;
            i++;
            
            exponente = 1;
            if(polinomio[i] == '^'){
                i++;
                exponente = 0;
                while(isdigit(polinomio[i])){
                    exponente = exponente * 10 + (polinomio[i] - '0');
                    i++;
                }
            }
            
            // actualizar grado y coeficiente principal si es necesario
            if(exponente > grado){
                grado = exponente;
                coef_principal = coeficiente;
            }
        } 
        // procesar termino constante
        else if (digitos_leidos) {
            if (grado == 0) {
                coef_principal = coeficiente * signo;
            }
        } else {
            i++; // avanzar si no hay digitos ni 'x'
        }
    }

    // procesar denominador de manera similar al numerador
    i = 0;
    while(polinomio2[i] != '\0'){
        if(polinomio2[i] == '-'){
            signo2 = -1;
            i++;
        }else if(polinomio2[i] == '+'){
            signo2 = 1;
            i++;
        }
        
        coeficiente2 = 0;
        int digitos_leidos = 0;
        if(isdigit(polinomio2[i])){
            while(isdigit(polinomio2[i])){
                coeficiente2 = coeficiente2 * 10 + (polinomio2[i] - '0');
                i++;
                digitos_leidos = 1;
            }
        }
        
        exponente2 = 0;
        if(polinomio2[i] == 'x'){
            if(coeficiente2 == 0) coeficiente2 = 1;
            coeficiente2 *= signo2;
            i++;
            
            exponente2 = 1;
            if(polinomio2[i] == '^'){
                i++;
                exponente2 = 0;
                while(isdigit(polinomio2[i])){
                    exponente2 = exponente2 * 10 + (polinomio2[i] - '0');
                    i++;
                }
            }
            
            if(exponente2 > grado2){
                grado2 = exponente2;
                coef_principal2 = coeficiente2;
            }
        } else if (digitos_leidos) { // termino constante
            if (grado2 == 0) {
                coef_principal2 = coeficiente2 * signo2;
            }
        } else {
            i++; // avanzar si no hay digitos ni 'x'
        }
    }

    // comparar grados para determinar el limite
    if(grado < grado2) resultado = 0;
    else if(grado > grado2) resultado = INFINITY;
    else resultado = coef_principal / coef_principal2;
    return resultado;
}

// funcion principal para calcular limites
double limite(char funcion[], char x[]){
    char numerador[50], denominador[50] = "1";  // inicializar denominador con "1"
    int i = 0, j = 0;

    // separar numerador y denominador
    while (funcion[i] != '/' && funcion[i] != '\0') {
        numerador[j++] = funcion[i++];
    }
    
    // si no hay denominador, usar 1
    if (funcion[i] != '/') {
        numerador[j] = '\0';
    } else {
        numerador[j] = '\0';
        
        i++;
        j = 0;
        while (funcion[i] != '\0') {
            denominador[j++] = funcion[i++];
        }
        denominador[j] = '\0';
    }

    printf("El numerador es: %s\n", numerador);
    printf("El denominador es: %s\n", denominador);
    // calcular limite segun el valor de x
    if (strcmp(x, "inf") == 0){
        return limiteInfinito(numerador, denominador);
    }else{
        // evaluar numerador y denominador
        double num = evaluar_polinomio(numerador, x);
        double den = evaluar_polinomio(denominador, x);

        // manejar casos especiales
        if (den != 0){
            return num/den;
        }else if (den == 0){
            printf("Error: Division por cero\n");
            return 0;
        }else{
            return num;
        }
    }
}

// funcion principal del programa
int main() {
    char funcion[100];
    char x[10];
    printf("Ingrese una funcion racional: \nEjemplo: (2x^2+3x+1)/(x^3+5)\n\n");
    scanf("%s", funcion);
    fflush(stdin);
    printf("Ingrese el valor de x: \n('inf' para infinito)\n\n");
    scanf("%s", x);
    fflush(stdin);

    // calcular y mostrar el limite
    printf("El limite de la funcion cuando x tiende a %s es %.2lf", x, limite(funcion, x));
}