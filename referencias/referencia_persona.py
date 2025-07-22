"""class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

p1 = Persona ("maria")
p2 = p1


p2.nombre = "Carla"

print(p1.nombre)"""

class Producto:
    def __init__(self, precio):
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

p = Producto(100)
p.aplicar_descuento(10)
print(p.precio)  # Imprime 90.0







