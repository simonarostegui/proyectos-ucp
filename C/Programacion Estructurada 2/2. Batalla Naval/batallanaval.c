#include <stdio.h> 
#include <stdlib.h> // rand
#include <time.h> // rand aleatorio

// Alumno: Arostegui Simón
int main(void)
{
    srand(time(NULL));
    int i, j, x, y; // auxiliares e indice
    int barcos_hundidos = 0; // cantidad de barcos hundidos
    int campoEnemigo[10][10] = {0}; // campo de juego
    int campoJuego[10][10] = {0};
    int valid_input; // validar entrada

    // colocar los barcos en el campo del enemigo
    for (i = 0; i < 5; i++) {
        do {
            x = rand() % 10;
            y = rand() % 10;
        } while (campoEnemigo[x][y] == 1);
        campoEnemigo[x][y] = 1;
    }
    
    // bucle principal del juego
    while (barcos_hundidos < 5) {
        // imprimir el campo de juego
        printf("Campo de Juego: \n   ");
        for (j = 1; j <= 10; j++) {
            printf("%2d ", j);
        }
        printf("\n");
        for (i = 0; i < 10; i++) {
            printf("%2d ", i + 1);
            for (j = 0; j < 10; j++) {
                printf(" %c ", campoJuego[i][j] == 1 ? 'X' : (campoJuego[i][j] == 2 ? 'O' : '#'));
            }
            printf("\n");
        }
        printf("Barcos restantes: %d\n", 5 - barcos_hundidos);

        // pedir coordenadas
        do {
            printf("Ingrese las coordenadas X Y que desea atacar (1-10):\n");
            valid_input = scanf("%d %d", &x, &y);
            while (getchar() != '\n'); // limpiar el buffer
        } while (!valid_input || x < 1 || x > 10 || y < 1 || y > 10);

        x--; y--; // ajustar a índices de array

        // verificar si el ataque fue exitoso
        if (campoEnemigo[x][y] == 1 && campoJuego[x][y] != 1) {
            campoJuego[x][y] = 1; // guardar la posición como barco hundido
            barcos_hundidos++; // incrementar la cantidad de barcos hundidos
        } else if (campoJuego[x][y] == 0) {
            campoJuego[x][y] = 2; // guardar la posición como disparo fallido
        }

        printf("\e[1;1H\e[2J"); // limpiar la pantalla
    }
    
    printf("Victoria!\n");
}