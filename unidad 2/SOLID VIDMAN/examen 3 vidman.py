import tkinter as tk
from tkinter import ttk
import time

# -------------------- LÓGICA DE NEGOCIO (S, O, L, I, D) --------------------
#CLASE HANOI
class HanoiGame:
    def __init__(self, n_discos):
        self.n_discos = n_discos
        self.movimientos = 0
        self.historial = []
        self.torres = {
            "A": [i for i in range(n_discos, 0, -1)],
            "B": [],
            "C": []
        }

    def mover_disco(self, origen, destino):
        if origen == destino:
            return False
        if self.torres[origen] and (not self.torres[destino] or self.torres[origen][-1] < self.torres[destino][-1]):
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos += 1
            self.historial.append((origen, destino))
            return True
        return False
    #muestra lo resuelto

    def esta_resuelto(self):
        return len(self.torres["C"]) == self.n_discos

    #FUNCION PARA RESOLVER TORRES DE HANOI
    # Utiliza recursión para resolver el juego de Torres de Hanoi
    def resolver_hanoi(self, n=None, origen="A", auxiliar="B", destino="C"):
        pasos = []
        n = n if n is not None else self.n_discos
        if n > 0:
            pasos += self.resolver_hanoi(n - 1, origen, destino, auxiliar)
            pasos.append((origen, destino))
            pasos += self.resolver_hanoi(n - 1, auxiliar, origen, destino)
        return pasos

# -------------------- INTERFAZ GRÁFICA (Tkinter) --------------------

class HanoiApp:
    def __init__(self, master):
        self.master = master
        master.title("Torres de Hanoi - SOLID")
        self.juego = None
        self.tiempo_inicio = None
        self.torre_seleccionada = None

        # UI
        self.crear_widgets()
    # Crea los widgets de la interfaz gráfica
    # Incluye etiquetas, botones, canvas y entradas de texto
    def crear_widgets(self):
        self.label_discos = ttk.Label(self.master, text="Número de discos:")
        self.label_discos.pack()
        self.entry_discos = ttk.Entry(self.master)
        self.entry_discos.insert(0, "3")
        self.entry_discos.pack()

        self.boton_iniciar = ttk.Button(self.master, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton_iniciar.pack()

        self.canvas = tk.Canvas(self.master, width=400, height=300, bg="lightblue")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_canvas)

        self.label_movimientos = ttk.Label(self.master, text="Movimientos: 0")
        self.label_movimientos.pack()

        self.label_tiempo = ttk.Label(self.master, text="Tiempo: 00:00")
        self.label_tiempo.pack()

        self.boton_solucion = ttk.Button(self.master, text="Mostrar Solución", command=self.mostrar_solucion)
        self.boton_solucion.pack()

        self.label_historial = ttk.Label(self.master, text="Historial:")
        self.label_historial.pack()
    # Inicia el juego con el número de discos especificado
    # Actualiza el tiempo de inicio y dibuja las torres
    def iniciar_juego(self):
        try:
            n_discos = int(self.entry_discos.get())
            if n_discos <= 0:
                raise ValueError
            self.juego = HanoiGame(n_discos)
            self.tiempo_inicio = time.time()
            self.actualizar_tiempo()
            self.dibujar_torres()
        except ValueError:
            print("Número inválido de discos.")
    # Actualiza el tiempo transcurrido desde que se inició el juego
    # Muestra el tiempo en formato MM:SS
    def actualizar_tiempo(self):
        if self.tiempo_inicio:
            t = int(time.time() - self.tiempo_inicio)
            self.label_tiempo.config(text=f"Tiempo: {t//60:02}:{t%60:02}")
            self.master.after(1000, self.actualizar_tiempo)
    # Dibuja las torres y los discos en el canvas
    # Resalta la torre seleccionada y muestra los discos en cada torre
    def dibujar_torres(self):
        self.canvas.delete("all")
        espacio_entre_torres = 130
        ancho_base = 60
        altura_disco = 20
        alto_torre = 150

        for i, torre in enumerate(["A", "B", "C"]):
            x = 80 + i * espacio_entre_torres
            y_base = 280
            color = "orange" if self.torre_seleccionada == torre else "brown"

            self.canvas.create_rectangle(x - 5, y_base - alto_torre, x + 5, y_base, fill=color)
            self.canvas.create_text(x, y_base + 10, text=torre)

            if self.juego:
                for j, disco in enumerate(self.juego.torres[torre]):
                    disco_ancho = ancho_base * (disco / self.juego.n_discos)
                    x0 = x - disco_ancho / 2
                    y0 = y_base - (j + 1) * (altura_disco + 4)
                    self.canvas.create_rectangle(x0, y0, x0 + disco_ancho, y0 + altura_disco, fill=self.color_disco(disco))

        if self.juego:
            self.label_movimientos.config(text=f"Movimientos: {self.juego.movimientos}")
            self.label_historial.config(text="\n".join([f"{o} → {d}" for o, d in self.juego.historial[-5:]]))

    def click_canvas(self, event):
        x = event.x
        for i, torre in enumerate(["A", "B", "C"]):
            x_torre = 80 + i * 130
            if abs(x - x_torre) < 50:
                if self.torre_seleccionada is None:
                    self.torre_seleccionada = torre
                else:
                    if self.juego.mover_disco(self.torre_seleccionada, torre):
                        self.dibujar_torres()
                        if self.juego.esta_resuelto():
                            print("¡Juego completado!")
                    self.torre_seleccionada = None
                break
        self.dibujar_torres()
    # Muestra la solución del juego de Torres de Hanoi
    # Ejecuta los pasos de la solución con un retraso para visualización
    def mostrar_solucion(self):
        if not self.juego:
            return
        pasos = self.juego.resolver_hanoi()
        self.ejecutar_pasos(pasos)
    # Ejecuta los pasos de la solución uno por uno
    # Utiliza un temporizador para mostrar cada movimiento con un retraso
    def ejecutar_pasos(self, pasos, idx=0):
        if idx >= len(pasos):
            return
        origen, destino = pasos[idx]
        self.juego.mover_disco(origen, destino)
        self.dibujar_torres()
        self.master.after(500, lambda: self.ejecutar_pasos(pasos, idx + 1))
    # Asigna un color a cada disco basado en su número
    # Utiliza una lista de colores predefinidos para alternar entre ellos
    def color_disco(self, disco):
        colores = ["red", "green", "blue", "cyan", "magenta", "yellow"]
        return colores[disco % len(colores)]

# -------------------- MAIN --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiApp(root)
    root.mainloop()
