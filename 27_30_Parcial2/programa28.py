#/////////////////////////////////////////////////////////////////////////////////////////
class Laptop:
    def __init__(self, nombre, modelo, ram, procesador):
        self.nombre = nombre
        self.modelo = modelo
        self.ram = ram
        self.procesador = procesador
        self.teclado = None

    def encender(self):
        print("Encendiendo...")

    def apagar(self):
        print("Apagando...")

    def procesar(self):
        print("Procesando Datos")

    def describir(self):
        print("El nombre del siguiente equipo es: ", self.nombre, "de modelo", self.modelo,
              "cuenta con", self.ram, "memoria ram y un procesador", self.procesador)
        
        if self.teclado:
            print("Cuenta con un teclado de tamaño", self.teclado.tamaño)

    def colocar_teclado(self, teclado):
        self.teclado = teclado
    
    def agregar_periferico(self, periferico):
        print(self.nombre, self.modelo, "cuenta con un periferico", periferico.nombre, "de tipo",  periferico.tipo)

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
#Asociacion
class Tecnico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos_en_reparacion = []

    def añadir_lista(self, lap):
        self.equipos_en_reparacion.append(lap)
        print(lap.nombre, "añadido a la lista de reparacion de ", self.nombre)

    def listar_equipos(self):
        print(self.nombre, "cuenta con los siguientes equipos en reparacion: ")
        for lap in self.equipos_en_reparacion:
            print(lap.nombre, lap.modelo)
    

#/////////////////////////////////////////////////////////////////////////////////////////
#Composicion
class TecladoIntegrado:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    
    def describir(self):
        print("Cuenta con un teclado de tamaño: ", 
              self.tamaño)


#/////////////////////////////////////////////////////////////////////////////////////////
#Herencia
class Estado(Laptop):
    def __init__(self, nombre, modelo, ram, procesador, estado):
        super().__init__(nombre, modelo, ram, procesador)
        self.estado = estado

    def revisar(self):
        super().describir()
        print("Se encuentra en estado: ", self.estado) 
            

#/////////////////////////////////////////////////////////////////////////////////////////
#Dependencia
class Periferico:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def describir(self):
        print("Este periferico es", self.nombre, "y es de tipo", self.tipo)
#/////////////////////////////////////////////////////////////////////////////////////////

lap1 = Laptop("Huawei", "D14", "12GB", "Intel i5 11va")
lap2 = Laptop("Samsung", "Notebook X", "8GB", "Intel i7 12va")
lap3 = Laptop("Huawei", "D15", "16GB", "Ryzen 9")

print("----------------------------------------------------------------")
print("Nombre de la lap1: ", lap1.nombre)
print("Modelo de la lap2: ", lap2.modelo)
lap1.encender()

tienda = Tienda("Steren")

tienda.añadir_lista(lap1)
tienda.añadir_lista(lap2)
tienda.añadir_lista(lap3)

print("Steren cuenta con los siguientes equipos: ")
tienda.listar_equipos()

print("----------------------------------------------------------------")
tecnico = Tecnico("Raul")

tecnico.añadir_lista(lap1)
tecnico.añadir_lista(lap2)
tecnico.añadir_lista(lap3)
tecnico.listar_equipos()

print("-----------------------------------------------------------------")
teclado1 = TecladoIntegrado("60%")
teclado2 = TecladoIntegrado("80%")
teclado3 = TecladoIntegrado("75%")

lap1.colocar_teclado(teclado1)
lap2.colocar_teclado(teclado3)
lap3.colocar_teclado(teclado2)

lap1.describir()
lap2.describir()

print("-----------------------------------------------------------------")
estado1 = Estado("HP", "Omen", "16GB","Intel i7 11va",  "Obsoleto")

estado1.revisar()

print("-----------------------------------------------------------------")
periferico1 = Periferico("Asus Rog", "Mouse")
lap1.agregar_periferico(periferico1)

