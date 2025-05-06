# La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO Y NO CÉNTRICO)
# La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
# Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.

nombre_barrio = input("Ingrese el nombre del barrio: ").lower()
ubicacion = input("Ingrese la ubicación del barrio (centrico/no centrico): ").lower()

if nombre_barrio[0] <= "m" and ubicacion == "centrico":
    print("El barrio está en la sección A")
else:
    print("El barrio está en la sección B")