peso = float(input("Ingrese su peso (kg): "))

estatura = float(input("Ingrese su estatura (m): "))

imc = round(peso / (estatura ** 2), 2)

print("Su indice de masa corporal es: ", imc)