# calculadora estadística genérica

from typing import TypeVar, Generic, List
import math

T = TypeVar('T', int, float)

class Estadistica(Generic[T]):
    def __init__(self, datos: List[T]):
        self.datos = datos

    def promedio(self) -> float:
        return sum(self.datos) / len(self.datos)

    def maximo(self) -> float:
        return max(self.datos)

    def minimo(self) -> float:
        return min(self.datos)

    def desviacion_estandar(self) -> float:
        prom = self.promedio()
        contador = [contador for contador in self.datos]
        varianza = sum((contador - prom) ** 2 for contador in self.datos) / (len(self.datos) - 1)
        return math.sqrt(varianza)
    
    def desviacion_estandar_poblacional(self) -> float:
        prom = self.promedio()
        contador = [contador for contador in self.datos]
        varianza = sum((contador - prom) ** 2 for contador in self.datos) / len(self.datos)
        return math.sqrt(varianza)

datos = [10, 20, 15, 25, 30]
estadistica = Estadistica(datos)

print("Calculadora estadistica generica:")
print(f"Promedio: {estadistica.promedio():.2f}")
print(f"Maximo: {estadistica.maximo()}")
print(f"Mainimo: {estadistica.minimo()}")
print(f"Desviacion estandar muestrar: {estadistica.desviacion_estandar():.2f}")
print(f"Desviacion estandar poblacional: {estadistica.desviacion_estandar_poblacional():.2f}")
