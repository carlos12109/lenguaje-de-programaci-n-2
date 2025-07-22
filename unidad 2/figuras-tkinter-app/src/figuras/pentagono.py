class Pentagono(Figura):
    def __init__(self, lado):
        super().__init__("Pentagono")
        self.__lado = lado

    def get_lado(self):
        return self.__lado

    def calcular_area(self):
        return (5 * self.__lado**2) / (4 * math.tan(math.pi / 5))

    def calcular_perimetro(self):
        return 5 * self.__lado