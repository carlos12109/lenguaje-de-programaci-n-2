#Sistema de figuras geométricas
#Aplicando: Encapsulamiento, Herencia, Polimorfismo

import math
class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def mostrar_info(self):
        print(f"Figura: {self.__nombre}")
        print(f"Area: {self.calcular_area()}")
        print(f"Perimetro: {self.calcular_perimetro()}")

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.__radio = radio
    def get_radio(self):
        return self.__radio
    def calcular_area(self):
        return math.pi * self.__radio**2
    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectangulo")
        self.__base = base
        self.__altura = altura
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def calcular_area(self):
        return self.__base * self.__altura
    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__("Triangulo")
        self.__base = base
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    def calcular_area(self):
        return (self.__base * self.__altura) / 2
    def calcular_perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

class Pentagono(Figura):
    def __init__(self, lado, apotema):
        super().__init__("Pentagono")
        self.__lado = lado
        self.__apotema = apotema
    def calcular_area(self):
        perimetro = 5 * self.__lado
        return (perimetro * self.__apotema) / 2
    def calcular_perimetro(self):
        return 5 * self.__lado

class Hexagono(Figura):
    def __init__(self, lado, apotema):
        super().__init__("Hexagono")
        self.__lado = lado
        self.__apotema = apotema
    def calcular_area(self):
        perimetro = 6 * self.__lado
        return (perimetro * self.__apotema) / 2
    def calcular_perimetro(self):
        return 6 * self.__lado

def main():
    lista_figuras = []
    while True:
        print("\n **SISTEMA DE FIGURAS**")
        print("1. Registrar Circulo")
        print("2. Registrar Rectangulo")
        print("3. Registrar Triangulo")
        print("4. Registrar Pentagono")
        print("5. Registrar Hexagono")
        print("6. Mostrar todas las figuras")
        print("7. Salir")

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            radio = float(input("Ingrese radio del circulo: "))
            c = Circulo(radio)
            lista_figuras.append(c)
            print("Circulo registrado")

        elif opcion == "2":
            base = float(input("Base del rectangulo: "))
            altura = float(input("Altura del rectangulo: "))
            r = Rectangulo(base, altura)
            lista_figuras.append(r)
            print("Rectangulo registrado")

        elif opcion == "3":
            base = float(input("Base del triangulo: "))
            altura = float(input("Altura del triangulo: "))
            lado1 = float(input("Lado 1 del triangulo: "))
            lado2 = float(input("Lado 2 del triangulo: "))
            lado3 = float(input("Lado 3 del triangulo: "))
            t = Triangulo(base, altura, lado1, lado2, lado3)
            lista_figuras.append(t)
            print("Triangulo registrado")

        elif opcion == "4":
            lado = float(input("Lado del pentagono: "))
            apotema = float(input("Apotema del pentagono: "))
            p = Pentagono(lado, apotema)
            lista_figuras.append(p)
            print("Pentagono registrado")

        elif opcion == "5":
            lado = float(input("Lado del hexagono: "))
            apotema = float(input("Apotema del hexagono: "))
            h = Hexagono(lado, apotema)
            lista_figuras.append(h)
            print("Hexagono registrado")

        elif opcion == "6":
            if len(lista_figuras) == 0:
                print("No hay figuras registradas")
            else:
                for f in lista_figuras:
                    f.mostrar_info()

        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()