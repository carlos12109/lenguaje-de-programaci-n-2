#clase base: Figura
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"soy una figura: {self.nombre}")

#subclase 1: cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("cuadrado")
        self.lado = lado
    
    def area(self):
        return self.lado**2

#sub clase 2:triangulo
class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("cuadrado")
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base *self.altura)/2

#subclase 3:circulo
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio=radio
    
    def area(self):
        return 3.14 * (self.radio**2)
    

figuras = [Cuadrado(4), Triangulo(3,4), Circulo(5)]

for figura in figuras:
    figura.mostrar_nombre()

    print(f"area: {figura.area():.2f} unidades al cuadrado \n")
    print("=d"*30)