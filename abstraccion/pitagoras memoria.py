import sys
import math

class pitagoras:
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    def calcular_hipotenusa(self):
        return math.sqrt(self.cateto1**2 + self.cateto2**2)
        
triangulo=pitagoras(3, 4)

print("-----Calculadora de Pitagoras-----")
print(f"resultado de la hipotenusa: {triangulo.calcular_hipotenusa()}\n")
print("tamaños en memoria (bytes):") 

#tamaño de la variable triangulo
tamaño_objeto = sys.getsizeof(triangulo)
tamaño_objeto1 = sys.getsizeof(triangulo.cateto1)
tamaño_objeto2 = sys.getsizeof(triangulo.cateto2)
tamaño_total = sys.getsizeof(triangulo.calcular_hipotenusa())
total = sys.getsizeof(pitagoras)
print(f"objeto triangulo: {tamaño_objeto} bytes")
print(f"objeto  cateto 1: {tamaño_objeto1} bytes")
print(f"objeto  cateto 2: {tamaño_objeto2} bytes")
print(f"objeto  total: {tamaño_total} bytes")
print(f"tamaño de la clase: {total} bytes")

suma_total = tamaño_objeto + tamaño_objeto1+tamaño_objeto2 + tamaño_total + total
print(f"tamaño total de la clase: {suma_total} bytes")