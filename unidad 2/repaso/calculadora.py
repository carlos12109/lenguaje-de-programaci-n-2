from typing import TypeVar, Generic
T = TypeVar("T", int, float)
class OperacionMatematica(Generic[T]):
    def calcular(self, a: T, b: T) -> T:
        raise NotImplementedError("metodo calcular() no implementado")
class Suma(OperacionMatematica[T]):
    def calcular(self, a: T, b: T) -> T:
        return a + b
class Resta(OperacionMatematica[T]):
    def calcular(self, a: T, b: T) -> T:
        return a - b
class Division(OperacionMatematica[T]):
    def calcular(self, a:T, b:T)->T:
        if b ==0:
            raise ValueError("no se puede divir por cero")
        return a / b
class Multiplicacion(OperacionMatematica[T]):
    def calcular(self, a:T, b:T)->T:
        return a * b
def main():
    while True:
        print(5*"-","CALCULADORA",5*"-")
        print("1: Suma")
        print("2: resta")
        print("3: division")
        print("4: multiplicacion")
        print("5: salir")
        opcion = input("ingrese una opcion: ")
        if opcion == "1":
            operacion = Suma()
            num1 = int(input("ingrese valor a: "))
            num2 = int(input("ingrese valor b: "))
            resultado = operacion.calcular(num1,num2)
            print(f"la suma de {num1} + {num2} es: {resultado}")
        elif opcion=="2":
            operacion = Resta()
            num1 = int(input("ingrese valor a: "))
            num2 = int(input("ingrese valor b: "))
            resultado = operacion.calcular(num1,num2)
            print(f"la suma de {num1} + {num2} es: {resultado}")
        elif opcion=="3":
            operacion = Division()
            num1 = int(input("ingrese valor a: "))
            num2 = int(input("ingrese valor b: "))
            resultado = operacion.calcular(num1,num2)
            print(f"la suma de {num1} + {num2} es: {resultado}")
        elif opcion == "4":
            operacion = Multiplicacion()
            num1 = int(input("ingrese valor a: "))
            num2 = int(input("ingrese valor b: "))
            resultado = operacion.calcular(num1,num2)
            print(f"la suma de {num1} + {num2} es: {resultado}")
        elif opcion == "5":
            print("gracias")
            break
        else:
            print("\n Opcion no valida.")
if __name__ == "__main__":
    main()

