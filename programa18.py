productos = {
    "Switch" : 5000,
    "Router" : 15300,
    "Bobina Cable UTP" : 1000,
    "Switch Ruteable" : 18000,
    "Servidor" : 5000, 
    "Bobina Cable Serial" : 2500
}
for clave in productos:
    valor = productos[clave] 
    print(clave, ": $", valor)

for clave in productos:
    valor = productos[clave]
    descuento = 0.15

    productos[clave] = valor - (valor * descuento)

print("-----------------------------------------------")

for clave in productos:
    valor = productos[clave] 
    print(clave, ": $", valor)
    

    