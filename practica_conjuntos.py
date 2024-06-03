#Crear conjunto
conjunto1 = {True, 10, 2,  "Ernesto", "Benita", "Flores"}

conjunto2 = {False, "Flor", "A"}
#Agregar valor
conjunto1.add(15)

#Eliminar valor
conjunto1.remove(True)
"""Metodo mas seguro de eliminar elementos
para evitar excepciones"""
conjunto1.discard(2)

#Union de conjuntos
union = conjunto1 | conjunto2
union = conjunto1.union(conjunto2)

#Interseccion de conjuntos
interseccion = conjunto1 & conjunto2
interseccion = conjunto1.intersection(conjunto2)

#Diferiencia de Conjuntos
diferiencia = conjunto1 - conjunto2
diferiencia = conjunto1.difference(conjunto2)

#Mostrar conjuntos
print(len(conjunto1))
"""Verificar si un elemento esta en el conjunto"""
print("Ernesto" in conjunto1)

#Limpiar un conjunto 
conjunto1.clear()

#Realizar una copia superficial del conjunto
conjunto1.copy()

