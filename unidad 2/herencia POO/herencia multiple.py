class Computadora:
    def encender(self):
        return "computadora encendida"
    
class Telefono:
    def llamar(self, numero):
        return f"llamando al numero {numero}..."
    

class Smartphone(Computadora, Telefono):
    def usar_aplicacion(self, app):
        return f"iniciando la app: {app}"

mi_telefono = Smartphone()
print(mi_telefono.encender())
print(mi_telefono.llamar("987654321"))
print(mi_telefono.usar_aplicacion("whatsApp"))