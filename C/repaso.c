#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Crear un programa que simule un sistema de gestión de votos. El mismo deberá
ser capaz de:
• Permitir la carga manual de los votos obtenidos por cada partido en cada
localidad
• Reportar el partido ganador
• Reportar en porcentaje de votos obtenidos por cada partido
• Buscar votos por localidad y por partido
La elección de lleva adelante en cinco localidades (L1, L2, L3, L4 y L5) diferentes y el
total de partidos que participan son 3 (P1, P2 y P3). Cada localidad tiene un
máximo de 300 habitantes habilitados para votar.

Requisitos:
• Utilizar estructuras de tipo arreglo (array)
• Modularizar en código en funciones*/

void cargarVotos(int votos[5][3]) {
    bool valido;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 3; j++) {
            do {
                printf("Ingrese los votos para el partido %d en la localidad %d: ", j + 1, i + 1);
                scanf("%d", &votos[i][j]);
                valido = votos[i][j] >= 0 && votos[i][j] <= 300;
                if (!valido) {
                    printf("Error: Los votos deben estar entre 0 y 300.\n");
                }
            } while (!valido);
        }
    }
};

void reportarGanador(int votos[5][3]) {
    int votosPorPartido[3] = {0};
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 3; j++) {
            votosPorPartido[j] += votos[i][j];
        }
    }
    int ganador = 0;
    int maxVotos = votosPorPartido[0];
    for (int i = 1; i < 3; i++) {
        if (votosPorPartido[i] > maxVotos) {
            maxVotos = votosPorPartido[i];
            ganador = i;
        }
    }
    printf("El partido ganador es el %d con %d votos.\n", ganador + 1, maxVotos);
};

void reportarPorcentaje(int votos[5][3]) {
    int votosPorPartido[3] = {0};
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 3; j++) {
            votosPorPartido[j] += votos[i][j];
        }
    }
    int totalVotos = 0;
    for (int i = 0; i < 3; i++) {
        totalVotos += votosPorPartido[i];
    }
    for (int i = 0; i < 3; i++) {
        printf("El partido %d tiene un porcentaje de votos de %.2f%%.\n", i + 1, (float)votosPorPartido[i] / totalVotos * 100);
    }
};

void buscarVotos(int votos[5][3]) {
    int localidad, partido;
    printf("Ingrese la localidad: ");
    scanf("%d", &localidad);
    printf("Ingrese el partido: ");
    scanf("%d", &partido);
    printf("Los votos para el partido %d en la localidad %d son %d.\n", partido, localidad, votos[localidad - 1][partido - 1]);
};

int main() {
    int votos[5][3];

    cargarVotos(votos);
    reportarGanador(votos);
    reportarPorcentaje(votos);
    buscarVotos(votos);

    return 0;
}

