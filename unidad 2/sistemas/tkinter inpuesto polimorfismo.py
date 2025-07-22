import tkinter as tk
from tkinter import ttk, messagebox

class Vehiculo:
    def __init__(self, marca, modelo, annio):
        self.__marca = marca
        self.__modelo = modelo
        self.__annio = int(annio)
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_annio(self):
        return self.__annio
    def calcular_impuesto(self):
        pass
    def mostrar_info(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__annio}, Impuesto: {self.calcular_impuesto()}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, annio, impuesto_base):
        super().__init__(marca, modelo, annio)
        self.__impuesto_base = float(impuesto_base)
    def calcular_impuesto(self):
        recargo = 50 if self.get_annio() < 2010 else 100
        return self.__impuesto_base + recargo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, annio, impuesto_base):
        super().__init__(marca, modelo, annio)
        self.__impuesto_base = float(impuesto_base)
    def calcular_impuesto(self):
        return self.__impuesto_base

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Vehículos")
        self.geometry("500x400")
        self.configure(bg="#e3f6fc")
        self.lista_vehiculos = []
        self.tipo_var = tk.StringVar(value="Auto")
        self.crear_widgets()

    def crear_widgets(self):
        titulo = tk.Label(self, text="Registro de Vehículos", font=("Arial", 18, "bold"), bg="#e3f6fc", fg="#1b4965")
        titulo.pack(pady=10)

        frame = tk.Frame(self, bg="#e3f6fc")
        frame.pack(pady=5)

        ttk.Label(frame, text="Tipo:", background="#e3f6fc").grid(row=0, column=0, padx=5, pady=5)
        tipo_menu = ttk.Combobox(frame, textvariable=self.tipo_var, values=["Auto", "Moto"], state="readonly")
        tipo_menu.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Marca:", background="#e3f6fc").grid(row=1, column=0, padx=5, pady=5)
        self.marca_entry = ttk.Entry(frame)
        self.marca_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Modelo:", background="#e3f6fc").grid(row=2, column=0, padx=5, pady=5)
        self.modelo_entry = ttk.Entry(frame)
        self.modelo_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Año:", background="#e3f6fc").grid(row=3, column=0, padx=5, pady=5)
        self.annio_entry = ttk.Entry(frame)
        self.annio_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Impuesto Base:", background="#e3f6fc").grid(row=4, column=0, padx=5, pady=5)
        self.impuesto_entry = ttk.Entry(frame)
        self.impuesto_entry.grid(row=4, column=1, padx=5, pady=5)

        btn_registrar = tk.Button(self, text="Registrar Vehículo", bg="#62b6cb", fg="white", font=("Arial", 12, "bold"),
                                  command=self.registrar_vehiculo)
        btn_registrar.pack(pady=10)

        btn_mostrar = tk.Button(self, text="Mostrar Vehículos", bg="#1b4965", fg="white", font=("Arial", 12, "bold"),
                                command=self.mostrar_vehiculos)
        btn_mostrar.pack(pady=5)

        self.text_area = tk.Text(self, height=8, width=55, bg="#fafdff", fg="#1b4965", font=("Arial", 10))
        self.text_area.pack(pady=10)

    def registrar_vehiculo(self):
        tipo = self.tipo_var.get()
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        annio = self.annio_entry.get()
        impuesto = self.impuesto_entry.get()
        if not (marca and modelo and annio and impuesto):
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return
        try:
            if tipo == "Auto":
                vehiculo = Auto(marca, modelo, int(annio), float(impuesto))
            else:
                vehiculo = Moto(marca, modelo, int(annio), float(impuesto))
            self.lista_vehiculos.append(vehiculo)
            messagebox.showinfo("Registro exitoso", f"{tipo} registrado correctamente.")
            self.marca_entry.delete(0, tk.END)
            self.modelo_entry.delete(0, tk.END)
            self.annio_entry.delete(0, tk.END)
            self.impuesto_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Año e impuesto deben ser números.")

    def mostrar_vehiculos(self):
        self.text_area.delete(1.0, tk.END)
        if not self.lista_vehiculos:
            self.text_area.insert(tk.END, "No hay vehículos registrados.\n")
        else:
            for v in self.lista_vehiculos:
                self.text_area.insert(tk.END, v.mostrar_info() + "\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()