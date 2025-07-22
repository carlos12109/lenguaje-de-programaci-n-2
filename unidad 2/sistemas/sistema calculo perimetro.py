#calcular perimetros de figura con POLIMORFISMO
import math

# Clase base
class Figura:
    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

# Subclases
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 4 * self.lado
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

###### uso polimorfismo
figuras = [Cuadrado(5),Rectangulo(4, 7),Circulo(3)]

for figura in figuras:
    print(f"perimetro: {figura.calcular_perimetro():.2f}")

