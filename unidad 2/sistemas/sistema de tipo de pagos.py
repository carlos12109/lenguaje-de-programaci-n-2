# Clase base
class MetodoPago:
    def procesar_pago(self):
        pass
        

class PagoTarjetaCredito(MetodoPago):
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre

    def procesar_pago(self):
        monto = 200
        print(f"Procesando pago de ${monto:.2f} con tarjeta de crédito de {self.nombre} Pago exitoso.")

# Subclase: Pago con PayPal
class PagoPayPal(MetodoPago):
    def __init__(self, email):
        self.email = email

    def procesar_pago(self):
        monto = 150
        print(f"Procesando pago de ${monto:.2f} mediante PayPal cuenta: {self.email} Pago exitoso.")

# Subclase: Pago con Criptomonedas
class PagoCriptomoneda(MetodoPago):
    def __init__(self, codigo):
        self.codigo = codigo

    def procesar_pago(self):
        monto = 300
        print(f"Procesando pago de ${monto:.2f} en criptomonedas desde wallet {self.codigo} Pago exitoso.")

# Función que utiliza polimorfismo
pagos = [PagoTarjetaCredito("200", "vidman"), PagoPayPal("vidmanmamani@mail.com.com"), PagoCriptomoneda("1312312312312")
]

for pago in pagos:

    print(f"pagos: {pago.procesar_pago()}")
