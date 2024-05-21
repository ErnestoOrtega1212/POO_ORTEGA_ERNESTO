

while True:
    print("Sumatoria de Números")
    num1 = float(input("Ingrese cualquier numero: "))
    num2 = float(input("Ingrese cualquier numero: "))

    suma = num1 + num2

    print(suma)

    print("Desea cerrar el programa? ")
    print("S) SI¨\n", "N) NO")

    cerrar = str(input())

    if cerrar == "N":
        "Programa cerrado con exito!"
        break
    else:
        print("El programa se ejecutara de nuevo")
