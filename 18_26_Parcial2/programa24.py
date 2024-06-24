#/////////////////////////////////////////////////////////////////////////////////////////
class Laptop:
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

#/////////////////////////////////////////////////////////////////////////////////////////

#Agregacion
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.Laptops = []

    def añadir_lista(self, lap):
        self.Laptops.append(lap)
        print(lap.nombre, "añadido a la lista de productos de ", self.nombre) 

    def listar_equipos(self):
        print(self.nombre, "cuenta con los siguientes equipos :")
        for lap in self.Laptops:
            print(lap.nombre, lap.modelo)   

#/////////////////////////////////////////////////////////////////////////////////////////

lap1 = Laptop("Huawei", "D14", "12GB", "Intel i5 11va")
lap2 = Laptop("Samsung", "Notebook X", "8GB", "Intel i7 12va")
lap3 = Laptop("Huawei", "D15", "16GB", "Ryzen 9")

print("Nombre de la lap1: ", lap1.nombre)
print("Modelo de la lap2: ", lap2.modelo)
lap1.encender()

tienda = Tienda("Steren")

tienda.añadir_lista(lap1)
tienda.añadir_lista(lap2)
tienda.añadir_lista(lap3)

print(f"Steren cuenta con los siguientes equipos: \n")
tienda.listar_equipos()



