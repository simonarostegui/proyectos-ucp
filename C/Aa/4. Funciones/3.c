#include <stdio.h>
#include <stdlib.h>

/*Codificar un programa que permita simular la venta de entradas a un espectáculo. El
programa debe determinar el pago a realizar por las entradas que solicite un cliente,
considerando que:
• Se pueden comprar solo hasta 4 (cuatro) entradas por cliente.
• Si se compran dos entradas se descuenta el 10%,
• Si la compra es de tres entradas, se descuenta el 15%.
• Si la compra es de cuatro entradas se descuenta el 20%.
• Cada entrada tiene un valor de $450,00.*/

int descuento(int cantidad){
    int precio = 450, descontado;
    switch(cantidad){
    case 1:
        return precio;
    case 2:
        descontado = (precio * 10) / 100;
        return precio - descontado;
    case 3:
        descontado = (precio * 15) / 100;
        return precio - descontado;
    case 4:
        descontado = (precio * 20) / 100;
        return precio - descontado;
    default:
        if(cantidad > 4){
            descontado = (precio * 20) / 100;
            cantidad = cantidad -4;
            int x = descuento(cantidad);
            return x + (precio - descontado);
            /*Si es mayor a 4, realiza el descuento de 20% y quita 4 a la cantidad total, 
            luego realiza el descuento restante y lo acumula hasta que la cantidad sea la correcta.*/
        }else{
            break;
        }
    }
}

int main(void)
{
    int n;
    printf("Ingrese la cantidad de entradas que desea comprar:\n");
    scanf("%i", &n);

    int x = descuento(n);
    
    printf("El total con su descuento sera: $%i", x);
}
