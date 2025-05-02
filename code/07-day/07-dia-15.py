import tkinter as tk # Importamos Tkinter y lo abreviamos como "tk"

class Dibujo:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujo con Canvas")

        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.dibujar)

    def dibujar(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="red")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Dibujo(ventana)
    ventana.mainloop()