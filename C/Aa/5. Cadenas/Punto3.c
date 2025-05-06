#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void){
    int i;
    char palabra[50];
    char copia[50];
    char alverre[50];

    printf("Ingrese una palabra:\n");
    gets(palabra);

    strcpy(copia, palabra); // Copia en el caso que el usuario utilice mayusculas en su texto.
    while (palabra[i]){
        palabra[i] = tolower(palabra[i]); // Cambia palabra[] a minuscula,
        i++;
    }

    strcpy(alverre, palabra); // Copia palabra[] en minuscula a alverre[]
    strrev(alverre); // Reverse alverre[]
    int check = strcmp(palabra, alverre); // Compara las dos listas con strcmp.
    
    if(check == 0){
        printf("%s es palindromo.\n", copia);
    }else{
        printf("%s no es palindromo.\n", copia);
    }
}
