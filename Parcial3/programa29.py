#Programa que contenga un menú que llame a diferentes funciones que expliquen que son los conceptos de POO "Abstracción", "Encapsulamiento", "Herencia" y "Polimorfismo"

#Programa 29 - Principios de la POO

# Programa 29 - Principios de la POO

def mostrar_menu():
  """Muestra el menú de opciones."""
  print("\nMenú de Conceptos de POO:")
  print("1. Abstracción")
  print("2. Encapsulamiento")
  print("3. Herencia")
  print("4. Polimorfismo")
  print("5. Salir")

  opcion = input("Selecciona una opción (1-5): ")
  return opcion

def explicar_abstraccion():
  """Explica el concepto de Abstracción en POO."""
  print("\nAbstracción en POO:")
  print("La abstracción es un mecanismo que permite ocultar la complejidad interna de un objeto, exponiendo solo lo esencial para su uso.")
  print("Esto facilita el desarrollo y la comprensión del código, al enfocarse en la funcionalidad sin preocuparse por los detalles de implementación.")

def explicar_encapsulamiento():
  """Explica el concepto de Encapsulamiento en POO."""
  print("\nEncapsulamiento en POO:")
  print("El encapsulamiento se refiere a la agrupación de datos (atributos) y métodos (funciones) que operan sobre esos datos dentro de una única entidad llamada clase.")
  print("El encapsulamiento protege los datos de acceso no autorizado, permitiendo el control sobre cómo se modifican y acceden a ellos.")

def explicar_herencia():
  """Explica el concepto de Herencia en POO."""
  print("\nHerencia en POO:")
  print("La herencia es un mecanismo que permite crear nuevas clases (subclases) basadas en clases existentes (superclases).")
  print("Las subclases heredan los atributos y métodos de las superclases, permitiendo reutilizar código y crear jerarquías de clases.")

def explicar_polimorfismo():
  """Explica el concepto de Polimorfismo en POO."""
  print("\nPolimorfismo en POO:")
  print("El polimorfismo se refiere a la capacidad de un objeto de tomar diferentes formas o comportamientos según el contexto.")
  print("Esto permite que una misma función o método se comporte de manera diferente según el tipo de objeto al que se aplique.")

def main():
  """Función principal del programa."""
  while True:
    opcion = mostrar_menu()

    if opcion == "1":
      explicar_abstraccion()
    elif opcion == "2":
      explicar_encapsulamiento()
    elif opcion == "3":
      explicar_herencia()
    elif opcion == "4":
      explicar_polimorfismo()
    elif opcion == "5":
      print("Saliendo del programa...")
      break
    else:
      print("Opción inválida. Por favor, ingresa un número entre 1 y 5.")

if __name__ == "__main__":
  main()