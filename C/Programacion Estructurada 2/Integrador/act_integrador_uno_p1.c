#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <windows.h>

#define color SetConsoleTextAttribute

//PENDIENTE: acceso a archivo, mecanicas de ultima carta, habilidades de las cartas, detector de turno, suma de robo al enemigo, organisar mediante funciones, punteros, 7 segmentos


void crearMazo(char (*mazo)[15]);

void displayNumero(int num);

void mostrarUltimaCarta(char mazo[][15], int ultima_carta[], HANDLE hConsole);

void mostrarMano(HANDLE hConsole, int cartas_p1, int mano_p1[][50], char mazo[][15]);

int main()
{
    FILE *ar;
    //Crear Partida Nueva
    int crear_partida;
    printf("Desea crear una partida nueva?\n(1 = Si, 2= No)");
    scanf("%i",&crear_partida);
    
    if (crear_partida){
        ar = fopen("turno.txt","w");
        fprintf(ar,"0");
        fclose(ar);
    }else{
        return 0;
    }
    //Crear mazo
    char mazo[4][15];
    crearMazo(mazo);
    
    //inicializar la mano del jugador 1
    int mano_p1[2][50];
    for(int i=0; i<2; i++)
    {
       for(int j=0; j<50; j++)
        {                
            mano_p1[i][j]=-1;
        }
    }

    //repartir la primera mano del jugador 1

    int fila;
    int columna;
    int cartas_p1=0;
    srand(time(0));

    for (int i=0; i<7; i++)
    {
        fila = rand()%(4);
        columna = rand()%(15);
        mano_p1[0][i]=fila;
        mano_p1[1][i]=columna;
        cartas_p1++;
    }


    //definir primer carta jugada
    int ultima_carta[2];

    fila = rand()%(4);
    columna = rand()%(10);
    ultima_carta[0]=fila;
    ultima_carta[1]=columna;

    
    //inicialsamos el juego
    int turno;

    ar = fopen ("turno.txt", "r");
    if (ar == NULL) {
        printf("error .\n");
        return 1;
    }
    fscanf(ar ,"%i", &turno);
    fclose(ar);

    
    if (turno == 0) //chequeamos que no halla una instancia de juego activa
    {
    int contador=0;
    int cartas_p2=7;
    int end=0;

    ar = fopen ("cartas_p1.txt", "w"); //guardamos las cartas iniciles del p1
    if (ar == NULL) {
        printf("error .\n");
        return 1;
    }
    fprintf(ar,"%i",cartas_p1);
    fclose(ar);

    ar = fopen ("cartas_p2.txt", "w"); //guardamos las cartas iniciles del p2
    if (ar == NULL) {
        printf("error .\n");
        return 1;
    }
    fprintf(ar,"%i",cartas_p2);
    fclose(ar);

    ar = fopen ("ultima_carta.txt", "w"); //guardamos la primer carta
    if (ar == NULL) {
        printf("error .\n");
        return 1;
    }
    fprintf(ar,"%i %i",ultima_carta[0],ultima_carta[1]);
    fclose(ar);

    ar = fopen ("turno.txt", "w"); //seteamos el turno al p1
    if (ar == NULL) {
        printf("error .\n");
        return 1;
    }
    fprintf(ar,"%i",1);
    fclose(ar);

    ar = fopen ("contador.txt", "w");
        if (ar == NULL) {
            printf("error.\n");
            return 1;
        }
        fprintf(ar ,"%i",1);
        fclose(ar);

    ar = fopen ("robo_p1.txt", "w"); // Crea el archivo si no existe.
        if (ar == NULL) {
            printf("error 2.\n");
            return 1;
        }
        fprintf(ar,"%i",0);
        fclose(ar);

    ar = fopen ("robo_p2.txt", "w"); // Crea el archivo si no existe.
        if (ar == NULL) {
            printf("error 2.\n");
            return 1;
        }
        fprintf(ar,"%i",0);
        fclose(ar);

    int jugada_tipo;
    int jugada_carta;
    char jugada_especial;
    int robo_p1;
    int robo_p2;
    
    do //bucle de juego
    {
        //Jugar 
        ar = fopen ("contador.txt", "r");
        if (ar == NULL) {
            printf("error.\n");
            return 1;
        }
        fscanf(ar ,"%i", &contador);
        fclose(ar);




        ar = fopen ("turno.txt", "r");
        if (ar == NULL) {
            printf("error.\n");
            return 1;
        }
        fscanf(ar ,"%i", &turno);
        fclose(ar);

        
        int check1=0;

        ar = fopen ("turno.txt", "r");
        if (ar == NULL) {
            printf("error.\n");
            return 1;
        }
        fscanf(ar ,"%i", &turno);
        fclose(ar);

        //mostrar ultima carta jugada
        ar = fopen ("ultima_carta.txt", "r");
            if (ar == NULL) {
                printf("error.\n");
                return 1;
            }
            fscanf(ar,"%i %i",&ultima_carta[0],&ultima_carta[1]);
            fclose(ar);
                
        printf("\nULTIMA CARTA JUGADA: ");
        HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE); 
        mostrarUltimaCarta(mazo,ultima_carta,hConsole);

        color(hConsole,7);//blanco

        if (turno==1) //chequeamos que sea nuestro turno
        {
        
            do
            {
                ar = fopen ("contador.txt", "r");
                if (ar == NULL) {
                    printf("error.\n");
                    return 1;
                }
                fscanf(ar ,"%i", &contador);
                fclose(ar);

                //cartas del p2
                ar = fopen ("cartas_p2.txt", "r");
                if (ar == NULL) {
                    printf("error 1.\n");
                    return 1;
                }
                fscanf(ar,"%i",&cartas_p2);
                fclose(ar);

                ar = fopen ("ultima_carta.txt", "r");
                if (ar == NULL) {
                    printf("error 2.\n");
                    return 1;
                }
                fscanf(ar,"%i%i",&ultima_carta[0],&ultima_carta[1]);
                fclose(ar);
                //mostrar el contador 
                printf("Contador de turnos:\n");
                displayNumero(contador);


                //mostrar las cartas del oponente
                printf("\nle quedan %i cartas al oponente: ",cartas_p2);


                    ar = fopen ("robo_p1.txt", "r");
                    if (ar == NULL) {
                        printf("error 2.\n");
                        return 1;
                    }
                    fscanf(ar,"%i",&robo_p1);
                    fclose(ar);

                    for (int i = 0; i<robo_p1 ; i++)
                    {
                        fila = rand()%(4);
                        columna = rand()%(15);
                        mano_p1[0][cartas_p1]=fila;
                        mano_p1[1][cartas_p1]=columna;
                        cartas_p1++;
                    }

                    ar = fopen ("robo_p1.txt", "w");
                    if (ar == NULL) {
                        printf("error 2.\n");
                        return 1;
                    }
                    fprintf(ar,"%i",0);
                    fclose(ar);

                //mostrar mano del gugador 1
                mostrarMano(hConsole,cartas_p1,mano_p1,mazo);
                printf("|");
                printf("\nDesea jugar una carta(1) o realizar otra accion?(2):\n");
                scanf("%i",&jugada_tipo);
                if (jugada_tipo == 1)                           //jugar una carta
                {
                    printf("\nIngrese el numero correspondiente a la carta que desea jugar\n");
                    scanf("%i",&jugada_carta);
                    jugada_carta--;
                    if (mano_p1[1][jugada_carta]>=13)  
                    {
                        printf("Que color quieres que tome la carta? Azul(1) Verde(2) Rojo(3) Amarillo(4) : \n");
                        scanf("%i",&(ultima_carta[0]));
                        ultima_carta[0]--;
                        ultima_carta[1]=mano_p1[1][jugada_carta];
                        
                        printf("%i",mano_p1[1][jugada_carta]);
                        if (mano_p1[1][jugada_carta]==14)
                        {
                            ar = fopen ("robo_p2.txt", "r");
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fscanf(ar,"%i",&robo_p2);
                            fclose(ar);
                            printf("%i",robo_p2);
                            robo_p2=robo_p2+4;
                            printf("%i",robo_p2);


                            ar = fopen ("robo_p2.txt", "w"); //
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fprintf(ar,"%i",robo_p2);
                            fclose(ar);
                        
                        }
                        else
                        {
                            ar = fopen ("turno.txt", "w"); //
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fprintf(ar,"%i",2);
                            fclose(ar);

                        }
                        ar = fopen ("cartas_p1.txt", "w"); 
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fprintf(ar,"%i",cartas_p1);
                            fclose(ar);

                    for (int i = jugada_carta; i < cartas_p1 - 1; i++) //reacomodamos las cartas
                        {
                            mano_p1[0][i] = mano_p1[0][i+1];
                            mano_p1[1][i] = mano_p1[1][i+1];
                        }

                        cartas_p1--;


                    contador++;
                    check1=1;
                    }
                    else if (mano_p1[1][jugada_carta]>=0 && mano_p1[1][jugada_carta]<13)
                    {
                        if (ultima_carta[0]==mano_p1[0][jugada_carta]||ultima_carta[1]==mano_p1[1][jugada_carta])
                        {
                            ultima_carta[0]=mano_p1[0][jugada_carta];
                            ultima_carta[1]=mano_p1[1][jugada_carta];

                            
                            if (mano_p1[1][jugada_carta]==12)
                            {
                                ar = fopen ("robo_p2.txt", "r");
                                if (ar == NULL) {
                                    printf("error .\n");
                                    return 1;
                                }
                                fscanf(ar,"%i",&robo_p2);
                                fclose(ar);
                               
                                robo_p2=robo_p2 +2;
                                


                                ar = fopen ("robo_p2.txt", "w"); //
                                if (ar == NULL) {
                                    printf("error .\n");
                                    return 1;
                                }
                                fprintf(ar,"%i",robo_p2);
                                fclose(ar);

                            }else if (mano_p1[1][jugada_carta]==11||mano_p1[1][jugada_carta]==10)
                            {
                                ar = fopen ("cartas_p1.txt", "w"); 
                                if (ar == NULL) {
                                    printf("error .\n");
                                    return 1;
                                }
                                fprintf(ar,"%i",cartas_p1);
                                fclose(ar);
                                
                            }else if(mano_p1[1][jugada_carta]<10)
                            {                    
                                ar = fopen ("turno.txt", "w"); //
                                if (ar == NULL) {
                                    printf("error .\n");
                                    return 1;
                                }
                                fprintf(ar,"%i",2);
                                fclose(ar);
                                

                                ar = fopen ("cartas_p1.txt", "w"); 
                                if (ar == NULL) {
                                    printf("error .\n");
                                    return 1;
                                }
                                fprintf(ar,"%i",cartas_p1);
                                fclose(ar);
                            }
                            for (int i = jugada_carta; i < cartas_p1 - 1; i++) 
                            {
                                mano_p1[0][i] = mano_p1[0][i+1];
                                mano_p1[1][i] = mano_p1[1][i+1];
                            }

                            cartas_p1--;
                            contador++;
                            check1=1;
     
                        }
                        else
                        {
                            printf("\nCarta invalida\n");

                        }
                    }
                    else
                    {
                        printf("\nError, carta no encontrada \n");
                    }
                    ar = fopen ("cartas_p1.txt", "w"); 
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fprintf(ar,"%i",cartas_p1);
                            fclose(ar);

                        ar = fopen("ultima_carta.txt", "w");
                        if (ar == NULL) {
                            printf("error.\n");
                            return 1;
                        }
                        fprintf(ar, "%i %i", ultima_carta[0], ultima_carta[1]);
                        fclose(ar);



                }
                else if (jugada_tipo==2)                        //robar y acciones especiales
                { 
                    printf("\ningrese 'r' para robar, 't' para terminar :\n");

                    scanf("%s",&jugada_especial);
                    fflush(stdin);
    
                    switch (jugada_especial)
                    {
                    case 'r':
                        
                        fila = rand()%(4);
                        columna = rand()%(15);

                        mano_p1[0][cartas_p1]=fila;
                        mano_p1[1][cartas_p1]=columna;
                        cartas_p1++;

                        ar = fopen ("turno.txt", "w"); //
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fprintf(ar,"%i",2);
                            fclose(ar);
                            contador++;

                            ar = fopen ("cartas_p1.txt", "w"); //guardamos las cartas iniciles del p1
                            if (ar == NULL) {
                                printf("error .\n");
                                return 1;
                            }
                            fprintf(ar,"%i",cartas_p1);
                            fclose(ar);

                        check1=1;
                        printf("\n has robado una carta \n");
                        break;
                    case 't':
                        end=1;
                        check1=1;
                        break;

                    default:
                        printf("\nError\n");
                        break;
                    }
                }
                else
                {
                printf("\nError\n");
                }

                // despues de jugar una carta o robar
                ar = fopen ("ultima_carta.txt", "w"); //guardamos la primer carta
                if (ar == NULL) {
                    printf("error .\n");
                    return 1;
                }
                fprintf(ar,"%i %i",ultima_carta[0],ultima_carta[1]);
                fclose(ar);
                
            } while (!check1);
            ar = fopen ("contador.txt", "w");
            if (ar == NULL) {
                printf("error.\n");
                return 1;
            }
            fprintf(ar ,"%i",contador);
            fclose(ar);
        }else
        {
            printf("\n      NO ES TU TURNO");
            char espera;
            fflush(stdin);
            scanf("%c",&espera);
            fflush(stdin);

            
            
        }
        ar = fopen ("contador.txt", "w");
        if (ar == NULL) {
            printf("error.\n");
            return 1;
        }
        fprintf(ar ,"%i",contador);
        fclose(ar);
        
        

        if (cartas_p1==0||cartas_p2==0)
        {
            end=1;
        }
        

    } while (!end);

    ar = fopen ("turno.txt", "w");
    if (ar == NULL) {
        printf("error.\n");
        return 1;
    }
    fprintf(ar,"0");
    fclose(ar);

    if(cartas_p1==0)
    {
        printf("\nGANASTE!!!!");
    }
    if(cartas_p2==0)
    {
        printf("\nperdiste:(");
    }

    
    
    else
    {
        printf("\nerror, otro juego en progreso");
    }
     
    
}
}

