
while True:
    print("Que conversion de temperatura quieres haacer? ")
    print("a) Celcius a Farenheit")
    print("b) Farenheit a Celcius")
    print("c) Cerrar programa \n")
    print("Ingresa de manera correcta el inciso\n")

    eleccion = str(input())

    if eleccion == "a":
        usuario = float(input("Ingrese los Celsius que decida convertir: \n"))        
        Farenheit = (usuario * 9 / 5) + 32
        print(Farenheit)
    
    elif eleccion == "b":
        usuario = float(input("Ingrese los Farenheit que quiera convertir: \n"))
        Celcius = (usuario - 32) * 5 / 9
        print(Celcius)
    
    elif eleccion == "c":
        break
    else:
        print("No ingresaste una opcion dentro del menú")
        
