class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def calcular_area(self):
        return math.pi * self.__radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio