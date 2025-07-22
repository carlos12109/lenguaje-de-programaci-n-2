from typing import TypeVar, Generic

T = TypeVar('T', int, float)
class Collatz(Generic[T]):
    def _init_(self, numero: T):
        self.numero = numero
        if numero <= 0:
            raise ValueError("El número debe ser un entero positivo.")

    def secuencia(self) -> int:
        n = self.numero
        secuencia = [n]
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            secuencia.append(n)
        return secuencia

numero = int(input("Ingrese un número entero positivo: "))
collatz = Collatz[int](numero)
secuencia = collatz.secuencia()

print("\n========= CONJETURA DE COLLATZ =========")
print("Número inicial:", numero)
print("Secuencia:", secuencia)
print("-" * 45)