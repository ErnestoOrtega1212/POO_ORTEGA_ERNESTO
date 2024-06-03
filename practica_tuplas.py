#Creación de Tuplas 
tupla1 = ("Ernesto", 18, "Estudiante", 4000)
tupla2 = ("OEAE050920HDGRDRA9", "3141230036")
tupla3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#Acceso a la posicion del elemento
print(tupla1[2])

#Concatenacion de tuplas
tupla_concatenada = tupla1 + tupla2

#Repeticion de tupla
tupla_repetida = tupla1 * 2

#Asignar elemenos de una tupla a diferentes variables

Nombre, Edad , Puesto, Sueldo = tupla1

#Mostrar valores de las tuplas
"""Cuantos elementos hay en la tupla"""
print(len(tupla1))

"""Solo valores numericos dentro de las tuplas"""
print(max(tupla3))
print(min(tupla3))
print(sum(tupla3))
