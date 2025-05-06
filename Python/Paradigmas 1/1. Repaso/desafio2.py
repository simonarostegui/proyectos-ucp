# La  contaminación del agua es cualquier cambio químico, físico o biológico en la calidad del agua que tiene un efecto dañino en cualquier cosa viva que consuma ese agua. Cuando seres humanos beben el agua contaminada tienen a menudo problemas de salud. 
# La contaminación del agua se detecta en los laboratorios, donde pequeñas muestras de agua se analizan para diversos tipos de contaminantes. Los organismos vivos tales como pescados se pueden también utilizar para la detección de la contaminación del agua. Los cambios en su comportamiento o crecimiento nos demuestran, que el agua en la que viven está contaminada.
# Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
# * Tamaño Normal: Mensaje "Pez en buenas condiciones"
# * Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
# * Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
# * Tamaño sobredimensionado: Mensaje "Pez contaminado"

print("Ingrese el tamaño del pez:")
print("Opciones: normal, por debajo de lo normal, un poco por encima de lo normal, sobredimensionado")
tamanioPez = str(input()).lower()

if tamanioPez == "normal":
    print("Pez en buenas condiciones")
elif tamanioPez == "por debajo de lo normal":
    print("Pez con problemas de nutrición")
elif tamanioPez == "un poco por encima de lo normal":
    print("Pez con síntomas de organismo contaminado")
elif tamanioPez == "sobredimensionado":
    print("Pez contaminado")
else:
    print("Ingrese un tamaño válido")