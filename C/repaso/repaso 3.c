#include <stdio.h>
#include <string.h>

/* Escriba un programa que dada una cadena s y un entero k, sea capaz de devolver
el número máximo de letras vocales en cualquier subcadena de s con longitud k.
Ejemplo:
Entrada: s = "abciiidef", k = 3
Salida: 1
Explicación: La subcadena "iii" contiene 3 letras vocales */

int main() {
    char s[100];
    int k, max_vocales = 0;
    printf("Ingrese la cadena: ");
    scanf("%s", s);
    printf("Ingrese el entero k: ");
    scanf("%d", &k);
    
    // Calcular el máximo de vocales en subcadenas de longitud k
    for (size_t i = 0; i <= strlen(s) - k; i++) {
        int count = 0;
        for (size_t j = i; j < i + k; j++) {
            if (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u') {
                count++;
            }
        }
        if (count > max_vocales) {
            max_vocales = count;
        }
    }
    
    printf("El número máximo de vocales en una subcadena de longitud %d es: %d\n", k, max_vocales);
    return 0;
}
