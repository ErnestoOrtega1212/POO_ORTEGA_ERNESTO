import math
eleccion = ""

while eleccion != "d":
    print("Que deseas calcular el dia de hoy: ")
    print("a) Rectangulo")
    print("b) Triangulo")
    print("c) Cuadrado") 
    print("d) Salir") 
    eleccion = str(input())
    if eleccion == "a":
        print("Dame la medida de la base de tu rectangulo: ")
        b = float(input())
        print("Dame la medida de la altura de tu rectangulo: ")
        h = float(input())
        area_rectangulo = b * h
        
        print("El area del rectangulo es: ", area_rectangulo)
    elif eleccion == "b":
        print("Dame la medida de la base del triangulo: ")
        b = float(input())
        print("Dame la medida de la altura del triangulo: ")
        h = float(input())
        area_triangulo = b * h / 2

        print("El area del triangulo es de : ", area_triangulo)
        
    elif eleccion == "c":
        print("Dame la medida del lado de tu cuadrado: ")
        l = float(input())
        area_cuadrado = l * l 

        print("El area de tu circulo es de: ", area_cuadrado)
        
