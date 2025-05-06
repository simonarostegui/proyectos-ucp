#include <stdio.h>
#include <stdlib.h> //rand
#include <string.h> //strcmp strcpy str todo
// #include <time.h> // rand seed
#include <ctype.h> // tolower

/*La empresa SYSTEMNEA SA necesita un sistema que le permita almacenar la siguiente información:

Trabajadores: apellido, nombre, año de ingreso, sexo, sueldo
Cliente: nombre, apellido, cuit, contacto
Proveedores: razón social, cuit, contacto
La información de contacto está compuesta por: dirección, teléfono, mail
Se pide elaborar una solución de permita:

cargar y mostrar los datos de clientes, proveedores y trabajadores.
listar los datos de clientes, proveedores y trabajadores.
seleccionar un trabajador y mostrar la antigüedad en la empresa.
informar el nombre de los empleados con salario por debajo del básico ($112500).
Informar la cantidad de trabajadoras del sexo femenino, y si se cumple con el cupo del 30% establecido por ley 27636
La edad promedio de los empleados
Mostrar los datos de contacto de un proveedor seleccionado
Mostrar los datos de contacto de un cliente seleccionado*/

struct trabajadores{
    char nombre[50];
    char apellido[50];
    int edad;
    int ingreso;
    int sexo;
    long int sueldo;
};

struct clientes{
    char nombre[50];
    char apellido[50];
    int sexo;
    long long int cuit;
    char direccion[100];
    long long int telefono;
    char mail[100];
};

struct proveedores{
    char razonSocial[100];
    long long int cuit;
    char direccion[100];
    long long int telefono;
    char mail[100];
};

