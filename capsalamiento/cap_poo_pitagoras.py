import math

class circulo:
    def __init__(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return math.pi * (self.__radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio

    #setter para area
    def set_radio(self, nuevo_radio):
        if nuevo_radio > 0:
            self.__radio = nuevo_radio

    def mostrar_resultados(self):
        print(f"El radio del circulo es: {self.__radio}")
        print(f"El area del circulo es: {self.calcular_area()}")
        print(f"El perimetro del circulo es: {self.calcular_perimetro()}")

#metodos
cir=circulo(4)
cir.mostrar_resultados()

print("\n-----MODIFICADO-----")
cir.set_radio(6)
cir.mostrar_resultados()
