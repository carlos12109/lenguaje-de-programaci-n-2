import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
import time
import threading
import random

# Colores y fuentes
COLORES = ["red", "blue", "green", "purple", "orange", "darkblue"]
FUENTES = [("Helvetica", 20, "bold"), ("Arial", 22, "italic"), ("Times", 24, "bold")]

class ReproductorLetras:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor de Canciones con Letra")
        self.root.geometry("800x500")
        self.root.configure(bg="black")

        self.letras = []
        self.current_line = 0

        pygame.mixer.init()

        # Botón para cargar canción
        self.boton_cancion = ttk.Button(root, text="Seleccionar Canción MP3", command=self.cargar_cancion)
        self.boton_cancion.pack(pady=10)

        # Botón para cargar letra
        self.boton_letra = ttk.Button(root, text="Cargar Letra (formato mm:ss texto)", command=self.cargar_letra)
        self.boton_letra.pack(pady=10)

        # Botón para reproducir
        self.boton_play = ttk.Button(root, text="▶ Reproducir", command=self.reproducir)
        self.boton_play.pack(pady=10)

        # Área de texto para la letra
        self.texto = tk.Label(root, text="", bg="black", fg="white", font=("Helvetica", 22), wraplength=700, justify="center")
        self.texto.pack(expand=True)

    def cargar_cancion(self):
        self.archivo_cancion = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

    def cargar_letra(self):
        archivo_letra = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if archivo_letra:
            self.letras.clear()
            with open(archivo_letra, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        tiempo_str, texto = linea.strip().split(" ", 1)
                        minutos, segundos = map(int, tiempo_str.split(":"))
                        tiempo = minutos * 60 + segundos
                        self.letras.append((tiempo, texto))
                    except ValueError:
                        continue

    def reproducir(self):
        if hasattr(self, "archivo_cancion") and self.letras:
            pygame.mixer.music.load(self.archivo_cancion)
            pygame.mixer.music.play()
            threading.Thread(target=self.mostrar_letras).start()

    def mostrar_letras(self):
        inicio = time.time()
        for tiempo, linea in self.letras:
            espera = tiempo - (time.time() - inicio)
            if espera > 0:
                time.sleep(espera)
            color = random.choice(COLORES)
            fuente = random.choice(FUENTES)
            self.texto.config(text=linea, fg=color, font=fuente)

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = ReproductorLetras(root)
    root.mainloop()
