#herencias circulo
import math
class Figura:
    def __init__(self, color):
        self.color = color

    def mostrar_info(self):
            print(f"color de la figura: {self.color}")


#herencia
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)
        
    def perimetro(self):
        return 2 * math.pi * self.radio

    #mostrar informacion
    def mostrar_info(self):
        
        print(f"\nRadio del circulo: {self.radio}, color: {self.color}")
        print(f"Area: {self.area():.2f}, Perimetro: {self.perimetro():.2f}")

r1 = Figura("rojo")
r2 = Circulo("azul", 3)

r1.mostrar_info()
r2.mostrar_info()