int main(void)
{
    int i, estado =1, k = 0, generos = 0, sizeTrabajadores, sizeCliente, sizeProveedor;

    printf("\nTrabajadores\n\n");
    while (estado)
    {
        printf("Ingrese la cantidad de trabajadores que desea crear.\n");
        scanf("%i", &sizeTrabajadores);
        if (sizeTrabajadores <= 0){
            printf("La cantidad no puede ser menor a 1.\n");
        }else{
            break;
        }
    }
    struct trabajadores trabajador[sizeTrabajadores];
    for (i = 0; i < sizeTrabajadores; i++)
    {
        fflush(stdin);
        printf("Ingrese el nombre del empleado %i\n", i+1);
        gets(trabajador[i].nombre);
        printf("Ingrese el apellido del empleado %i\n", i+1);
        gets(trabajador[i].apellido);
        fflush(stdin);
        printf("Ingrese el sexo del empleado %i\n(Siendo 0 Masculino y 1 Femenino)\n",i+1);
        while (estado)
        {
            scanf("%i", &trabajador[i].sexo);
            if (trabajador[i].sexo == 0 || trabajador[i].sexo == 1)
            {
                break;
            }else
            {
                printf("Valor ingresado no reconocido. Intente denuevo.\n");
            }            
        }
        printf("Ingrese la edad del empleado %i\n",i+1);
        while (estado)
        {
            scanf("%i", &trabajador[i].edad);
            if (trabajador[i].edad > 18)
            {
                break;
            }else
            {
                printf("Su empleado no puede ser menor de edad.\n");
            }            
        }
        printf("Ingrese el a%co de ingreso del empleado %i\n", 164, i+1);
        while (estado)
        {
            scanf("%i", &trabajador[i].ingreso);
            if (trabajador[i].ingreso < 2024){
                break;
            }else{
                printf("Su empleado no puede viajar en el tiempo. Intente nuevamente.\n");
            }            
        }
        printf("Ingrese el sueldo mensual del empleado %i\n$", i+1);
        scanf("%li",&trabajador[i].sueldo);
        printf("\n");
    }

    printf("Clientes\n\n");
    while (estado)
    {
        printf("Ingrese la cantidad de clientes que desea crear.\n");
        scanf("%i", &sizeCliente);
        if (sizeCliente <= 0){
            printf("La cantidad no puede ser menor a 1.\n");
        }else{
            break;
        }
    }
    struct clientes cliente[sizeCliente];
    for (i = 0; i < sizeCliente; i++)
    {
        fflush(stdin);
        printf("Ingrese el nombre del cliente %i\n", i+1);
        gets(cliente[i].nombre);
        printf("Ingrese el apellido del cliente %i\n", i+1);
        gets(cliente[i].apellido);
        fflush(stdin);
        printf("Ingrese el sexo del cliente %i\n(Siendo 0 Masculino y 1 Femenino)\n",i+1);
        while (estado)
        {
            scanf("%i", &cliente[i].sexo);
            if (cliente[i].sexo == 0 || cliente[i].sexo == 1)
            {
                break;
            }else
            {
                printf("Valor ingresado no reconocido. Intente nuevamente.\n");
            }            
        }
        printf("Ingrese el CUIT del cliente %i\nEste debe ser ingresado sin guiones.\n", i+1);
        while (estado)
        {
            scanf("%lld", &cliente[i].cuit);
            if (cliente[i].cuit < 28000000000 && cliente[i].cuit > 20000000000){
                break;
            }else{
                printf("Su CUIT es incorrecto..\n");
            }            
        }
        fflush(stdin);
        printf("Ingrese la direccion del cliente %i\n", i+1);
        gets(cliente[i].direccion);
        printf("Ingrese el numero de telefono del cliente %i, junto al numero de area del mismo.\n", i+1);
        scanf("%lld", &cliente[i].telefono);
        fflush(stdin);
        printf("Ingrese el mail del cliente %i\n", i+1);
        gets(cliente[i].mail);
        fflush(stdin);
        printf("\n");
    }

    printf("Proveedores\n\n");
    
    while (estado)
    {
        printf("Ingrese la cantidad de proveedores que desea crear.\n");
        scanf("%i", &sizeProveedor);
        if (sizeProveedor <= 0){
            printf("La cantidad no puede ser menor a 1.\n");
        }else{
            break;
        }
    }
    struct proveedores proveedor[sizeProveedor];
    for (i = 0; i < sizeProveedor; i++)
    {
        fflush(stdin);
        printf("Ingrese el nombre del proveedor %i\n", i+1);
        gets(proveedor[i].razonSocial);
        fflush(stdin);
        printf("Ingrese el CUIT del proveedor %i\nEste debe ser ingresado sin guiones.\n", i+1);
        while (estado)
        {
            scanf("%lld", &proveedor[i].cuit);
            if (proveedor[i].cuit < 28000000000 && proveedor[i].cuit > 20000000000){
                break;
            }else{
                printf("Su CUIT es incorrecto..\n");
            }            
        }
        printf("Ingrese la direccion del proveedor %i\n", i+1);
        fflush(stdin);
        gets(proveedor[i].direccion);
        fflush(stdin);
        printf("Ingrese el numero de telefono del proveedor %i, junto al numero de area del mismo.\n", i+1);
        scanf("%lld", &proveedor[i].telefono);
        fflush(stdin);
        printf("Ingrese el mail del proveedor %i\n", i+1);
        gets(proveedor[i].mail);
        fflush(stdin);
        printf("\n");
    }

    printf("\nTRABAJADORES\n");
    for (int i = 0; i < sizeTrabajadores; i++) {
        printf("Empleado %d:\n", i + 1);
        printf("Nombre: %s\n", trabajador[i].nombre);
        printf("Apellido: %s\n", trabajador[i].apellido);
        if (trabajador[i].sexo == 0){ // Masculino
            printf("Sexo: Masculino\n");
        }else{ // Femenino
            printf("Sexo: Femenino\n");
        }
        printf("Edad: %d\n", trabajador[i].edad);
        printf("Ingreso: %d\n", trabajador[i].ingreso);
        printf("Sueldo: $%ld\n\n", trabajador[i].sueldo);
    }

    printf("\nCLIENTES\n");
     for (int i = 0; i < sizeCliente; i++) {
         printf("Cliente %d:\n", i + 1);
         printf("Nombre: %s\n", cliente[i].nombre);
         printf("Apellido: %s\n", cliente[i].apellido);
         printf("CUIT: %lld\n", cliente[i].cuit);
         printf("Direccion: %s\n", cliente[i].direccion);
         printf("Telefono: %lld\n", cliente[i].telefono);
         printf("Email: %s\n\n", cliente[i].mail);
     }

    printf("\nPROVEEDORES\n");
    for (int i = 0; i < sizeProveedor; i++) {
        printf("Proveedor %d:\n", i + 1);
        printf("Nombre: %s\n", proveedor[i].razonSocial);
        printf("CUIT: %lld\n", proveedor[i].cuit);
        printf("Direccion: %s\n", proveedor[i].direccion);
        printf("Telefono: %lld\n", proveedor[i].telefono);
        printf("Email: %s\n\n", proveedor[i].mail);
    }

    printf("Desea continuar?\n(Si/No)\n");
    char respuesta[5];
    gets(respuesta);
    for(i = 0; respuesta[i]; i++){
        respuesta[i] = tolower(respuesta[i]);
    }
    int numeroGuardado[10] = {};
    if (strcmp("si", respuesta) == 0){
        while (estado){        
            int valor, j;
            printf("Que desea hacer?\n1. Ver antiguedad en la empresa de un empleado.\n2. Ver los sueldos de los empleados y si son pagados justamente.\n3. Ver las estadisticas de genero de sus empleados.\n4. Ver la edad promedio de los empleados.\n0. Cerrar.\n");
            scanf("%d", &valor);
            switch (valor){
            case 1:
                printf("\nIngrese  el número de empleado que desea ver.");
                scanf("%d", &j);
                printf("El empleado %i ingreso a la empresa en el a%co %i.\n\n", j, 164, trabajador[j-1].ingreso);
                printf("Desea continuar?\n(1 = Si/ 0 = No)\n");
                scanf("%d", &j);
                if (j == 0)
                {
                    estado = 1; 
                }else
                {
                    break;
                }
            case 2:
                for (i = 0; i < sizeTrabajadores; i++)
                {
                    if (trabajador[i].sueldo < 112500)
                    {
                        numeroGuardado[k] = i+1;
                        k++;
                    }
                }
                if (k == 0){
                    printf("No se encontraron empleados con sueldos menores al salario minimo.\n");
                }else{
                    for (i = 0; i < k; i++)
                    {
                        printf("El empleado %i tiene un sueldo menor al salario minimo.\n", numeroGuardado[i]);
                    }
                    
                }
                printf("Desea continuar?\n(1 = Si/ 0 = No)\n");
                scanf("%d", &j);
                fflush(stdin);
                if (j == 0)
                {
                    estado = 0; 
                }else
                {
                    break;
                }
            case 3:
                for (i = 0; i < sizeTrabajadores; i++)
                {
                    if (trabajador[i].sexo == 1)
                    {
                        generos++;
                    }
                    
                }
                printf("Cantidad de Hombres: %i\nCantidad de Mujeres: %i\n", sizeTrabajadores-generos, generos);
                if (generos * 100 / sizeTrabajadores < 30){
                    printf("Su empresa contiene menos porcentaje de mujeres que el establecido por la ley 27636.\n");
                }else
                {
                    printf("Su empresa esta de acuerdo al porcentaje establecido por la ley 27636.\n");
                }
                printf("Desea continuar?\n(1 = Si/ 0 = No)\n");
                scanf("%d", &j);
                if (j == 0)
                {
                    estado = 0; 
                }else
                {
                    break;
                }

            default:
                estado = 0;
            }            
        }
    }

}



