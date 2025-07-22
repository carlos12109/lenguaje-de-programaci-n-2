"""un sisptema de empleado poo()
clase principlamn empleado
sub clases administrativos, operarios (herencia)
atrivbutos de la clase prinvipsal
nombre dni salario base (encapsulamiento y polimorfismo(calcular salario y mostrar imformacion))

sub vlase Administrativo: nombre, dni, salario base
sub clase operarios: nobre dni salario base, bono de produccion"""

"""
class Solutionempleado
atributos de la clase principal:
nombre
dni
monto salario base
(encapsulamiento y polimorfismo(calcular salario y mostrar imformacion)
sub clase administrativo
sub base Administrativo: nombre, dni, salario base menos el impuesto de 10%
sub clase operarios:
nombre dni salario base , bono de produccion +
sub clase Empleado:
nombre, dni, salario base
ar"""
class Empleado:
    def __init__(self, nombre, dni, salario_base):
        self.__nombre = nombre
        self.__dni = dni
        self.__salario_base = salario_base

    def get_nombre(self):
        return self.__nombre
    def get_dni(self):
        return self.__dni
    def get_salario_base(self):
        return self.__salario_base

    def calcular_salario(self):
        return self.__salario_base

    def mostrar_informacion(self) -> str:
        return f"Nombre: {self.__nombre}, DNI: {self.__dni}, Salario Base: {self.__salario_base}, Salario Total: {self.calcular_salario()}"

class Administrativo(Empleado):
    def __init__(self, nombre, dni, salario_base):
        super().__init__(nombre, dni, salario_base)

    #restar 10% del salario base y que muestre la cantidad restada
    def calcular_salario(self):

        return self.get_salario_base() * 0.9
    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", descuento de salario: {self.get_salario_base()*0.9-self.get_salario_base()}"
    

class Operario(Empleado):
    def __init__(self, nombre, dni, salario_base, bono_produccion):
        super().__init__(nombre, dni, salario_base)
        self.__bono_produccion = bono_produccion

    def get_bono_produccion(self):
        return self.__bono_produccion

    def calcular_salario(self):
        return self.get_salario_base() + self.__bono_produccion

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Bono de Producción: {self.get_bono_produccion()}, Salario Total: {self.calcular_salario()}"
    
def main():
    empleados = []
    while True:
        print("-"*50)
        print("             SISTEMA DE EMPLEADOS        ")
        print("-"*50+"\n")
        print("1. Registrar Administrativo")
        print("2. Registrar Operario")
        print("3. Mostrar todos los empleados")
        print("4. Salir\n")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del administrativo: ")
            dni = input("Ingrese el DNI del administrativo: ")
            salario_base = float(input("Ingrese el salario base del administrativo: "))
            empleados.append(Administrativo(nombre, dni, salario_base))
            print("Administrativo registrado exitosamente.\n")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del operario: ")
            dni = input("Ingrese el DNI del operario: ")
            salario_base = float(input("Ingrese el salario base del operario: "))
            bono_produccion = float(input("Ingrese el bono de producción del operario: "))
            empleados.append(Operario(nombre, dni, salario_base, bono_produccion))
            print("Operario registrado exitosamente.\n")
        elif opcion == "3":
            if not empleados:
                print("No hay empleados registrados.\n")
            else:
                for emp in empleados:
                    print(emp.mostrar_informacion())
                print()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()