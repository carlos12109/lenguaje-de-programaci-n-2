class persona:
    def __init__(self, nombre, edad, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
    #getter para nombre
    def obtener_nombre(self):
        return self.__nombre

    #getter para edad
    def obtener_edad(self):
        return self.__edad
    #getter para altura
    def obtener_altura(self):
        return self.__altura

    #setter para nombre
    def establecer_nombre(self, nombre):
        self.__nombre = nombre
    #setter para edad
    def establecer_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    def mayor_edad(self):
        return self.__edad >= 18

    #setter para altura
    def establecer_altura(self, altura):
        self.__altura = altura

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}, edad: {self.__edad} Altura: {self.__altura}")

    def cumplir_edad(self):
        self.__edad+=1
        print(f"feliz cumpleaño! {self.__nombre} ahora tienes: {self.__edad} años")

#creacion de objetos
persona1 = persona("juan", 15, 1.75)
#persona2 = persona("maria", 30, 1.55)
persona1.mostrar_datos()

if persona1.mayor_edad():
    print("es mayor de edad")
else:
    print(" es menor de edad")

persona1.cumplir_edad()
persona1.mostrar_datos()