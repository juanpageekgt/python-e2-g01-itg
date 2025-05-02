import tkinter as tk

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menús en Tkinter")

        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        self.opciones = tk.Menu(self.menu)
        self.menu.add_cascade(label="Opciones", menu=self.opciones)
        self.opciones.add_command(label="Rojo", command=lambda: self.cambiar_color("red"))
        self.opciones.add_command(label="Verde", command=lambda: self.cambiar_color("green"))
        self.opciones.add_command(label="Azul", command=lambda: self.cambiar_color("blue"))

    def cambiar_color(self, color):
        self.root.config(bg=color)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = MenuApp(ventana)
    ventana.mainloop()