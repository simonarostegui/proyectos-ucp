#include <stdio.h>
#include <stdlib.h>

/*Luego de un evento, en donde 5 especialistas disertaron sobre Transformación Digital, se realizó una
encuesta a 11 asistentes, elegidos al azar, para saber su opinión sobre los siguientes temas:
• Le gusto la temática del evento: si (1)-no (0)
• Indique el grado de satisfacción respecto de la organización del evento:
o (0) insatisfactorio
o (1) satisfactorio
o (2) muy satisfactorio
• Que disertación le resulto más interesante:
o (1) Lic. Esteban Dido
o (2) Ing. Elsa Capunta
o (3) Esp. Armando Bronca
o (4) Lic. Victor Tazo
o (5) Ing. Ana Conda
• Que le pareció el costo del evento: Calificar del 1 al 10
Se pide confeccione un programa que:
1. Permita hacer las preguntas a los usuarios, almacenar los datos recolectados y mostrar los
datos cargados (1,5 ptos)
2. Informe:
a. la cantidad de respuestas negativas y la cantidad de respuestas positivas respecto de la
temática del evento. (1 ptos)
b. El porcentaje de satisfacción respecto de la organización del evento. (1,5 ptos)
c. El nombre y apellido del disertante mas elegido y el menos elegido. (1,5 ptos)
d. La opinión del costo. Si la calificación promedio es: (1,5 ptos)
i. Menor a 6: “caro”
ii. Mayor o igual a 6 y menor a 8: “aceptable”
iii. Mayor o igual a 8: “excelente*/

int main(void)
{
    int i, k, v;
    int matriz[11][4]; // 0: Tematica del Evento. 1: Grado de Satisfaccion. 2: Disertacion. 3: Costo.

    // Valores Matriz Personalizados
    
    // Valores Matriz Aleatorios
    for (i = 0; i < 11; i++){
        for (k = 0; k < 4; k++){
            switch (k){
                case 0: // Tematica del Evento
                    v = rand()%2;
                    matriz[i][0] = v;
                    break;
                case 1: // Grado de Satisfaccion
                    v = rand()%3;
                    matriz[i][1] = v;
                    break;
                case 2: // Disertacion Favorita
                    v = rand()%5;
                    matriz[i][2] = v;
                    break;
                case 3: // Costo
                    v = rand()%10+1;
                    matriz[i][3] = v;
                    break;
                default:
                    break;
                }
            
        }
        
    }
    
    // Mostrar Tematica
    int respuestasPositivas = 0, respuestasNegativas = 0;
    for (i = 0; i < 11; i++)
    {
        if(matriz[i][0] == 0){
            respuestasNegativas++;
        }else{
            respuestasPositivas++;
        }
    }
    printf("\nTematica:\n");
    printf("Respuestas Positivas: %i\nRespuestas Negativas: %i\n", respuestasPositivas, respuestasNegativas);

    // Mostrar Satisfaccion
    int satisAux0 = 0, satisAux1 = 0, satisAux2= 0;

    for (i = 0; i < 11; i++){
        switch (matriz[i][1]){
        case 0:
            satisAux0++;
            break;
        case 1:
            satisAux1++;
            break;
        case 2:
            satisAux2++;
            break;
        }
    }
    satisAux0 = (satisAux0 *100)/11; // Porcentaje Insatisfactorio Regla de 3
    satisAux1 = (satisAux1 *100)/11; // Porcentaje Satisfactorio Regla de 3
    satisAux2 = (satisAux2 *100)/11; // Porcentaje Muy Satisfactorio Regla de 3

    printf("\nSatisafaccion respecto al evento:\n");
    printf("Porcentaje Insatisfactorio: %i%%\nPorcentaje Satisfactorio: %i%%\nPorcentaje Muy Satisfactorio: %i%%\n", satisAux0, satisAux1, satisAux2);
    
    // Disertacion Favorita
    char disertacion1[20] = "Lic. Esteban Dido", disertacion2[20] = "Ing. Elsa Capunta", disertacion3[20] = "Esp. Armando Bronca", disertacion4[20] = "Lic. Victor Tazo", disertacion5[20] = "Ing. Ana Conda"; //que lindo seria poder usar diccionarios, te extraño python
    int disAux1 = 0, disAux2 = 0, disAux3 = 0 , disAux4 = 0, disAux5 = 0;
    for (i = 0; i < 11; i++){
        switch(matriz[i][2]){
        case 0:
            disAux1++;
            break;
        case 1:
            disAux2++;
            break;
        case 2:
            disAux3++;
            break;
        case 3:
            disAux4++;
            break;
        case 4:
            disAux5++;
            break;
        }
    }

    printf("\nDisertacion Favorita: \n");
    if (disAux1 > disAux2 && disAux1 > disAux3 && disAux1 > disAux4 && disAux1 > disAux5){
        puts(disertacion1);
    }else if (disAux2 > disAux1 && disAux2 > disAux3 && disAux2 > disAux4 && disAux2 > disAux5){
        puts(disertacion2);
    }else if (disAux3 > disAux1 && disAux3 > disAux2 && disAux3 > disAux4 && disAux3 > disAux5){
        puts(disertacion3);
    }else if (disAux4 > disAux1 && disAux4 > disAux2 && disAux4 > disAux3 && disAux4 > disAux5){
        puts(disertacion4);
    }else{
        puts(disertacion5);
    }

    printf("\nDisertacion Menos Favorita: \n");
    if (disAux1 < disAux2 && disAux1 < disAux3 && disAux1 < disAux4 && disAux1 < disAux5){
        puts(disertacion1);
    }else if (disAux2 < disAux1 && disAux2 < disAux3 && disAux2 < disAux4 && disAux2 < disAux5){
        puts(disertacion2);
    }else if (disAux3 < disAux1 && disAux3 < disAux2 && disAux3 < disAux4 && disAux3 < disAux5){
        puts(disertacion3);
    }else if (disAux4 < disAux1 && disAux4 < disAux2 && disAux4 < disAux3 && disAux4 < disAux5){
        puts(disertacion4);
    }else{
        puts(disertacion5);
    }
    printf("\n");

    // Precio
    int precioCaro =0, precioAceptable =0 , precioEx= 0;
    for (i = 0; i < 11; i++){
        if (matriz[i][3] >= 6){
            if(matriz[i][3] >= 8){
                precioEx++;
            }else{
                precioAceptable++;
            }
        }else{
            precioCaro++;
        }
        
        
    }

    //Conversion a Porcentaje:
    precioCaro = (precioCaro * 100)/11;
    precioAceptable = (precioAceptable*100)/11;
    precioEx = (precioEx*100)/11;

    printf("Precio:\nExcelente: %i%%\nAceptable: %i%%\nCaro: %i%%\n\nConsenso:\n", precioEx, precioAceptable, precioCaro);
    if(precioEx > precioAceptable && precioEx > precioCaro){
        printf("El precio es excelente!\n");
    }else if (precioAceptable >precioEx && precioAceptable > precioCaro){
        printf("El precio es aceptable.\n");
    }else{
        printf("El precio es muy caro.\n");
    }
    
    
}
