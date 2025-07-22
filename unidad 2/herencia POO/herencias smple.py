class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

    def descripcion(self):
        return f"Vehiculo: {self.marca} {self.modelo}"
    

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puerta):
        super().__init__(marca, modelo)
        self.puerta =puerta

    def descripcion (self):
        return super().descripcion() + f" puertas: {self.puerta}"

auto1 = Auto("toyota", "corolla", 4)
print(auto1.descripcion())
#y de repente estas representando a tu universidad