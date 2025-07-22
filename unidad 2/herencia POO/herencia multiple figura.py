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

class dimension:
    def __init__(self, lado):
        self.lado =lado
    def mostrar_lado(self):
        print(f"lado : {self.lado}")

class Cuadrado(Figura, Colores, dimension):
    def __init__(self, nombre, color, lado):
        Figura.__init__(self, nombre)
        Colores.__init__(self, color)
        dimension.__init__(self, lado)

    def calcular_area(self):
        return self.lado**2

    def op_perimetro(self):
        resultado2 = self.base + self.lado + self.lado
        return f"el perimetro es: {resultado2}"
    
    def mostrar_todo(self):
        self.mostrar_nombre()
        self.mostrar_color()
        self.mostrar_lado()
        print(f"Area: {self.calcular_area()} unidades al cuadrado")

cuad= Cuadrado("cudrado", "azul", 6)
cuad.mostrar_todo()
