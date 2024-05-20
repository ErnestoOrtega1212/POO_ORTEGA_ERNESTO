peso = float(input("Ingrese el peso de su paquete(kg): "))


if peso <= 1:
    costo = 50

elif peso <= 5:
    costo = 100

elif peso <= 10:
    costo = 200

else:
    costo = 500

print("El costo de envio de su paquete sera de: ", "$",costo)