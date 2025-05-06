#include <stdio.h>

/*
Implementar una funcion llamada calcularEdadFutura que reciba la edad actual de una persona y el numero de años a futuro como parametro por valor. Esta funcion debe calcular la edad futura de la persona sin modificar la edad actual.
Implementar una funcion llamada ajustarEdad que reciba por referencia la edad actual de la persona y le sume 2 años, modificando la edad directamente.
El programa principal debe:
Pedir al usuario que ingrese su edad actual y el numero de años a futuro.
Calcular la edad futura usando calcularEdadFutura (por valor).
Mostrar si la edad se modificó.
Llamar a ajustarEdad(por referencia)
Mostrar la nueva edad.
*/

void calcularEdadFutura(int edadActual, int añosFuturos, int *edadFutura) { // calc
    *edadFutura = edadActual + añosFuturos;
}

void ajustarEdad(int *edadActual) {
    *edadActual += 2;
}

int main()
{
    int edadActual, añosFuturos, edadFutura;

    printf("Ingrese su edad actual: ");
    scanf("%d", &edadActual);
    printf("Ingrese el numero de años a futuro: ");
    scanf("%d", &añosFuturos);

    calcularEdadFutura(edadActual, añosFuturos, &edadFutura);
    printf("La edad futura es: %d\n", edadFutura);
    return 0;
}
