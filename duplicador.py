# Para generar el ejecutable (.exe) usa:
# pyinstaller --onefile --windowed duplicador.py

# importaciones necesarias
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import PyPDF2

# función para duplicar el archivo
def duplicar_archivo(filepath, cantidad):
    base, ext = os.path.splitext(filepath)
    for i in range(1, cantidad+1):
        nuevo_nombre = f"{base}_copia{i}{ext}"
        shutil.copy(filepath, nuevo_nombre)

def duplicar_pdf(filepath, cantidad):
    # Lee el PDF original
    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        writer = PyPDF2.PdfWriter()
        # Repite todas las páginas 'cantidad' veces
        for _ in range(cantidad):
            for page in reader.pages:
                writer.add_page(page)
        # Guarda el PDF resultante con nombre temporal
        base, ext = os.path.splitext(filepath)
        temp_nombre = f"{base}_duplicado{ext}"
        with open(temp_nombre, "wb") as out_f:
            writer.write(out_f)
    # Borra el archivo original y renombra el nuevo
    os.remove(filepath)
    os.rename(temp_nombre, filepath)
    return filepath

# función para seleccionar archivo
def seleccionar_archivo():
    filepath = filedialog.askopenfilename(title="Selecciona un archivo")
    if filepath:
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, filepath)

# función principal al presionar el botón
def ejecutar_duplicado():
    filepath = entry_archivo.get()
    try:
        cantidad = int(entry_cantidad.get())
        if not os.path.isfile(filepath):
            messagebox.showerror("Error", "Archivo no encontrado.")
            return
        if cantidad < 1:
            messagebox.showerror("Error", "La cantidad debe ser mayor a 0.")
            return
        # Solo permite PDFs
        if not filepath.lower().endswith(".pdf"):
            messagebox.showerror("Error", "Solo se permiten archivos PDF.")
            return
        nuevo_pdf = duplicar_pdf(filepath, cantidad)
        messagebox.showinfo("Éxito", f"PDF generado: {nuevo_pdf}")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida.")

# ventana principal
root = tk.Tk()
root.title("Duplicador de Archivos")
root.geometry("400x180")

# widgets
tk.Label(root, text="Archivo:").pack(pady=5)
frame_archivo = tk.Frame(root)
frame_archivo.pack()
entry_archivo = tk.Entry(frame_archivo, width=35)
entry_archivo.pack(side=tk.LEFT, padx=5)
btn_buscar = tk.Button(frame_archivo, text="Buscar", command=seleccionar_archivo)
btn_buscar.pack(side=tk.LEFT)

tk.Label(root, text="¿Cuántas copias quieres?").pack(pady=5)
entry_cantidad = tk.Entry(root, width=10)
entry_cantidad.pack()

btn_duplicar = tk.Button(root, text="Duplicar", command=ejecutar_duplicado, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_duplicar.pack(pady=15)

root.mainloop()
