class CalculadoraBasica:
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2

    # Getters
    def obtener_numero1(self):
        return self._numero1

    def obtener_numero2(self):
        return self._numero2

    # Setters
    def establecer_numero1(self, nuevo_valor):
        self._numero1 = nuevo_valor

    def establecer_numero2(self, nuevo_valor):
        self._numero2 = nuevo_valor

    # Operaciones
    def suma(self):
        return self._numero1 + self._numero2

    def resta(self):
        return self._numero1 - self._numero2

    def multiplicacion(self):
        return self._numero1 * self._numero2

    def division(self):
        if self._numero2 != 0:
            return self._numero1 / self._numero2
        else:
            return "No se puede dividir entre cero"

    def mostrar_operaciones(self):
        print(f"Numero1: {self._numero1}")
        print(f"Numero2: {self._numero2}")
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicacion: {self.multiplicacion()}")
        print(f"Division: {self.division()}")

# Crear objeto de la calculadora con entrada por teclado
try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    calc = CalculadoraBasica(numero1, numero2)
    calc.mostrar_operaciones()

    print("\n-----Cambiando valores.-----")

    # Cambiar los números y mostrar las operaciones nuevamente
    print("\nCambiando los números:")
    nuevo_numero1 = float(input("Ingrese el nuevo primer numero: "))
    nuevo_numero2 = float(input("Ingrese el nuevo segundo numero: "))

    calc.establecer_numero1(nuevo_numero1)
    calc.establecer_numero2(nuevo_numero2)
    calc.mostrar_operaciones()
except ValueError:
    print("Error: Ingrese un numero valido.")