/* 
No me dio el tiempo de terminar
Originalmente cree este codigo con la intención de pedirle al usuario si quería generar el codigo automaticamente o no. Había creado el codigo entero y aprendí a usar operadores que antes no sabía solo para este codigo.
Pero una vez terminado y cuando empecé a hacer el codigo manual, aprendí que si declarás una estructura dentro de un if entonces solo se puede usar dentro de ese if sin importar si es llamado en todos los ifs.
La unica forma de arreglarlo seria utilizando punteros y malloc, pero todavía no se bien como usar punteros.
Este código tambien se puede usar para crear una lista aleatoria y luego hacer que el usuario añada o quite empleados o clientes a la lista. Pero no lo voy a hacer porque no tengo tiempo.

int main(void){
    srand(time(NULL));
    int i,estado = 0, sizeTrabajadores, sizeCliente, sizeProveedor;
    char respuesta[20];
    printf("Desea cargar los datos manualmente?\n(Si/No)\n");
    gets(respuesta);

    for(i = 0; respuesta[i]; i++){
        respuesta[i] = tolower(respuesta[i]);
    }

    if (strcmp("no", respuesta) == 0)
    {
        int randCantidad;
        char fNombreLista[13][30] = {"Eliana", "Lisa", "Karina", "Sofia", "Micaela", "Yanina", "Alejandra", "Daiana", "Joaquina", "Ludmila", "Oriana", "Carmen", "Silvana"};
        char hNombreLista[14][30] = {"Fernando", "Jorge", "Nicolas", "Matias", "Juan", "Enzo", "Rodrigo", "Miguel", "Pedro", "Ivan", "Gabriel", "Damian", "Fabian", "Angel"};
        char apellidoLista[13][40] = {"Rodriguez", "Fernandez", "Figueredo", "Ayala", "Cabrera", "Montero", "Porta", "Perani", "Acevedo", "Weiteder", "Riquelme", "Moreno", "Larretta"};
        char direccionesLista[13][50] = {"Gobernador Gutierrez", "Lavalle", "General Paz", "Elias Abbad", "San Juan", "Rivadavia", "Uruguay", "Roca", "Islas Malvinas", "Estado de Israel", "San Lorenzo", "Heroes Civiles", "Sarmiento"};
        char mailLista[4][50] = {"gmail.com", "hotmail.com", "outlook.live", "yahoo.com"};
        char empresaLista[7][50] = {"Casa Blanca SRL", "Los Pinos SA", "La Rosada SRL", "El Rojo SA", "El Tio", "Don Chelo", "Real Company"};
        char nombreLower[50], apellidoLower[50];
        //Estas listas estan diseñadas para ser llamadas dentro del codigo abajo. Generando un numero aleatorio dentro del rango de la matriz


        randCantidad = rand()%10+1;
        struct trabajadores trabajador[randCantidad];
        sizeTrabajadores = sizeof(trabajador)/sizeof(trabajador[0]);
        for (i = 0; i < sizeTrabajadores; i++)
        {
            trabajador[i].sexo = rand()%2;
            if (trabajador[i].sexo == 0){ // Masculino
                strcpy(trabajador[i].nombre, hNombreLista[rand()%14]);
            }else{ // Femenino
                strcpy(trabajador[i].nombre, fNombreLista[rand()%13]);
            }
            strcpy(trabajador[i].apellido, apellidoLista[rand()%13]);
            trabajador[i].ingreso = 2023-rand()%50;
            trabajador[i].sueldo = (rand()%(300000 - 100000+1)) + 100000;
        }
        
        struct clientes cliente[randCantidad];
        sizeCliente = sizeof(cliente)/sizeof(cliente[0]);
        for (i = 0; i < sizeCliente; i++)
        {
            cliente[i].sexo = rand()%2;
            if (cliente[i].sexo == 0){ // Masculino
                strcpy(cliente[i].nombre, hNombreLista[rand()%14]);
                cliente[i].cuit = 20000000000LL+((rand()%99999)*10000)+(rand()%9999);
            }else{ // Femenino
                strcpy(cliente[i].nombre, fNombreLista[rand()%13]);
                cliente[i].cuit = 27000000000LL+((rand()%99999)*10000)+(rand()%9999);
            }
            //El CUIT fue un poco complicado. Lo que está haciendo este codigo es concatenar un numero de 9 digitos aleatorio con el metodo de multiplicar el numero obtenido por 10k, entonces es movido arriba.
            //Generando este numero, aprendí que el rand() tiene un valor maximo de 25600, entonces mutiplicarlo y moverlo para arriba, y luego añadir otro set de numeros generados en los valores que son puestos en cero fue la solución.
            strcpy(cliente[i].apellido, apellidoLista[rand()%13]);
            char direccionRand[5];
            snprintf(direccionRand, sizeof(direccionRand), "%d", rand()%4000); // Genera un numero dentro de la variable direccionRand, convirtiendolo en string para luego ser añadido debajo
            snprintf(cliente[i].direccion, sizeof(cliente[i].direccion), "%s %s", direccionesLista[rand()%13], direccionRand); // Concatena dentro de cliente[i].direccion un valor aleatorio del 0-12 el cual agarra un nombre de calle y luego añade un numero al final, generado arriba.
            cliente[i].telefono = 3794000000 + rand()%999999 * 10 + rand()%10;
            for (int j = 0; cliente[i].nombre[j]; j++) {
                nombreLower[j] = tolower(cliente[i].nombre[j]);
            }
            nombreLower[strlen(cliente[i].nombre)] = '\0';
            for (int j = 0; cliente[i].apellido[j]; j++) {
                apellidoLower[j] = tolower(cliente[i].apellido[j]);
            }
            apellidoLower[strlen(cliente[i].apellido)] = '\0';
            snprintf(cliente[i].mail, sizeof(cliente[i].mail), "%s%s@%s", nombreLower, apellidoLower, mailLista[rand()%4]);
            //Generar un mail fue lo menos complicado, agarra el nombre dentro de las 2 variables puestas arriba y lo pone en toLower, añadiendo el valor nulo al final manualmente.
            //(No se por que no lo añadió directamente.)
        }

        struct proveedores proveedor[randCantidad];
        sizeProveedor = sizeof(proveedor)/sizeof(proveedor[0]);
        for (i = 0; i < sizeProveedor; i++)
        {
            strcpy(proveedor[i].razonSocial, empresaLista[rand()%7]);
            proveedor[i].cuit = 20000000000LL+((rand()%99999)*10000)+(rand()%9999);
            char direccionRand[5];
            snprintf(direccionRand, sizeof(direccionRand), "%d", rand()%4000); 
            snprintf(proveedor[i].direccion, sizeof(proveedor[i].direccion), "%s %s", direccionesLista[rand()%13], direccionRand);
            proveedor[i].telefono = 3794000000 + rand()%999999 * 10 + rand()%10;
            char empresaMail[50];
            char *empresaNombre = proveedor[i].razonSocial;
            int k=0;
            for (int j = 0; empresaNombre[j]; j++) {
                if (!isspace(empresaNombre[j])) {
                    empresaMail[k] = tolower(empresaNombre[j]);
                    k++;
                }
            }
            empresaMail[k] = '\0';
            snprintf(proveedor[i].mail, sizeof(proveedor[i].mail), "%s@%s", empresaMail, mailLista[rand()%4]);

        }

        estado++;
    }else if (strcmp("si", respuesta) == 0){
        printf("\nTrabajadores\n\n");
        printf("Ingrese la cantidad de trabajadores que desea crear.\n");
        scanf("%i", &sizeTrabajadores);
        struct trabajadores trabajador[sizeTrabajadores];
        for (i = 0; i < sizeTrabajadores; i++)
        {
            fflush(stdin);
            printf("Ingrese el nombre del empleado %i\n", i+1);
            gets(trabajador[i].nombre);
            printf("Ingrese el apellido del empleado %i\n", i+1);
            gets(trabajador[i].apellido);
            fflush(stdin);
            printf("Ingrese el sexo del empleado %i\n(Siendo 0 Masculino y 1 Femenino)\n",i+1);
            scanf("%i", &trabajador[i].sexo);
            printf("Ingrese el a%co de ingreso del empleado %i\n", 164, i+1);
            scanf("%i",&trabajador[i].ingreso);
            printf("Ingrese el sueldo mensual del empleado %i\n", i+1);
            scanf("%li",&trabajador[i].sueldo);
        }
        

    }else{
        printf("Valor no reconocido.");
    }

    printf("\nTRABAJADORES\n");
    for (int i = 0; i < sizeTrabajadores; i++) {
        printf("Empleado %d:\n", i + 1);
        printf("Nombre: %s\n", trabajador[i].nombre);
        printf("Apellido: %s\n", trabajador[i].apellido);
        if (trabajador[i].sexo == 0){ // Masculino
            printf("Sexo: Masculino\n");
        }else{ // Femenino
            printf("Sexo: Femenino\n");
        }
        printf("Ingreso: %d\n", trabajador[i].ingreso);
        printf("Sueldo: $%ld\n\n", trabajador[i].sueldo);
    }

    printf("\nCLIENTES\n");
    for (int i = 0; i < sizeCliente; i++) {
        printf("Cliente %d:\n", i + 1);
        printf("Nombre: %s\n", cliente[i].nombre);
        printf("Apellido: %s\n", cliente[i].apellido);
        printf("CUIT: %lld\n", cliente[i].cuit);
        printf("Direccion: %s\n", cliente[i].direccion);
        printf("Telefono: %lld\n", cliente[i].telefono);
        printf("Email: %s\n\n", cliente[i].mail);
    }

    printf("\nPROVEEDORES\n");
    for (int i = 0; i < sizeProveedor; i++) {
        printf("Proveedor %d:\n", i + 1);
        printf("Nombre: %s\n", proveedor[i].razonSocial);
        printf("CUIT: %lld\n", proveedor[i].cuit);
        printf("Direccion: %s\n", proveedor[i].direccion);
        printf("Telefono: %lld\n", proveedor[i].telefono);
        printf("Email: %s\n\n", proveedor[i].mail);
   }

}*/