void crearMazo(char (*mazo)[15]) {
    int h = 0;
    char cartas[60] = {'0','1','2','3','4','5','6','7','8','9',157,'~','+','@',172,
                       '0','1','2','3','4','5','6','7','8','9',157,'~','+','@',172,
                       '0','1','2','3','4','5','6','7','8','9',157,'~','+','@',172,
                       '0','1','2','3','4','5','6','7','8','9',157,'~','+','@',172};
                       
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 15; j++) {                
            mazo[i][j] = cartas[h];
            h++;
        }
    }
}

void displayNumero(int num) {
    // Patrones de segmentos para 0-9
    const char* digitos[10][5] = {
        {" _ ", "| |", "|_|", "   "}, // 0
        {"   ", "  |", "  |", "   "}, // 1
        {" _ ", " _|", "|_ ", "   "}, // 2
        {" _ ", " _|", " _|", "   "}, // 3
        {"   ", "|_|", "  |", "   "}, // 4
        {" _ ", "|_ ", " _|", "   "}, // 5
        {" _ ", "|_ ", "|_|", "   "}, // 6
        {" _ ", "  |", "  |", "   "}, // 7
        {" _ ", 
         "|_|", 
         "|_|", "   "}, // 8
        {" _ ", "|_|", " _|", "   "}  // 9
    };

    int decenas = num / 10;
    int unidades = num % 10;

    // Imprime cada fila de los dos dígitos
    for (int i = 0; i < 4; i++) {
        printf("%s %s\n", digitos[decenas][i], digitos[unidades][i]);
    }
}

