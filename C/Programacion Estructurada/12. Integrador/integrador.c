#include <stdio.h>


//Crea variables globales MAX_NODOS y NOMBRE_LENGTH, el cual seran usados para crear los archivos y conexiones.
#define MAX_NODOS 7 
#define NOMBRE_LENGTH 20

struct computadoras{
    int conexiones[7];
};

FILE * files[MAX_NODOS];

int main(void)
{
    int x = 1, y, z = 1, nodoNuevo; // x = Nodo Actual, y = Opcion elegida, z = Bucle, nodoNuevo = cambio de nodo elegido.
    char filename[NOMBRE_LENGTH]; 
    char userText[100]; 
    char c;

    //Inicializa una esctructura de 7 objetos, dandole valor definido a cada .conexiones mediante inicialización
    struct computadoras computadora[7] = {
        [0] = {.conexiones = {2, 3, 5, 6}},
        [1] = {.conexiones = {3, 6, 1}},
        [2] = {.conexiones = {2, 1, 4, 6}},
        [3] = {.conexiones = {3, 7, 5}},
        [4] = {.conexiones = {4, 1, 6}},
        [5] = {.conexiones = {7, 1, 2, 3, 5}},
        [6] = {.conexiones = {6, 4}},
    };

    printf("Bienvenido.\n\n");

    sprintf(filename, "%d\\computer_%d.txt", x, x); //Declara a filename como la direccion del archivo, ej 1\\computer_1.txt
    files[x- 1] = fopen(filename, "a+"); //Abre (o crea) archivos, siendo x el nodo. (x-1 porque C inicializa en 0)

    if (files[x - 1] == NULL) {
        fprintf(stderr, "Error al abrir el archivo %d\n", x);
        return 1;
    }
    
    while (z){
        printf("\nUsted se encuentra en la computadora %d. Que desea hacer?\n1. Escribir Archivo.\n2. Leer Archivo.\n3. Cambiar de Nodo.\n4. Cerrar.\n", x);
        printf("Conexiones posibles:");
        for (size_t j = 0; j < sizeof(computadora[x - 1].conexiones) / sizeof(computadora[x - 1].conexiones[0]); j++) {
            if (computadora[x - 1].conexiones[j] != 0) { // La verdadera matriz consiste de X X X X X X X, rellenando los valores que no tienen numero con cero. Esto los obvia.
                printf(" %d", computadora[x - 1].conexiones[j]);
            }
            //printf(" %d", computadora[x - 1].conexiones[j]);
        }
        printf("\n");

        scanf("%i", &y);

        switch (y){
        case 1: // Caso 'Escribir'
            fflush(stdin);
            printf("Ingrese su texto:\n");
            fgets(userText, sizeof(userText), stdin);
            fprintf(files[x - 1], "%s\n", userText);
            break;
        case 2: // Caso 'Abrir'
            fflush(stdin);
            fseek(files[x - 1], 0, SEEK_SET); //Abre el archivo desde el comienzo y lee todo.
            c = fgetc(files[x-1]); 
            while (c != EOF) 
            { 
                printf ("%c", c); 
                c = fgetc(files[x-1]); 
            } 
            break;
        case 3:
            fflush(stdin);
            printf("A que nodo desea cambiar?\n");
            scanf("%i", &nodoNuevo);

            int nodoValido = 0;
            for (size_t j = 0; j < sizeof(computadora[x - 1].conexiones) / sizeof(computadora[x - 1].conexiones[0]); j++) {
                if (computadora[x - 1].conexiones[j] == nodoNuevo) { //Checkea si Nodo Nuevo es parte de .conexiones
                    nodoValido = 1;
                    break;
                }
            }

            if (nodoValido && nodoNuevo >= 1 && nodoNuevo <= MAX_NODOS) {
                fclose(files[x - 1]);
                x = nodoNuevo; //Si nodo es valido y nodoNuevo no sobrepasa los limites del arreglo, se cambia de nodo.
                sprintf(filename, "%d\\computer_%d.txt", x, x);
                files[x - 1] = fopen(filename, "a+");
                if (files[x - 1] == NULL) {
                    fprintf(stderr, "Error al abrir el archivo %d\n", x);
                    return 1;
                }
            } else {
                printf("Nodo no valido.\n");
            }
            break;
        default:
            fclose(files[x - 1]);
            z = 0; // Cualquier otra opcion rompe el bucle.
            break;
        }
    }

    for (size_t i = 1; i <= MAX_NODOS; i++) {
        fclose(files[i - 1]); // Cierra todos los nodos por las dudas.
    }
    
}
