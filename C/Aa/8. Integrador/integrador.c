#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

/*Alumnos: Arostegui Simon
Goya Bautista
Gomez Guillermo
Pujol Valentin*/

/*1. El sistema solicitara y validara el nombre de usuario y contraseña para dar acceso al sistema.
2. El sistema brindará la opción de visualizar el historial (semanal) de carga y descarga de
cereales de cada silo (10 en total).
3. El sistema solicitará al empleado el número de silo del que desea registrar información (carga
y descarga).
4. El sistema mostrará al usuario el número total de silos disponibles
5. El sistema brindará al usuario una opción para cerrar el programa.*/

int login(char * usuario, char * contrasena);


int main(void){
    char usuario[30], contrasena[30];
    int i, k, v, x=100, y, y2; // i - indice para loop. k - columna. v- fila. x - para las opciones. y- carga y descarga
    int siloCargas[10][7];
    int siloDescargas[10][7];
    int loginIncorrecto = 1;
    
    printf("Bienvenido a COPRA SA.\n");
    while(loginIncorrecto){ // Mientras sea 1 sigue corriendo, como un booleano
        printf("Ingrese su Usuario:\n");
        gets(usuario);
        printf("Ingrese su Contrase%ca:\n", 164);
        gets(contrasena);
        loginIncorrecto = login(usuario, contrasena); // Devuelve 0 si las dos comparaciones de usuario y contrasena son correctas
    }

    //Interfaz facha
    printf(" ## ##    ## ##   ### ##   ### ##     ##               ## ##     ##     \n##   ##  ##   ##   ##  ##   ##  ##     ##             ##   ##     ##    \n##       ##   ##   ##  ##   ##  ##   ## ##            ####      ## ##   \n##       ##   ##   ##  ##   ## ##    ##  ##            #####    ##  ##  \n##       ##   ##   ## ##    ## ##    ## ###               ###   ## ###  \n##   ##  ##   ##   ##       ##  ##   ##  ##           ##   ##   ##  ##  \n ## ##    ## ##   ####     #### ##  ###  ##            ## ##   ###  ## \n\n===========================================\n\n");
    
    for (i = 0; i < 10; i++){
        for (k = 0; k < 7 ; k++){
            siloCargas[i][k] = rand()%1501; // Crea un valor y lo añade a la matriz en columna i fila k
            siloDescargas[i][k] = rand()%1501; // i = Silo. k = Dia
        }  
        
    }

    while (x != 0){
        printf("Silos Disponibles:\n");
        printf("==========================================\n| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |\n==========================================\n\n");
        printf("Ingrese el silo que desea visualizar.\nSi desea terminar, ingrese 0.\n");
        scanf("%i", &x);
        char opcion[30];

        if(x == 0){
            break;
        }else if(x < 11){
            printf("Ingrese el historial que desea ver (Carga/Descarga):\n");
            fflush(stdin);
            gets(opcion);
            char dias[7][10] = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"};

            while(opcion[i]){ // Vuelve 'opcion' a minuscula
                opcion[i] = tolower(opcion[i]);
                i++;
            }
            y = strcmp(opcion, "carga"); // Compara la variable con 'carga' o 'descarga'
            y2 = strcmp(opcion, "descarga");

            if(y == 0){ // Si 'carga' es correcto, corre
                v=1;
                printf("\nHistorial semanal de cargas de Silo %i:\n", x);
                for (i = 0; i < 7; i++){
                    printf("%s - %i toneladas\n", dias[v-1], siloCargas[x-1][i-1]);
                    v++;
                }
                printf("\n");} 
            else if(y2 == 0){ // Si 'descarga' es correcto, corre
                v=1;
                printf("\nHistorial semanal de descargas de Silo %i:\n", x);
                for (i = 0; i < 7; i++){
                    printf("%s - %i toneladas\n", dias[v-1], siloDescargas[x-1][i-1]);
                    v++;
                }
                printf("\n");}
            else{
                break; // Si no, explota
                }
            
        }else{
            printf("Silo no registrado. Intente nuevamente.\n");
        }
    }
}

int login(char * usuario, char * contrasena){ // Puntero a usuario y contraseña de funcion Main 
    char defUsuario[] = "admin"; // default Usuario
    char defContrasena[] = "123"; // default Contraseña
    

    int x = strcmp(usuario, defUsuario);
    int y = strcmp(contrasena, defContrasena);
    if(x == 0 && y == 0){
        printf("\nContrase%ca correcta! Bienvenido!.\n\n===========================================\n\n", 164);
        return 0;
    }else{
        printf("\nContrase%ca incorrecta. Intente nuevamente.\n\n", 164);
        return 1;
    }
}