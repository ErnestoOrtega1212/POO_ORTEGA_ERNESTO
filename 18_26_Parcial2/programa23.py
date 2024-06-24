class Tecnologia:
    def __init__(self, nombre, modelo, ram, procesador):
        self.nombre = nombre
        self.modelo = modelo
        self.ram = ram
        self.procesador = procesador

    def encender(self):
        print("Encendiendo...")

    def apagar(self):
        print("Apagando...")

    def procesar(self):
        print("Procesando Datos")

lap1 = Tecnologia("Huawei", "D14", "12GB", "Intel i5 11va")
lap2 = Tecnologia("Samsung", "Notebook X", "8GB", "Intel i7 12va")
lap3 = Tecnologia("Huawei", "D15", "16GB", "Ryzen 9")

print(lap1.nombre)
print(lap2.modelo)
print(lap1.encender())

