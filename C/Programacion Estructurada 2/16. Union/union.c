#include <stdio.h>
#include <string.h>
#include <ctype.h>

union proveedor{
	char razon[40];
	char cuit[20];
};

struct producto
{
	int clave;
	char nombre[50];
	int stock;
	union proveedor tipo;
};

int main(void)
{
	int i = 0,j =0, y;
	char x[50];
	int corriendo = 1;
	struct producto p[100];
	do
	{
		printf("Ingrese el nombre del producto que desea crear.\n");
		gets(p[i].nombre);
		fflush(stdin);
		printf("Ingrese la clave del producto (Valor Numerico)\n");
		scanf("%i", &p[i].clave);
		printf("Ingrese el stock del producto\n");
		scanf("%i", &p[i].stock);
		printf("Ingrese el tipo de proveedor (Mayorista/Minorista)\n");
		fflush(stdin);
		gets(x);
		strlwr(x);
		strcmp(x, "minorista") == 0 ?(printf("Ingrese la razon social:\n"), gets(p[i].tipo.razon)):(printf("Ingrese el CUIT:\n"), gets(p[i].tipo.cuit));

		fflush(stdin);
		printf("Desea terminar y mostrar todos los productos creados? \n1. Si 2. No\n");
		scanf("%i", &y);
		y == 1?corriendo = 0:i++;
		fflush(stdin);


	}while (corriendo && i < 100);

	for (j = 0; j <= i; j++)
	{
		printf("Nombre Producto %i: %s\n", j+1, p[j].nombre);
		printf("Clave Producto %i: %i\n", j+1, p[j].clave);
		printf("Stock Producto %i: %i\n", j+1, p[j].stock);
		printf("Identificador del Proveedor del Producto %i: %s\n\n", j+1, p[j].tipo);
	}


}
