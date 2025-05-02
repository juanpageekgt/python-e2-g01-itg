import tkinter as tk

class MiAplicación:
    def __init__(self, root):
        self.root = root # guardamos la ventana principal
        self.root.title("Mi Primera Aplicación con Tkinter")

        # Crear un widget de etiqueta (label)
        self.label = tk.Label(root, text="Bienvenido a Tkinter GUI", font=("Arial", 16))
        self.label.pack(pady=20)  # Mostramos la equiqueta en la ventana

        # Creamos un bótón que cierra la aplicación
        self.boton = tk.Button(root, text="Salir", command=self.salir)
        self.boton.pack(pady=10)
    
    def salir(self):
        self.root.destroy() # Cierra la ventana principal


# main program
if __name__ == "__main__":
    ventana = tk.Tk()  # Creamos la ventana principal
    app = MiAplicación(ventana)
    ventana.mainloop() # Mantener la ventana abierta