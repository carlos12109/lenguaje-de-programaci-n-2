#herencia

import math
class Rectangulo:
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color

    def area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)

    def mostrar_info(self):
        """Muestra la información del rectángulo."""
        print(f"Recantgulo de Base: {self.base}, Altura: {self.altura}, color {self.color}")
        print(f"Area: {self.area()}, Perimetro: {self.perimetro()}")

class Cuadrado (Recantgulo):
    def __init__(self, lado, color):
        super().__init__(lado, lado, color)
    def mostrar_info(self):
        """Muestra la información del cuadrado."""
        print(f"\nCuadrado de Lado: {self.base}, color {self.color}")
        print(f"Area: {self.area()}, Perimetro: {self.perimetro()}")


# Solicitar datos al usuario
print("rec 1: ")
a3=float(input("ingrese la base: "))
a4=float(input("ingrese la altura: "))
c=input("ingrese el color: ")

print("rec 2: ")
a5=float(input("ingrese la base: "))
a6=float(input("ingrese la altura: "))
b=input("ingrese el color: ")

rec_rojo = Rectangulo(a3, a4, c)
rec_rosado = Rectangulo(a5, a6, b)

ref1 = rec_rojo
ref2 = rec_rosado


print("----- Resultados -----")
ref1.mostrar_info()
print(f"area: {ref1.area():.2f} perimetro: {ref2.perimetro():.2f}")
ref2.mostrar_info()
print(f"area {ref2.area():.2f} peerimetro {ref2.perimetro():.2f}")