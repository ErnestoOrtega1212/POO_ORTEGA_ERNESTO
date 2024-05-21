contraseña_c = "POO123"

while True:

    usuario = str(input("Ingrese su contraseña: "))

    if usuario == contraseña_c:
        print("Contraseña Correcta!")
        break
    else:
        print("Contraseña Invalida")