void mostrarUltimaCarta(char mazo[][15], int ultima_carta[], HANDLE hConsole) {
    
    if (ultima_carta[1] >= 0 && ultima_carta[1] <= 14) {
        switch (ultima_carta[0]) {
            case 0: color(hConsole,1); break; // azul
            case 1: color(hConsole,2); break; // verde
            case 2: color(hConsole,4); break; // rojo
            case 3: color(hConsole,6); break; // amarillo
            default: break;
        }
    }

    printf(" %c \n", mazo[ultima_carta[0]][ultima_carta[1]]);
    color(hConsole,7);
}

void mostrarMano(HANDLE hConsole, int cartas_p1, int mano_p1[][50], char mazo[][15]){
    printf("\nNum: ");
    for (int i = 0; i < cartas_p1; i++)
        {
            printf("| %i ",i+1);
        }
        printf("|");
        printf("\nCart:");
        for (int i = 0; i < cartas_p1; i++)
        {
            printf("|");
            if (mano_p1[1][i]>=0 && mano_p1[1][i]<13)
            {
                switch (mano_p1[0][i])
                {
                case 0:color(hConsole,1);break;//azul
                case 1:color(hConsole,2);break;//verde
                case 2:color(hConsole,4);break;//rojo
                case 3:color(hConsole,6);break;//amarillo
                default:break;
                }
            }
            else
            {
                color(hConsole,7);   
            }
                    
            printf(" %c ", mazo[mano_p1[0][i]][mano_p1[1][i]]);
        color(hConsole,7); 
    }
}
