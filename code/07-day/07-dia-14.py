import tkinter as tk # Importamos Tkinter y lo abreviamos como "tk"

class Formulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario")

        self.label = tk.Label(root, text="Escribe tu nombre:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.boton = tk.Button(root, text="Saludar", command=self.saludar)
        self.boton.grid(row=1, column=0, columnspan=2, pady=10)

        self.resultado = tk.Label(root, text="")
        self.resultado.grid(row=2, column=0, columnspan=2, pady=10)

    def saludar(self):
        nombre = self.entry.get()
        self.resultado.config(text=f"¡Hola, {nombre}!")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Formulario(ventana)
    ventana.mainloop()