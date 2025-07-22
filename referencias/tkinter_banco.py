import tkinter as tk
from tkinter import ttk
from datetime import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo_inicial = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self._titular}: S/. {self._saldo_inicial: .2f}"

    def depositar(self, monto):
        if monto > 0:
            self._saldo_inicial += monto
            return f"Depósito de S/. {monto: .2f} realizado con éxito."
        else:
            return "El monto a depositar debe ser POSITIVO."

    def retirar(self, monto):
        if 0 < monto <= self._saldo_inicial:
            self._saldo_inicial -= monto
            self.guardar_boleta(monto)
            return f"Retiro de S/. {monto: .2f} realizado con éxito."
        else:
            return "Monto de retiro insuficiente."

    def guardar_boleta(self, monto):
        now = datetime.now()
        fecha = now.strftime("%Y-%m-%d %H-%M-%S")
        nombre_archivo = f"boleta_{fecha}.txt"
        with open(nombre_archivo, "w") as file:
            file.write("===== Boleta de Comprobante =====\n")
            file.write(f"Titular: {self._titular}\n")
            file.write(f"Fecha: {now.strftime('%d/%m/%Y')}\n")
            file.write(f"Hora: {now.strftime('%H:%M:%S')}\n")
            file.write(f"Monto retirado: S/. {monto: .2f}\n")
            file.write(f"Saldo restante: S/. {self._saldo_inicial: .2f}\n")
            file.write("=================================\n")

# Interfaz gráfica con Tkinter
class App:
    def __init__(self, root):
        self.cuenta = CuentaBancaria("Raul", 500.00)
        root.title("Gestión de Cuenta Bancaria")
        root.geometry("400x350")
        root.configure(bg="#f0f4f7")

        self.label_titulo = ttk.Label(root, text="Cuenta Bancaria de Raul", font=("Helvetica", 16))
        self.label_titulo.pack(pady=10)

        self.entry_monto = ttk.Entry(root)
        self.entry_monto.pack(pady=5)
        self.entry_monto.insert(0, "Ingrese monto")

        self.btn_depositar = ttk.Button(root, text="Depositar", command=self.depositar)
        self.btn_depositar.pack(pady=5)

        self.btn_retirar = ttk.Button(root, text="Retirar", command=self.retirar)
        self.btn_retirar.pack(pady=5)

        self.btn_saldo = ttk.Button(root, text="Consultar Saldo", command=self.consultar)
        self.btn_saldo.pack(pady=5)

        self.resultado = tk.Text(root, height=8, width=45, bg="#ffffff", font=("Courier", 10))
        self.resultado.pack(pady=10)

    def mostrar_mensaje(self, mensaje):
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, mensaje)

    def consultar(self):
        mensaje = self.cuenta.consultar_saldo()
        self.mostrar_mensaje(mensaje)

    def depositar(self):
        try:
            monto = float(self.entry_monto.get())
            mensaje = self.cuenta.depositar(monto)
        except ValueError:
            mensaje = "Por favor, ingrese un monto válido."
        self.mostrar_mensaje(mensaje)

    def retirar(self):
        try:
            monto = float(self.entry_monto.get())
            mensaje = self.cuenta.retirar(monto)
        except ValueError:
            mensaje = "Por favor, ingrese un monto válido."
        self.mostrar_mensaje(mensaje)

# Ejecutar la app
root = tk.Tk()
app = App(root)
root.mainloop()
