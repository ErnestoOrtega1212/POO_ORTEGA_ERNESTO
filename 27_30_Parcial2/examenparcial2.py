#/////////////////////////////////////////////////////////////////////////////////////////
class Laptop:
    def __init__(self, nombre, modelo, ram, procesador):
        self.nombre = nombre
        self.modelo = modelo
        self.ram = ram
        self.procesador = procesador
        self.teclado = None
        self.cliente = None

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
        
        if self.cliente:
            print("Equipo adquirido por:", self.cliente.nombre)

    def colocar_teclado(self, teclado):
        self.teclado = teclado
    
    def agregar_periferico(self, periferico):
        print(self.nombre, self.modelo, "cuenta con un periferico", periferico.nombre,  periferico.modelo)

    def mostrar_cantidad(self, disponibilidad):
        print(self.nombre, self.modelo, "cuenta con" ,disponibilidad.cantidad, "ejemplares disponibles")

    def agregar_compra(self, cliente):
        self.cliente = cliente

    

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
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

    def describir(self):
        print("Este periferico es de", self.nombre, "y es de modelo", self.modelo)
#/////////////////////////////////////////////////////////////////////////////////////////
#EXTRA 1
#DEPENDENCIA
class Disponibilidad:
    def __init__(self, cantidad):
        self.cantidad = cantidad
    
    def mostrar(self):
        print("Contamos con", self.cantidad, "disponibles de este equipo")
#/////////////////////////////////////////////////////////////////////////////////////////
#EXTRA 2
#COMPOSICION
class Comprador:
    def __init__(self, nombre, compra):
        self.nombre = nombre
        self.compra = compra

    def agregar_compra(self):
        print(self.compra, "fue adquirido por", self.nombre)


#/////////////////////////////////////////////////////////////////////////////////////////
#OBJETOS NECESARIOS
lap1 = Laptop("Huawei", "D14", "12GB", "Intel i5 11va")
lap2 = Laptop("Samsung", "Notebook X", "8GB", "Intel i7 12va")
lap3 = Laptop("Huawei", "D15", "16GB", "Ryzen 9")

teclado1 = TecladoIntegrado("60%")
teclado2 = TecladoIntegrado("80%")
teclado3 = TecladoIntegrado("75%")

cantidad_D14 = Disponibilidad(10)
cantidad_D15 = Disponibilidad(20)
cantidad_Note = Disponibilidad(11)

cliente1 = Comprador("Carlos", "Huawei D14")
cliente2 = Comprador("Melanie", "Huawei D15")
cliente3 = Comprador("Sarah", "Notebook X")

mouse1   = Periferico("Logitech", "G305")
headset1 = Periferico("Astro", "A10")
micro1   = Periferico("Shure", "SM27B")


#MENU INTERACTIVO:

def menu_principal():
    while True:
        print("✿ -------------------- STEREN MENÚ----------------------- ✿\n")
        print("Seleccione la operacion que desea realizar:")
        print("A) Adquirir producto")
        print("B) Disponibilidad de producto")
        print("C) Comprar Periferico")
        print("D) Salir")
        usuario = (input())

        if usuario == "A":
            submenu_a()

        elif usuario == "B":
            submenu_b()

        elif usuario == "C":
            submenu_c()

        elif usuario == "D":
            print("Finalizando programa")
            break
        else:
            print("El valor ingresado no esta dentro de las opciones disponibles")

def submenu_a():
    while True:
        print("✿ -------------------- COMPRAS MENÚ ----------------------- ✿")
        print("\nQue equipo desea adquirir: ")
        print("A) Huawei D14")
        print("B) Samsung Notebook X" )
        print("C) Huawei D15")
        print("D) Volver al Menu Principal")
        usuario_submenu_a = input()

        if usuario_submenu_a == "A":
            lap1.agregar_compra(cliente1)
            lap1.describir()
                   
        elif usuario_submenu_a == "B":
            lap2.agregar_compra(cliente2)
            lap2.describir()

        elif usuario_submenu_a == "C":
            lap3.agregar_compra(cliente3)
            lap3.describir()   

        elif usuario_submenu_a == "D":
            print("Finalizando proceso...")
            break
        else:
            print("El valor ingresado no esta dentro de las opciones disponibles")

def submenu_b():
    while True:
        print("✿ -------------------- DISPO MENÚ----------------------- ✿")
        print("\nQue equipo desea ver su disponibilidad: ")
        print("A) Huawei D14")
        print("B) Samsung Notebook X" )
        print("C) Huawei D15")
        print("D) Volver al Menu Principal")
        usuario_submenu_b = input()

        if usuario_submenu_b == "A":
            lap1.mostrar_cantidad(cantidad_D14)
                   
        elif usuario_submenu_b == "B":
            lap2.mostrar_cantidad(cantidad_D15)

        elif usuario_submenu_b == "C":
            lap3.mostrar_cantidad(cantidad_Note) 

        elif usuario_submenu_b == "D":
            print("Finalizando proceso...")
            break
        else:
            print("El valor ingresado no esta dentro de las opciones disponibles")

def submenu_c():
    while True:
        print("✿ -------------------- PERIF MENÚ----------------------- ✿")
        print("\nQue tipo de periferico desea adquirir: ")
        print("A) Mouse")
        print("B) Headset" )
        print("C) Micrófono")
        print("D) Volver al Menu Principal")
        usuario_submenu_c = input()

        if usuario_submenu_c == "A":
            mouse1.describir()
            print("Añadido a la lista de compras con un precio de $", 900)       
        elif usuario_submenu_c == "B":
            headset1.describir()
            print("Añadido a la lista de compras con un precio de $", 700) 
        elif usuario_submenu_c == "C":
            micro1.describir()
            print("Añadido a la lista de compras con un precio de $", 8500 ) 
        elif usuario_submenu_c == "D":
            print("Finalizando proceso...")
            break
        else:
            print("El valor ingresado no esta dentro de las opciones disponibles")

menu_principal()