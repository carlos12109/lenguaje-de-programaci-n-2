class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_nombre(self):
        print(f"figura: {self.nombre}")
class Colores:
    def __init__(self, color):
        self.color = color

    def mostrar_color(self):
        print(f"color: {self.color}")

class dimensiones:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mostrar_dimensiones(self):
        print(f"base : {self.base}")
        print(f"altura: {self.altura}")

class Triangulo(Figura, Colores, dimensiones):
    def __init__(self, nombre, color, base, altura):
        Figura.__init__(self, nombre)
        Colores.__init__(self, color)
        dimensiones.__init__(self, base, altura)

    def calcular_area(self):
        return (self.base * self.altura)/2

    def op_perimetro(self):
        resultado2 = self.base + self.lado + self.lado
        return f"el perimetro es: {resultado2}"
    
    def mostrar_todo(self):
        self.mostrar_nombre()
        self.mostrar_color()
        self.mostrar_dimensiones()
        print(f"Area: {self.calcular_area()} unidades al cuadrado")

tri= Triangulo("Triangulo", "azul", 6, 2)
tri.mostrar_todo()
