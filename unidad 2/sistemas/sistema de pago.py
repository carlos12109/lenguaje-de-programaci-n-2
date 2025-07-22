#dibujar figuras en consola
class Figura:
    def __init__(self):
        pass

    def dibujar(self):
        print("no se puede dibujar una figura geometrica")
class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado

    def dibujar(self):
        for i in range(self.lado):
            print("■ "*self.lado)

class Triangulo(Figura):
    def __init__(self,altura):
        self.altura=altura


    def dibujar(self):
        for i in range(self.altura):
            print("▲ "*i)

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio

    def dibujar(self):
        
        for i in range(self.radio):
            print(
            "\n  ⚪⚪\n" \
            "⚪    ⚪\n" \
            "⚪    ⚪\n" \
            "  ⚪⚪  \n"*i)

#3. uso polimorfismo

figuras = [Cuadrado(3), Triangulo(4), Circulo(3)]

for figura in figuras:
    print("figura: ", figura.dibujar())