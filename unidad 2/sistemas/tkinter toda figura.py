import tkinter as tk
from tkinter import ttk
import math

# -------------------- CLASES --------------------

class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def mostrar_info(self):
        return f"Figura: {self.__nombre}\nÁrea: {self.calcular_area():.2f}\nPerímetro: {self.calcular_perimetro():.2f}\n"

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.__radio = radio
    def calcular_area(self):
        return math.pi * self.__radio**2
    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.__base = base
        self.__altura = altura
    def calcular_area(self):
        return self.__base * self.__altura
    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        super().__init__("Triángulo")
        self.__base = base
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    def calcular_area(self):
        return (self.__base * self.__altura) / 2
    def calcular_perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

class Pentagono(Figura):
    def __init__(self, lado, apotema):
        super().__init__("Pentágono")
        self.__lado = lado
        self.__apotema = apotema
    def calcular_area(self):
        perimetro = 5 * self.__lado
        return (perimetro * self.__apotema) / 2
    def calcular_perimetro(self):
        return 5 * self.__lado

class Hexagono(Figura):
    def __init__(self, lado, apotema):
        super().__init__("Hexágono")
        self.__lado = lado
        self.__apotema = apotema
    def calcular_area(self):
        perimetro = 6 * self.__lado
        return (perimetro * self.__apotema) / 2
    def calcular_perimetro(self):
        return 6 * self.__lado

# -------------------- INTERFAZ --------------------

class SistemaFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Figuras Geométricas")
        self.root.geometry("750x450")
        self.root.configure(bg="#e0f7fa")

        self.figuras = []

        self.frame_formulario = tk.Frame(root, bg="#e1f5fe", bd=2, relief="ridge")
        self.frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.frame_resultado = tk.Frame(root, bg="#f0f4c3", bd=2, relief="ridge")
        self.frame_resultado.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.label_titulo = tk.Label(self.frame_formulario, text="Registrar Figura", font=("Arial", 16), bg="#e1f5fe")
        self.label_titulo.pack(pady=10)

        self.combo_figura = ttk.Combobox(self.frame_formulario, values=[
            "Círculo", "Rectángulo", "Triángulo", "Pentágono", "Hexágono"
        ])
        self.combo_figura.pack()
        self.combo_figura.bind("<<ComboboxSelected>>", self.mostrar_campos)

        self.campos = []
        self.labels_entradas = []
        self.boton_guardar = None

        self.text_resultado = tk.Text(self.frame_resultado, height=20, width=40, bg="#f9fbe7", font=("Courier", 10))
        self.text_resultado.pack(padx=10, pady=10)

        self.boton_mostrar = tk.Button(self.frame_resultado, text="Mostrar Figuras", bg="#81d4fa", command=self.mostrar_todas)
        self.boton_mostrar.pack(pady=5)

    def limpiar_campos(self):
        for widget in self.labels_entradas:
            widget.destroy()
        self.labels_entradas.clear()
        self.campos.clear()
        if self.boton_guardar:
            self.boton_guardar.destroy()

    def mostrar_campos(self, event):
        figura = self.combo_figura.get()
        self.limpiar_campos()

        campos_figura = {
            "Círculo": ["Radio"],
            "Rectángulo": ["Base", "Altura"],
            "Triángulo": ["Base", "Altura", "Lado 1", "Lado 2", "Lado 3"],
            "Pentágono": ["Lado", "Apotema"],
            "Hexágono": ["Lado", "Apotema"]
        }

        for campo in campos_figura[figura]:
            label = tk.Label(self.frame_formulario, text=campo, bg="#e1f5fe")
            label.pack()
            entry = tk.Entry(self.frame_formulario)
            entry.pack()
            self.labels_entradas.append(label)
            self.campos.append(entry)

        self.boton_guardar = tk.Button(self.frame_formulario, text="Registrar", bg="#aed581", command=self.registrar_figura)
        self.boton_guardar.pack(pady=10)

    def registrar_figura(self):
        figura = self.combo_figura.get()
        try:
            valores = [float(entry.get()) for entry in self.campos]
            if figura == "Círculo":
                f = Circulo(*valores)
            elif figura == "Rectángulo":
                f = Rectangulo(*valores)
            elif figura == "Triángulo":
                f = Triangulo(*valores)
            elif figura == "Pentágono":
                f = Pentagono(*valores)
            elif figura == "Hexágono":
                f = Hexagono(*valores)
            else:
                return
            self.figuras.append(f)
            self.text_resultado.insert(tk.END, f"{figura} registrado correctamente.\n")
        except ValueError:
            self.text_resultado.insert(tk.END, "Error: ingrese solo valores numéricos.\n")

    def mostrar_todas(self):
        self.text_resultado.delete(1.0, tk.END)
        if not self.figuras:
            self.text_resultado.insert(tk.END, "No hay figuras registradas.\n")
        else:
            for figura in self.figuras:
                self.text_resultado.insert(tk.END, figura.mostrar_info() + "\n")

# -------------------- EJECUCIÓN --------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaFiguras(root)
    root.mainloop()
