class Hexagono(Figura):
    def __init__(self, lado):
        super().__init__("Hexagono")
        self.__lado = lado

    def get_lado(self):
        return self.__lado

    def calcular_area(self):
        return (3 * math.sqrt(3) / 2) * (self.__lado ** 2)

    def calcular_perimetro(self):
        return 6 * self.__lado