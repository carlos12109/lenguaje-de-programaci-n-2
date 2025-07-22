import tkinter as tk
from tkinter import ttk
from datetime import datetime
import openpyxl

historial = []
campos_entry = []

# Función para mostrar campos específicos según método de pago
def mostrar_campos_especificos(event=None):
    for widget in frame_especifico.winfo_children():
        widget.destroy()
    campos_entry.clear()

    metodo = metodo_pago.get()
    campos = []

    if metodo == "Tarjeta de crédito":
        campos = [
            "Tu nombre", "Tu número de tarjeta",
            "Nombre del destino", "Número de tarjeta destino", "Monto (S/)"
        ]
    elif metodo == "Yape":
        campos = [
            "Tu nombre", "Tu DNI", "Tu celular",
            "Nombre del destino", "Celular del destino", "Monto (S/)"
        ]
    elif metodo == "Plin":
        campos = [
            "Tu nombre", "Tu celular",
            "Nombre del destino", "Celular del destino", "Monto (S/)"
        ]
    elif metodo == "PayPal":
        campos = [
            "Tu nombre", "Tu correo PayPal",
            "Correo del destino", "Monto (S/)"
        ]
    elif metodo == "Criptomonedas":
        campos = [
            "Tu nombre", "Tu Wallet ID",
            "Wallet destino", "Criptomoneda usada", "Monto (S/)"
        ]

    for i, campo in enumerate(campos):
        label = tk.Label(frame_especifico, text=campo + ":", bg="#393E46", fg="white", font=("Arial", 12))
        label.grid(row=i, column=0, sticky="e", pady=2)
        entry = tk.Entry(frame_especifico, font=("Arial", 12), width=30)
        entry.grid(row=i, column=1, padx=10, pady=2)
        campos_entry.append(entry)

# Función para registrar depósito
def registrar_deposito():
    metodo = metodo_pago.get()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datos = [e.get().strip() for e in campos_entry]

    if not metodo or any(not d for d in datos):
        label_status.config(text="Por favor completa todos los campos", fg="red")
        return

    try:
        monto = float([d for d in datos if d.replace('.', '', 1).isdigit()][-1])
    except:
        label_status.config(text="Monto inválido", fg="red")
        return

    deposito = {
        "Método": metodo,
        "Datos": datos,
        "Fecha": fecha,
        "Monto": monto
    }
    historial.append(deposito)
    actualizar_historial()

    for e in campos_entry:
        e.delete(0, tk.END)

# Función para actualizar tabla de historial
def actualizar_historial():
    tree.delete(*tree.get_children())
    for i, h in enumerate(historial, 1):
        resumen = ", ".join(h["Datos"][:2])
        tree.insert("", "end", values=(i, h["Método"], resumen, f"S/ {h['Monto']:.2f}", h["Fecha"]))
    label_status.config(text="Depósito registrado correctamente", fg="green")

# Exportar a archivo .txt
def exportar_txt():
    with open("historial_depositos.txt", "w", encoding="utf-8") as f:
        f.write("Historial de Depósitos\n\n")
        for h in historial:
            f.write(f"Método: {h['Método']}\n")
            for dato in h["Datos"]:
                f.write(f"  {dato}\n")
            f.write(f"Fecha: {h['Fecha']}\n\n")
    label_status.config(text="Exportado a historial_depositos.txt", fg="blue")

# Exportar a archivo .xlsx
def exportar_excel():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Historial"
    ws.append(["#", "Método", "Remitente", "Monto", "Fecha"])
    for i, h in enumerate(historial, 1):
        resumen = ", ".join(h["Datos"][:2])
        ws.append([i, h["Método"], resumen, h["Monto"], h["Fecha"]])
    wb.save("historial_depositos.xlsx")
    label_status.config(text="Exportado a historial_depositos.xlsx", fg="blue")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Depósitos")
ventana.configure(bg="#222831")
ventana.geometry("950x680")

# Estilo tabla
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#EEEEEE", foreground="black", rowheight=25, fieldbackground="#EEEEEE")
style.map("Treeview", background=[("selected", "#00ADB5")])

# Título
tk.Label(ventana, text="Sistema de Registro de Depósitos", bg="#222831", fg="#00FFF5",
         font=("Helvetica", 18, "bold")).pack(pady=10)

# Frame para método de pago
frame_form = tk.Frame(ventana, bg="#393E46", pady=10, padx=10)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Método de pago:", bg="#393E46", fg="white", font=("Arial", 12)).grid(row=0, column=0, sticky="e")
metodo_pago = ttk.Combobox(
    frame_form,
    values=["Yape", "Plin", "Tarjeta de crédito", "PayPal", "Criptomonedas"],
    font=("Arial", 12),
    state="readonly"
)
metodo_pago.grid(row=0, column=1, padx=10)
metodo_pago.bind("<<ComboboxSelected>>", mostrar_campos_especificos)
metodo_pago.set("Yape")

# Frame para campos personalizados
frame_especifico = tk.Frame(ventana, bg="#393E46", pady=10, padx=10)
frame_especifico.pack()
mostrar_campos_especificos()

# Botón de registrar
btn_registrar = tk.Button(ventana, text="Registrar Depósito", bg="#00ADB5", fg="white",
                          font=("Arial", 12, "bold"), command=registrar_deposito)
btn_registrar.pack(pady=10)

# Tabla historial
tree = ttk.Treeview(ventana, columns=("Nº", "Método", "Remitente", "Monto", "Fecha"), show="headings", height=7)
for col in ("Nº", "Método", "Remitente", "Monto", "Fecha"):
    tree.heading(col, text=col)
tree.pack(padx=20, pady=10)

# Botones de exportación
frame_exportar = tk.Frame(ventana, bg="#222831")
frame_exportar.pack()

tk.Button(frame_exportar, text="Exportar TXT", bg="#F96D00", fg="white", font=("Arial", 12, "bold"),
          command=exportar_txt).grid(row=0, column=0, padx=10)
tk.Button(frame_exportar, text="Exportar Excel", bg="#00C853", fg="white", font=("Arial", 12, "bold"),
          command=exportar_excel).grid(row=0, column=1, padx=10)

# Etiqueta de estado
label_status = tk.Label(ventana, text="", bg="#222831", fg="white", font=("Arial", 12))
label_status.pack(pady=10)

ventana.mainloop()
