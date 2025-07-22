class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        return (f"{self.nombre} hace un sonido")

class Perro (Animal):
    def hablar(self):
        return (f"{self.nombre} dice ¡Guau!")
    
animal = Animal ("animal generico")
print(animal.hablar())
perro = Perro ("firualis")
print(perro.hablar())