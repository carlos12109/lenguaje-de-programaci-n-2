from typing import TypeVar, Generic
import math

T = TypeVar('t', int, float)

class Pitagoras(Generic[T]):
    def __init__(self, a: T):
        self.a = a


    def potencia(self) -> float:
        return self.a ** 2
    
    def raiz(self)-> float:
        if self.a > 0:
            return math.sqrt(self.a)
        else:
            print(f"{self.a} ERROR ingrese un numero positivo")
    
    def logaritmo(self) -> float:
        if self.a > 0:
            return math.log(self.a)
        else:
            print(f"{self.a} ERROR ingrese un numero positivo")
    
    def funcion_seno(self) -> float:
        return math.sin(self.a)
    
    def  funcion_coseno(self) -> float:
        return math.cos(self.a)
    
    def funcion_tangente(self) -> float:
        return math.tan(self.a)

resul_entero = Pitagoras[int](-3)
resul_decimal = Pitagoras[float](6.0)
# Example usage
print("-----POTENCIA-----")
print(f"resultado con entero: {resul_entero.potencia()}")
print(f"resultado con decimal: {resul_decimal.potencia():.2f}")
print("\n")

print("-----RAIZ-----")
print(f"resultado con entero: {resul_entero.raiz()}")
print("\n")

print("-----LOGARITMO-----")
print(f"resultado con entero: {resul_entero.logaritmo()}")
print("\n")

print("-----SENO-----")
print(f"resultado con entero: {resul_entero.funcion_seno()}")
print(f"resultado con decimal: {resul_decimal.funcion_seno():.4f}")
print("\n")

print("-----COSENO-----")
print(f"resultado con entero: {resul_entero.funcion_coseno()}")
print(f"resultado con decimal: {resul_decimal.funcion_coseno():.4f}")
print("\n")

print("---TANGENTE-----")
print(f"resultado con entero: {resul_entero.funcion_tangente()}")
print(f"resultado con decimal: {resul_decimal.funcion_tangente():.4f}")
print("\n")