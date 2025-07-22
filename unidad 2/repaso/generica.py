import math
from typing import TypeVar, Generic
T= TypeVar("T", int, float)
class OperacionMatematica(Generic[T]):
    def calcular(self,a:T,b:T)->T:
        raise NotImplementedError ("metodo calcular() no implementado")
class Suma(OperacionMatematica[T]):
    def calcular(self, a:T , b:T)->T:
        return math.sqrt(a**2+ b**2)

def main():
    operacion = Suma()
    num1=5
    num2=7
    resultado=operacion.calcular(num1,num2)

    print(f"cateto a, {num1} y {num2} cateto b: {resultado:.2f}")


    num3=5.5
    num4=7.9
    resultado=operacion.calcular(num1,num2)
    print(f"la suma de, {num3} y {num4} es: {resultado:.2f}")

if __name__ == "__main__":
    main()
