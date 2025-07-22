"""class persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura


    def hablar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")

    def caminar(self, distancia):
        print(f"{self.nombre} ha caminado {distancia} metros")

    def dormir(self, horas):
        print(f"{self.nombre} ha dormido {horas} horas")

#creacion de objetos

persona1 = persona("juan", 25, 1.75)
persona2 = persona("maria", 30, 1.55)

# uso de metodos 
print("\n-------aciones de juan------------")
persona1.hablar("hola soy juan")
persona1.caminar(500)
persona1.dormir(8)

print("\n-------acciones de maria------------")
persona2.hablar("hola soy maria")
persona2.caminar(300)
persona2.dormir(7)
"""
"""
class animal:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def especie(self, raza):
        print(f"{self.nombre} es {raza} ")


    def jugar(self, jugar):
        print(f"{self.nombre} juega {jugar} ")

    def caminar(self, distancia):
        print(f"{self.nombre} ha caminado {distancia} metros")

    def dormir(self, horas):
        print(f"{self.nombre} ha dormido {horas} horas")


#creacion de objetos

animal1 = animal("michi", "siomera", 2)
animal2 = animal("rex", "pastor aleman", 5)

# uso de metodos 
print("\n-------aciones de gato------------")
animal1.especie("gato")
animal1.jugar("con la pelota")
animal1.caminar(500)
animal1.dormir(8)

print("\n-------acciones de perro------------")
animal2.especie("perro")
animal2.jugar("con su sueño")
animal2.caminar(300)
animal2.dormir(7)
"""

class docotor:
    def __init__(self, nombre, especialidad, años_experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.años_experiencia = años_experiencia

    def mostrar_nombre(self):
        print(f"El doctor se llama: {self.nombre}")

    def mostrar_especialidad(self):
        print(f"Es de especialidad: {self.especialidad}")

    def mostrar_experiencia(self):
        print(f"cuenta con {self.años_experiencia} años de experiencia")



# Creacion de objetos
doctor1 = docotor("Juan", "Dermatologia", 20)
doctor2 = docotor("Gabriel", "cardiologia", 5)

# Uso de metodos
print("\n-------Acciones de doctor 1------------")
doctor1.mostrar_nombre()
doctor1.mostrar_especialidad()
doctor1.mostrar_experiencia()


print("\n-------Acciones de doctor 2------------")
doctor2.mostrar_nombre()
doctor2.mostrar_especialidad()
doctor2.mostrar_experiencia()





