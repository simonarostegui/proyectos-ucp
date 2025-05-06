# Los insecticidas se usan para exterminar plagas de insectos. Actúan sobre larvas, huevos o insectos adultos. Uno de los insecticidas más usado fue el DDT, que se caracteriza por ser muy rápido. Trabaja por contacto y es absorbido por la cutícula de los insectos, provocándoles la muerte. Este insecticida puede mantenerse por 10 años o más en los suelos y no se descompone.
# En nuestro rol de Devs (Programador o Programadora de Software), debemos elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando insecticida en su plantación. Si hace 10 o más añoss, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".


años = int(input("Ingrese la cantidad de años que viene usando insecticida en su plantación: "))

if años >= 10:
    print("Por favor solicite revisión de suelos en su plantación")
elif años < 10:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación")
else:
    print("Ingrese un número válido")
