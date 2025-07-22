class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo_inicial = saldo_inicial

    def consultar_saldo(self):
        print(f"saldo actual de {self._titular}: S/. {self._saldo_inicial: .2f}")

    def depositar(self,monto):
        if monto>0:
            self._saldo_inicial += monto
            print (f"deposito de S/. {monto: .2f} realizo con exito")
        else:
            print("el monot a depositar debe ser POSITIVO")

    def retirar(self, monto):
        if 0< monto <=self._saldo_inicial:
            self._saldo_inicial-=monto
            print("---------------------------------------------------")
            print(f"Retiro de S/. {monto: .2f} realizado con exito.")
        else:
            print("monto  de retiro insuficiente")

#objeto
cuenta = CuentaBancaria("Raul", 500.00)
cuenta.consultar_saldo()

cuenta.depositar(150)
cuenta.consultar_saldo()

cuenta.retirar(100)
cuenta.consultar_saldo()