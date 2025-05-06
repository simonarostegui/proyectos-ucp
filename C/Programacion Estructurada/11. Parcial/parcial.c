#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define NUM_CANDIDATOS 3
#define MAX_NOMBRE 50
#define MAX_APELLIDO 50

// Estructura para candidatos
struct candidato {
    char nombre[MAX_NOMBRE];
    char apellido[MAX_APELLIDO];
    int edad;
    int sexo;
    int distancia;
    int nivel;
    int experiencia;
    float calificacion;
};

// Prototipos de funciones
float calcular_calificacion(int edad, int distancia, int nivel, int experiencia);
void generar_candidato(struct candidato *c, const char *fNombreLista[], const char *hNombreLista[], const char *apellidoLista[]);
void mostrar_candidato(const struct candidato *c, int num);
void escribir_candidato_elegido(FILE *file, const struct candidato *c);

int main(void) {
    // Listas de nombres y apellidos
    const char *fNombreLista[] = {"Eliana", "Lisa", "Karina", "Sofia", "Micaela", "Yanina", "Alejandra", "Daiana", "Joaquina", "Ludmila", "Oriana", "Carmen", "Silvana"};
    const char *hNombreLista[] = {"Fernando", "Jorge", "Nicolas", "Matias", "Juan", "Enzo", "Rodrigo", "Miguel", "Pedro", "Ivan", "Gabriel", "Damian", "Fabian", "Angel"};
    const char *apellidoLista[] = {"Rodriguez", "Fernandez", "Figueredo", "Ayala", "Cabrera", "Montero", "Porta", "Perani", "Acevedo", "Weiteder", "Riquelme", "Moreno", "Larretta"};

    struct candidato candidatos[NUM_CANDIDATOS];
    int modo, i;
    float max_calificacion = 0;
    int candidato_elegido = 0;
    FILE *jefe_it;

    srand(time(NULL));

    printf("Ingrese el Modo de Operacion:\n1. Crear Candidatos (Automatico)\n2. Cargar Candidato Elegido\n");
    scanf("%d", &modo);

    switch (modo) {
        case 1:
            jefe_it = fopen("C:\\Programacion\\Programacion Estructurada\\11. Parcial\\jefe_it.txt", "w");
            if (jefe_it == NULL) {
                perror("Error al abrir el archivo");
                return 1;
            }

            for (i = 0; i < NUM_CANDIDATOS; i++) {
                generar_candidato(&candidatos[i], fNombreLista, hNombreLista, apellidoLista);
                mostrar_candidato(&candidatos[i], i+1);

                if (candidatos[i].calificacion > max_calificacion) {
                    max_calificacion = candidatos[i].calificacion;
                    candidato_elegido = i;
                }
            }

            escribir_candidato_elegido(jefe_it, &candidatos[candidato_elegido]);
            fclose(jefe_it);
            break;

        case 2:
            jefe_it = fopen("C:\\Programacion\\Programacion Estructurada\\11. Parcial\\jefe_it.txt", "r");
            if (jefe_it == NULL) {
                perror("Error al abrir el archivo");
                return 1;
            }

            char buffer[100];
            while (fgets(buffer, sizeof(buffer), jefe_it) != NULL) {
                printf("%s", buffer);
            }
            fclose(jefe_it);
            break;

        default:
            printf("Opcion no reconocida. Cerrando el programa.\n");
            return 1;
    }

    return 0;
}

float calcular_calificacion(int edad, int distancia, int nivel, int experiencia) {
    int puntos_edad = (edad < 25) ? 3 : (edad < 36) ? 5 : 2;
    int puntos_distancia = (distancia < 20) ? 3 : (distancia < 50) ? 2 : 5;
    int puntos_nivel = (nivel == 1) ? 1 : (nivel == 2) ? 3 : 6;
    int puntos_experiencia = experiencia ? 5 : 0;

    return puntos_edad + puntos_distancia + puntos_nivel + puntos_experiencia;
}

void generar_candidato(struct candidato *c, const char *fNombreLista[], const char *hNombreLista[], const char *apellidoLista[]) {
    c->sexo = rand() % 2;
    strcpy(c->nombre, c->sexo ? fNombreLista[rand() % 13] : hNombreLista[rand() % 14]);
    strcpy(c->apellido, apellidoLista[rand() % 13]);
    c->edad = (rand() % (60 - 18 + 1)) + 18;
    c->distancia = rand() % 101;
    c->nivel = rand() % 3 + 1;
    c->experiencia = rand() % 2;
    c->calificacion = calcular_calificacion(c->edad, c->distancia, c->nivel, c->experiencia);
}

void mostrar_candidato(const struct candidato *c, int num) {
    printf("Candidato %d:\n", num);
    printf("Nombre: %s\n", c->nombre);
    printf("Apellido: %s\n", c->apellido);
    printf("Edad: %d\n", c->edad);
    printf("Distancia: %d km\n", c->distancia);
    printf("Nivel de Estudio: %d\n", c->nivel);
    printf("Experiencia: %d\n", c->experiencia);
    printf("Calificacion: %.2f\n\n", c->calificacion);
}

void escribir_candidato_elegido(FILE *file, const struct candidato *c) {
    fprintf(file, "Nombre: %s\nApellido: %s\n", c->nombre, c->apellido);
}