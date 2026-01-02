import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


def run():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Aplicación de Escritorio")
    ventana.geometry("800x600")
    
    # Crear área de texto con scroll
    texto_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=25)
    texto_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
    
    def abrir_archivo():
        """Abre un archivo de texto"""
        archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    texto_area.delete(1.0, tk.END)
                    texto_area.insert(1.0, contenido)
                ventana.title(f"Aplicación de Escritorio - {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{str(e)}")
    
    def guardar_archivo():
        """Guarda el contenido en un archivo"""
        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )
        if archivo:
            try:
                contenido = texto_area.get(1.0, tk.END)
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                messagebox.showinfo("Éxito", "Archivo guardado correctamente")
                ventana.title(f"Aplicación de Escritorio - {archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    
    # Crear barra de menú
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)
    
    # Crear menú Archivo
    menu_archivo = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
    
    # Agregar opciones al menú Archivo
    menu_archivo.add_command(label="Abrir", command=abrir_archivo, accelerator="Ctrl+O")
    menu_archivo.add_command(label="Guardar", command=guardar_archivo, accelerator="Ctrl+S")
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=ventana.quit)
    
    # Atajos de teclado
    ventana.bind('<Control-o>', lambda e: abrir_archivo())
    ventana.bind('<Control-s>', lambda e: guardar_archivo())
    
    # Iniciar la aplicación
    ventana.mainloop()


if __name__ == '__main__':
    run()