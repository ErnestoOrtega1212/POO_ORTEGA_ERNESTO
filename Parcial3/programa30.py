#Programa una conexión a una base de datos en mysql usando la libreria mysql.connector que ejecuta algunas consultas por medio de un cursor (select, insert, delete, update) para comprobar su funcionamiento

#Programa 30 - Conexión a bd

import mysql.connector

host = "localhost"
usuario = "usuario"
contraseña = "contraseña"
base_de_datos = "nombre_de_la_base_de_datos"

try:
    conexion = mysql.connector.connect(
        host=host,
        user=usuario,
        password=contraseña,
        database=base_de_datos
    )
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    exit()

cursor = conexion.cursor()

#SELECT
cursor.execute("SELECT * FROM tabla_ejemplo")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}")

#INSERT
nuevo_registro = ("Nuevo Nombre", 25)
cursor.execute("INSERT INTO tabla_ejemplo (nombre, edad) VALUES (%s, %s)", nuevo_registro)
conexion.commit()
print("Registro insertado correctamente")

#UPDATE
cursor.execute("UPDATE tabla_ejemplo SET edad = 30 WHERE id = 1")
conexion.commit()
print("Registro actualizado correctamente")

#DELETE
cursor.execute("DELETE FROM tabla_ejemplo WHERE id = 2")
conexion.commit()
print("Registro eliminado correctamente")

cursor.close()
conexion.close()
