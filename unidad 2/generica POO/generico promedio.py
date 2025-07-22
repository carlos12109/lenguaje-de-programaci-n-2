from typing import TypeVar, Generic
import math

T = TypeVar('t', int, float)

class Pitagoras(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def calcular_promedio(self) -> float:
        return (self.a+self.b) / 2

promedio_entero= Pitagoras[int](8, 12)
promedio_decimal = Pitagoras[float](5.5, 7.3)

#########
print("promedio de 2 numeros: ")
print(f"promedio entero: {promedio_entero.calcular_promedio()}")
print(f"promedio decimal: {promedio_decimal.calcular_promedio():.2f}")
