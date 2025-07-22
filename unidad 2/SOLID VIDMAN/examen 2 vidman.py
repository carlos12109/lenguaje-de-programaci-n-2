import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
import math

# cuando seleciones la figura te muestra todo sus parametros a ingresar
#una vez ingresado te muestra todo los resultados de las figuras

# ------------------ INTERFAZ BASE ------------------
class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

# ------------------ FIGURAS ------------------
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def descripcion(self):
        return f"Círculo de radio {self.radio}"

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def descripcion(self):
        return f"Cuadrado de lado {self.lado}"

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def descripcion(self):
        return f"Rectángulo de base {self.base} y altura {self.altura}"

class Triangulo(FiguraGeometrica):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetro(self):
        return self.a + self.b + self.c

    def descripcion(self):
        return f"Triángulo de lados {self.a}, {self.b}, {self.c}"

# ------------------ VISUALIZADOR ------------------
class VisualizadorFiguras:
    def __init__(self, figuras, textbox):
        self.figuras = figuras
        self.textbox = textbox

    def mostrar(self):
        self.textbox.delete("1.0", tk.END)
        for figura in self.figuras:
            self.textbox.insert(tk.END, f"{figura.descripcion()}\n", "desc")
            self.textbox.insert(tk.END, f"Área: {figura.area():.2f}\n", "res")
            self.textbox.insert(tk.END, f"Perímetro: {figura.perimetro():.2f}\n\n", "res")

# ------------------ INTERFAZ PRINCIPAL ------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculadora de Figuras Geométricas")
        self.root.configure(bg="#f2f2f2")
        self.figuras = []

        title = tk.Label(root, text="Sistema de Figuras Geométricas", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#2e7d32")
        title.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # Selector de figura
        tk.Label(root, text="Selecciona una figura:", font=("Helvetica", 11), bg="#f2f2f2").grid(row=1, column=0, sticky="w", padx=10)
        self.figura_var = tk.StringVar()
        self.figura_menu = ttk.Combobox(root, textvariable=self.figura_var, state="readonly",
                                        values=["Círculo", "Cuadrado", "Rectángulo", "Triángulo"], width=20)
        self.figura_menu.grid(row=1, column=1, pady=5)
        self.figura_menu.bind("<<ComboboxSelected>>", self.actualizar_parametros)

        # Marco de parámetros
        self.param_frame = tk.Frame(root, bg="#e8f5e9", bd=2, relief="groove")
        self.param_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        self.param_labels = []
        self.param_entries = []

        # Botones
        tk.Button(root, text="➕ Agregar Figura", bg="#81c784", fg="white", font=("Helvetica", 10, "bold"),
                command=self.agregar_figura).grid(row=3, column=0, pady=5, padx=10)
        tk.Button(root, text="👁 Mostrar Figuras", bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"),
                command=self.mostrar_figuras).grid(row=3, column=1, pady=5)

        # Área de resultados
        self.textbox = tk.Text(root, width=60, height=15, bg="#ffffff", fg="#333", font=("Courier New", 10))
        self.textbox.grid(row=4, column=0, columnspan=2, padx=10, pady=(5, 10))
        self.textbox.tag_config("desc", foreground="#1a237e", font=("Courier New", 10, "bold"))
        self.textbox.tag_config("res", foreground="#004d40")

    def actualizar_parametros(self, event=None):
        for lbl in self.param_labels:
            lbl.destroy()
        for ent in self.param_entries:
            ent.destroy()
        self.param_labels.clear()
        self.param_entries.clear()

        figura = self.figura_var.get()
        campos = []

        if figura == "Círculo":
            campos = ["Radio"]
        elif figura == "Cuadrado":
            campos = ["Lado"]
        elif figura == "Rectángulo":
            campos = ["Base", "Altura"]
        elif figura == "Triángulo":
            campos = ["Lado A", "Lado B", "Lado C"]

        for i, nombre in enumerate(campos):
            lbl = tk.Label(self.param_frame, text=nombre + ":", font=("Helvetica", 10), bg="#e8f5e9")
            lbl.grid(row=i, column=0, padx=5, pady=3, sticky="w")
            ent = tk.Entry(self.param_frame, font=("Helvetica", 10), width=20)
            ent.grid(row=i, column=1, padx=5, pady=3)
            self.param_labels.append(lbl)
            self.param_entries.append(ent)

    def agregar_figura(self):
        tipo = self.figura_var.get()
        try:
            valores = [float(e.get()) for e in self.param_entries]
            figura = None
            if tipo == "Círculo" and len(valores) == 1:
                figura = Circulo(valores[0])
            elif tipo == "Cuadrado" and len(valores) == 1:
                figura = Cuadrado(valores[0])
            elif tipo == "Rectángulo" and len(valores) == 2:
                figura = Rectangulo(valores[0], valores[1])
            elif tipo == "Triángulo" and len(valores) == 3:
                figura = Triangulo(valores[0], valores[1], valores[2])

            if figura:
                self.figuras.append(figura)
                self.textbox.insert(tk.END, "✅ Figura agregada correctamente.\n", "res")
            else:
                self.textbox.insert(tk.END, "❌ Parámetros insuficientes o inválidos.\n", "res")
        except ValueError:
            self.textbox.insert(tk.END, "⚠ Error: Ingresa solo números válidos.\n", "res")

    def mostrar_figuras(self):
        visualizador = VisualizadorFiguras(self.figuras, self.textbox)
        visualizador.mostrar()

# ------------------ EJECUCIÓN ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
