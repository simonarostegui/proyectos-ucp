#include <stdio.h>
#include <string.h>
#include <ctype.h>



int main(void) {
    char alfabeto[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    char cifrado[100] = "";
    char texto[100];
    int x, modo = 0;
    
    FILE * cesar;

    while (modo == 0)
    {
        printf("Que desea hacer?\n1. Encriptar Texto\n2. Desencriptar Texto\n");
        scanf("%i", &modo); // Pide al usuario que elija un modo de operación.
    }
    
    if (modo == 1) // Si el usuario elige 1, este encripta.
    {
        printf("Ingrese un numero del 1-25, este sera su clave:\n");
        scanf("%i", &x);
        fflush(stdin);
        printf("Ingrese un texto el cual cifrar:\n");
        gets(texto);

        for (size_t i = 0; i < strlen(texto); i++) {
            if (texto[i] == ' ') { // Deja los espacios en blanco sin cambiar.
                cifrado[i] = ' ';
            }
            texto[i] = tolower(texto[i]);

            for (int j = 0; j < 26; j++) {
                if (texto[i] == alfabeto[j]) {
                    if (j + x < 26) {  // Si la sumatoria de el numero de la letra mas la clave es menor al numero total de letras en el alfabeto, solamente elige.
                        cifrado[i] = alfabeto[j + x];
                    } else {
                        cifrado[i] = alfabeto[j + x - 26]; // Si sobrepasa el alfabeto, le resta 26 al valor, volviendo al principio.
                    }
                    break;
                }
            }
        }

        cesar = fopen("C:\\Programacion\\Programacion Estructurada\\10. Cesar\\encriptado.txt", "w"); // Cambiar a TU dirección donde guardas el archivo. Agregar \ a cada barra.
        fprintf(cesar, "%s\n", cifrado); // Crea o sobreescribe archivo 'cesar'
        printf("%s\n", cifrado);
    }else if (modo == 2)
    {
        printf("Ingrese su clave. Este es un valor del 1-25\n");
        scanf("%i", &x);
        cesar = fopen("C:\\Programacion\\Programacion Estructurada\\10. Cesar\\encriptado.txt", "r"); // Cambiar a TU dirección donde guardas el archivo. Agregar \ a cada barra.
        fgets(texto, 100, cesar); // Guarda el valor dentro del archivo cesar dentro de variable texto.
        printf("%s", texto);
        for (size_t i = 0; i < strlen(texto); i++) {
            if (texto[i] == ' ') {
                cifrado[i] = ' '; // Deja los espacios sin cambiar.
            }

            for (int j = 0; j < 26; j++) {
                if (texto[i] == alfabeto[j]) {
                    cifrado[i] = alfabeto[(j + 26 - x)%26];  // Numero alfabeto + 26 - Clave es dividido por 26, el resto de esta division se convierte en el numero del alfabeto.
                    break;
                }
            }
        }
        printf("%s", cifrado);
    } else
    { // En el caso de que el usuario elija un valor de modo mayor a 2 o menor a 1.
        printf("Valor no reconocido.\n");
    }
    
    
    



    fclose(cesar); // Cierra independientemente de la opcion elegida por las dudas.
}
