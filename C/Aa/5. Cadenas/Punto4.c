#include <stdio.h>
#include <string.h>

int main(void){
    char password[30];
    char preset[30] = "contrasena123";
    for(int cont = 3; cont > 0; cont--){
        printf("Ingrese su contrase%ca:\n", 164); // 164 es el valor de la ñ
        gets(password);

        int a = strcmp(preset, password);
        if(a == 0){
            printf("Bienvenido!");
            break; // No dice que realice una función al finalizar, asi que solamente rompe el bucle.
        }else{
            if(cont > 1){
                printf("Intente nuevamente. Numero de intentos restantes: %i\n\n\n", cont-1);
            }else{
                printf("Numero de intentos excedido. Intente nuevamente mas tarde.\n\n"); // Teoricamente este codigo te mandaría a la misma pagina que si hubieras puesto la contraseña correcta, pero eso es por falta de conclusión.
            }
        }
    }
}
