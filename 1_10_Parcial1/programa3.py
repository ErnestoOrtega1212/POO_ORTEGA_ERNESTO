peso = float(input("Ingrese su peso en (kg): "))

estatura = float(input("Ingrese su estatura en (m): "))

imc = round(peso / (estatura ** 2), 2)

print("Su índice de masa corporal es: ", imc)


