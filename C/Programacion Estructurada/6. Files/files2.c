#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE * divFile;
    char buff[255];
    if ((divFile = fopen("C:\\Users\\simon\\OneDrive\\Escritorio\\divisores.txt", "r")) ==NULL){ // Abre el archivo. Si este no abre correctamente, cierra el programa.
        printf("ERROR AL ABRIR EL ARCHIVO.\n");
        exit(1);    
    }
    
    while(fgets(buff, 255, divFile)){     // Lee linea por linea el archivo de texto, almacena dentro de variable buff.
        printf("%s", buff);
    }
    fclose(divFile);
}
