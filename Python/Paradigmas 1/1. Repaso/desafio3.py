# Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de fertilizantes.

porcentajeCompuesto = float(input("Ingrese el porcentaje de compuesto en el suelo:"))
tipoVegetacion = str(input("Existen matorrales en el terreno? (si/no)")).lower()

if tipoVegetacion == "si":
    print("No es factible la utilización de fertilizantes")
elif porcentajeCompuesto >= 10:
    print("Es factible la utilización de fertilizantes")
else:
    print("No es factible la utilización de fertilizantes")

