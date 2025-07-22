import sys
import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + (self.base*2 + self.altura)*(1/2)
    
    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

triangulo = TrianguloRectangulo(3, 4)


print("---resultados---\n")
print(f"resultado del area: {triangulo.calcular_area()}")
print(f"resultado del perimetro: {triangulo.calcular_perimetro()}")
print(f"resultado de hipotenusa: {triangulo.calcular_hipotenusa()}\n")

#tamaño de la variable triangulo rectagulo

tamaño_objeto = sys.getsizeof(triangulo.calcular_area)
tamaño_objeto1 = sys.getsizeof(triangulo.calcular_perimetro)
tamaño_objeto2 = sys.getsizeof(triangulo.calcular_hipotenusa)
tamaño_objeto3 = sys.getsizeof(triangulo)
total = sys.getsizeof(TrianguloRectangulo)
print(f"objeto calcular area: {tamaño_objeto} bytes")
print(f"objeto  calcular perimetro: {tamaño_objeto1} bytes")
print(f"objeto  triangulo: {tamaño_objeto2} bytes")
print(f"objeto  hipotenusa: {tamaño_objeto3} bytes")
print(f"tamaño de la clase: {total} bytes")

suma_total = tamaño_objeto + tamaño_objeto1+tamaño_objeto2 + tamaño_objeto3+total
print(f"tamaño total de la clase: {suma_total} bytes")