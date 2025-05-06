#include <stdio.h>
#include <string.h>
/* Elaborar un programa en lenguaje c que permita generar el usuario y contraseña de logueo para
una plataforma. Se deberá tener la cuenta lo siguiente:
• El nombre de usuario tendrá una longitud mínima de 8 caracteres y máxima de 10.
• La contraseña tendrá una longitud total de 8 caracteres. Deberá comenzar con una letra
en mayúscula y contener al menos un número y uno de los siguientes símbolos: -
!#$%&()*?/@_.
• Guardar el usuario y contraseña en un archivo de texto llamado "usuarios.txt".*/

int main() {
    FILE *archivo;
    archivo = fopen("usuarios.txt", "w");

    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    char usuario[11];
    char contrasena[9];
    int tiene_mayuscula = 0, tiene_numero = 0, tiene_simbolo = 0;
    const char *simbolos = "-!#$%&()*?/@_";
    
    printf("Ingrese el nombre de usuario (8-10 caracteres): ");
    scanf("%s", usuario);

    printf("Ingrese la contrase%ca (8 caracteres, may%cscula inicial, al menos un n%cmero y un s%cmbolo: -!#$%%&()*?/@_): ", 164, 163, 163, 161);
    scanf("%s", contrasena);


    if (contrasena[0] >= 'A' && contrasena[0] <= 'Z') {
        tiene_mayuscula = 1;
    }

    for (int i = 0; i < 8; i++) {
        if (contrasena[i] >= '0' && contrasena[i] <= '9') {
            tiene_numero = 1;
        }
        if (strchr(simbolos, contrasena[i]) != NULL) {
            tiene_simbolo = 1;
        }
    }

    if (!tiene_mayuscula || !tiene_numero || !tiene_simbolo) {
        printf("Error: La contrase%ca no cumple con los requisitos.\n", 164);
        return 1;
    }

    if (strlen(usuario) < 8 || strlen(usuario) > 10 || strlen(contrasena) != 8) {
        printf("Error: Longitud inv%clida.\n", 160);
        return 1;
    }

    fprintf(archivo, "Usuario: %s\n", usuario);
    fprintf(archivo, "Contrase%ca: %s\n", 164, contrasena);

    fclose(archivo);

    return 0;
}
