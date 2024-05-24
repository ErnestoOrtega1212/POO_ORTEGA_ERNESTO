edades = [18, 20, 30, 15, 16, 31, 55, 11, 8, 3, 12, 12, 11]
menores = []
mayores = []
for i in edades:
    if i >= 18:
        mayores.append(i)
    else:
        menores.append(i)

print(mayores)
print(menores)