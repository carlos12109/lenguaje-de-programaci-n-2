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

class Cuadrado(Rectangulo):
    def __init__(self, lado, color):
        super().__init__(lado, lado, color)
    def mostrar_info(self):
        """Muestra la información del cuadrado."""
        print(f"\nCuadrado de Lado: {self.base}, color {self.color}")
        print(f"Area: {self.area()}, Perimetro: {self.perimetro()}")


r1 = Rectangulo(10, 5, "verde")
c1 = Cuadrado(7, "azul")

r1.mostrar_info()
c1.mostrar_info()
