# Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
# ■ Ingredientes comunes: Verduras y berenjena.
# ■ Ingredientes Receta 1: Lentejas y apio.
# ■ Ingredientes Receta 2: Morrón y Cebolla..
# Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

print("¿Qué tipo de receta desea? (Receta 1/2)")
receta = str(input()).lower()

match receta:
    case "1":
        print("Los ingredientes disponibles son:")
        print("1. Lentejas")
        print("2. Apio")
        print("3. Verduras")
        print("4. Berenjena")
    case "2":
        print("Los ingredientes disponibles son:")
        print("1. Morrón")
        print("2. Cebolla")
        print("3. Verduras")
        print("4. Berenjena")
    case _:
        print("Opción inválida")
        
ingredientes = []

for i in range(3):
    print(f"Ingrese el ingrediente {i+1}:")
    ingrediente = str(input()).capitalize()
    if ingrediente in ingredientes:
        print("El ingrediente ya está en la lista")
    else:
        ingredientes.append(ingrediente)

print("La receta elegida es:", receta)
print("Los ingredientes elegidos son:", ", ".join([str(ingrediente) for ingrediente in ingredientes])) #.join sacado de codedamn.com

