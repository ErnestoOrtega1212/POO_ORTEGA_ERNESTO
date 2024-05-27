edades = [5, 10, 10, 18, 20, 40, 32, 41, 12, 
          45, 50, 11, 5, 1, 3, 4, 5, 30, 41,
           7, 8, 12, 16, 17, 19, 20, 22, 17]

Adultos = 0
Jovenes = 0
Adolescentes = 0
Infancia = 0
Maternal = 0

for edad in edades:
    if edad >= 27:
        Adultos += 1

    elif edad >= 18:
        Jovenes += 1

    elif edad >= 12:
        Adolescentes += 1

    elif edad >= 6:
        Infancia += 1
    else:
        Maternal += 1
print(edades)
print("Hay", Adultos, "Adultos")
print("Hay", Jovenes, "Jovenes")
print("Hay", Adolescentes, "Adolescentes")
print("Hay", Infancia, "Infantiles")
print("Hay", Maternal, "en Maternal")
