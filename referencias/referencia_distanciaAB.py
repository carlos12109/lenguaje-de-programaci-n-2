import math
class Ciudad:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y

    def distancia(self, otra_ciudad):
        dx = self.x - otra_ciudad.x
        dy = self.y - otra_ciudad.y

        return math.sqrt(dx **2 + dy **2)

a1=input("ingrese el nombre de la ciudad 1: ")
a3=float(input("ingrese la coordenada x de la ciudad 1: "))
a4=float(input("ingrese la coordenada y de la ciudad 1: "))

a2=input("ingrese el nombre de la ciudad 2: ")
a5=float(input("ingrese la coordenada x de la ciudad 2: "))
a6=float(input("ingrese la coordenada y de la ciudad 2: "))

#creacion de objetos
ciudad1 = Ciudad(a1, a3, a4)
ciudad2 = Ciudad(a2, a5, a6)


#referencia a la distancia entre dos objetos
ref1 = ciudad1
ref2 = ciudad2

distancia_km = ref1.distancia(ref2)
print(f"la distiancia entre {ref1.nombre} y {ref2.nombre} es de: {distancia_km: .2f} km")
