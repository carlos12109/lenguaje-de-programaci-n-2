from typing import TypeVar, Generic
import math

T = TypeVar('t', int, float)

class Pitagoras(Generic[T]):
    def __init__(self, cateto1: T, cateto2: T):
        self.a = cateto1
        self.b = cateto2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self.a ** 2 + self.b ** 2)

pitagoras_enteros = Pitagoras[int](3, 4)
pitagoras_decimales = Pitagoras[float](6.0, 2.5)
# Example usage
print("teorema dep itagoras: ")
print(f"hipotenusa entero: {pitagoras_enteros.calcular_hipotenusa()}")  # Output: 5
print(f"hipotenusa decimal: {+pitagoras_decimales.calcular_hipotenusa():.2f}")  # Output: 5.0
