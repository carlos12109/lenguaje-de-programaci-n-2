
"""CLASS animal
felino
NOMBRE
edad
ESPECIE
color de pelaje

AVE
tipo de pico
NOMBRE
edad
ESPECIE
"""
class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_especie(self):
        return self.__especie

    def hacer_sonido(self):
        pass
    def mostrar_color_pelaje(self):
        return self.__color_pelaje
    def mostrar_tipo_pico(self):
        return self.__tipo_pico
    
    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Especie: {self.__especie},"
    
class Felino(Animal):
    def __init__(self, nombre, edad, especie, color_pelaje):
        super().__init__(nombre, edad, especie)
        self.__color_pelaje = color_pelaje

    def hacer_sonido(self):
        return "Grrr"

    def mostrar_info(self):
        return super().mostrar_info() + f" Color de pelaje: {self.__color_pelaje}, Sonido: {self.hacer_sonido()}"

class Ave(Animal):
    def __init__(self, nombre, edad, especie, tipo_pico):
        super().__init__(nombre, edad, especie)
        self.__tipo_pico = tipo_pico

    def hacer_sonido(self):
        return "Pío pío"

    def mostrar_info(self):
        return super().mostrar_info() + f" Tipo de pico: {self.__tipo_pico}, Sonido: {self.hacer_sonido()}"
    
def main():
    lista_animales = []
    while True:
        print("-----------------------------------------")
        print("             VETERINARIO VDM             ")
        print("-----------------------------------------\n")
        print("\n1. Registrar felino")
        print("2. Registrar ave")
        print("3. Mostrar todos los animales")
        print("4. Salir\n")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del felino: ")
            edad = input("Ingrese la edad del felino: ")
            especie = input("Ingrese la especie del felino: ")
            color_pelaje = input("Ingrese el color de pelaje del felino: ")
            f = Felino(nombre, edad, especie, color_pelaje)
            lista_animales.append(f)
            print("\nFelino registrado exitosamente.\n")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del ave: ")
            edad = input("Ingrese la edad del ave: ")
            especie = input("Ingrese la especie del ave: ")
            tipo_pico = input("Ingrese el tipo de pico del ave: ")
            a = Ave(nombre, edad, especie, tipo_pico)
            lista_animales.append(a)
            print("\nAve registrada exitosamente.\n")
        elif opcion == "3":
            if not lista_animales:
                print("\nNo hay animales registrados.\n")
            else:
                for animal in lista_animales:
                    print(animal.mostrar_info())
        elif opcion == "4":
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()