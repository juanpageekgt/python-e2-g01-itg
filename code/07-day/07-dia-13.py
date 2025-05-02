import tkinter as tk

class MiPrimeraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Ejercicio Guiado')

        self.label = tk.Label(root, text="!Bienvenido!", font=("Arial", 16))
        self.label.pack(pady=20)

        self.boton = tk.Button(root, text="Cambiar Texto", command=self.cambiar_texto)
        self.boton.pack(pady=10)
    
    def cambiar_texto(self):
        self.label.config(text="!Texto cambiado!")


# main 
if __name__ == "__main__":
    ventana = tk.Tk()
    app = MiPrimeraGUI(ventana)
    ventana.mainloop()