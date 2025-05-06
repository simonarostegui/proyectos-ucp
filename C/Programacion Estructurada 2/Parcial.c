#include <stdio.h>

//Arostegui Simon
/* 
Una empresa de flete posee tres vehiculos en su flota. De cada uno de ellos guarda la siguiente informacion:
 * Marca
 * Modelo
 * Patente
 * Kilometraje Actual

Durante la semana (lunes a viernes) todos los vehiculos realizan fletes. Por cada dia se registra la cantidad de km realizados por cada uno de los vehiculos, de la siguiente manera:
 * Dia
 * Kilometros Vehiculo 1
 * Kilometros Vehiculo 2
 * Kilometros Vehiculo 3

Teniendo en cuenta que la empresa cobra por sus sevicios $1000 por km, se pide calcular la cantidad de dinero generado por cada vehiculo durante la semana y el total general. Esta informacion debera guardarse en un archivo y mostrar por pantalla el contenido de dicho archivo.

Debera crear un programa que permita:
* Guardar en un arreglo de registros los datos de los vehiculos (struct)
* Guardar en un arreglo de registros los movimientos diarios (struct)
* Calcular el ingreso por servicio generado por vehiculo y el total general
* Guardar los calculos en un archivo (file). Se debera guardar
  * Patente Vehiculo - Total generado por vehiculo
  * Total general
Mostrar por pantalla los datos guardados en el archivo (file).
*/

struct Vehiculo {
    char marca[20];
    char modelo[20];
    char patente[20];
    int kilometrajeActual;
};

struct Movimiento {
    int dia;
    int kilometrosVehiculo1;
    int kilometrosVehiculo2;
    int kilometrosVehiculo3;
};

int calcularIngreso(int kilometros);

int main(void)
{
    struct Vehiculo vehiculos[3];
    struct Movimiento movimientos[5];

    FILE *archivo = fopen("movimientos.txt", "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo");
        return 1;
    }

    printf("Ingrese los datos de los vehiculos:\n");
    for (int i = 0; i < 3; i++) {
        printf("Vehiculo %d:\n", i + 1);
        printf("Marca: ");
        gets(vehiculos[i].marca);
        fflush(stdin);  
        printf("Modelo: ");
        gets(vehiculos[i].modelo);
        fflush(stdin);
        printf("Patente: ");
        gets(vehiculos[i].patente);
        fflush(stdin);
        printf("Kilometraje Actual: ");
        scanf("%d", &vehiculos[i].kilometrajeActual);
        fflush(stdin);
    }

    fflush(stdin);
    printf("Ingrese los movimientos diarios:\n");
    for (int i = 0; i < 5; i++) {
        printf("Dia %d:\n", i + 1);
        printf("Kilometros Vehiculo 1: ");
        scanf("%d", &movimientos[i].kilometrosVehiculo1);
        printf("Kilometros Vehiculo 2: ");
        scanf("%d", &movimientos[i].kilometrosVehiculo2);
        printf("Kilometros Vehiculo 3: ");
        scanf("%d", &movimientos[i].kilometrosVehiculo3);
    }

    fprintf(archivo, "Patente - Total generado\n");
    printf("Patente - Total generado\n");
    for (int i = 0; i < 3; i++) {
        int totalKilometros = 0; // creado aca para que se reinicie el valor en cada iteracion
        for (int j = 0; j < 5; j++) {
            switch(i) {
                case 0:
                    totalKilometros += movimientos[j].kilometrosVehiculo1;
                    break;
                case 1:
                    totalKilometros += movimientos[j].kilometrosVehiculo2;
                    break;
                case 2:
                    totalKilometros += movimientos[j].kilometrosVehiculo3;
                    break;
            }
        }
        fprintf(archivo, "%s - $%d\n", vehiculos[i].patente, calcularIngreso(totalKilometros));
        printf("%s - $%d\n", vehiculos[i].patente, calcularIngreso(totalKilometros));
    }

    fclose(archivo);
}

int calcularIngreso(int kilometros) { 
    return kilometros * 1000;
}
