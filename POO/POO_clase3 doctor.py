class doctor:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia
    
    def mostrar_infoirmacion(self):
        print(f"Nombre del doctor: ", self.nombre)
        print(f"Especialidad del doctor: ", self.especialidad)
        print(f"Años de experiencia del doctor: ", self.experiencia)
    
    def atender_paciente(self, paciente):
        print(f"El doctor {self.nombre} está atendiendo al paciente {paciente}")

    def calcular_salario(self):
        salario_base = 2000
        bono_experiencia =self.experiencia * 150
        salario_total = salario_base + bono_experiencia
        print(f"el salario mensula del dr. {self.nombre} es $ {salario_total}")
    
    def recetar_medicamento (self, medicamento):
        print(f"el doctor {self.nombre} receta: {medicamento}")


#crear un objeto doctor
doctor1 = doctor("Carlos Perez", "Cardiología", 10)
doctor2 = doctor("diñooo", "Dentista", 1)
doctor3 = doctor("vidman", "dermatologo", 6)

#mostrar infirmacion del doctor 
print("\n-------acciones de doctor 1------------")
doctor1.mostrar_infoirmacion()
doctor1.atender_paciente("Juan Lopez")
doctor1.calcular_salario()
doctor1.recetar_medicamento("paracetamol 500 mg ")

print("\n-------acciones de docotr 2------------")
doctor2.mostrar_infoirmacion()
doctor2.atender_paciente(" blanca ")
doctor2.calcular_salario()
doctor2.recetar_medicamento("atibiticos 4 mg ")

print("\n-------acciones de docotr 3------------")
doctor3.mostrar_infoirmacion()
doctor3.atender_paciente(" Alex ")
doctor3.calcular_salario()
doctor3.recetar_medicamento("P.generico 60 mg ")





