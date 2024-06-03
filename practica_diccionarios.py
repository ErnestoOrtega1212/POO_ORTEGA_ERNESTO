
#Crear diccionarios con llaves
diccionario = {
    "Nombre" : "Ana",
    "Edad" : 23,
    "Grupo" : "A"
}
print(diccionario)

#Crear diccionarios por parentesis
diccionario = dict(Nombre = "Ernesto", Edad = 25, Grupo = "A")

#Acceder al dato
print(diccionario["Nombre"])

#Modificar valor
diccionario["Nombre"] = "Carlos"
print(diccionario["Nombre"])

#Añadir un nuevo par (clave y valor)
diccionario["Carrera"] = "TI"
print(diccionario)

#Eliminar un par 
del diccionario["Carrera"]
print(diccionario)

#Imprimir todas las claves del diccionario 
keys = diccionario.keys()
print(keys)

#Imprimir todos los valores del diccionario 
values = diccionario.values()
print(values)

#Mostrar todas las claves y valores del diccionario
items = diccionario.items()
print(items)