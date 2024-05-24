u1 = float(input("Ingrese cualquier valor numerico: "))
u2 = float(input("Ingrese otro valor numerico: "))
u3 = float(input("Ingrese otro valor numerico: "))


if u1 > u2 and u1 > u3:
    mayor = u1
    print("El numero mayor es: ", mayor)
elif u2 > u1 and u2 > u3:
    mayor = u2
    print("El numero mayor es: ", mayor)
elif u3 > u1 and u3 > u2:
    mayor = u3
    print("El numero mayor es: ", mayor)
else:
    print("Los numeros son iguales")

