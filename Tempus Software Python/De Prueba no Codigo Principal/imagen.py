import tkinter as tk

class FrameImagenTexto(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        imagen = tk.PhotoImage(file="./imagenes/logo.png")
        self.imagen = tk.Label(self, image=imagen)
        self.imagen.image = imagen  # Mantén una referencia para evitar que se elimine
        self.imagen.pack()
        self.label = tk.Label(self, text="Este texto cambiará de color")
        self.label.pack()

    def cambiar_color(self):
        if self["bg"] == "white":
            self.config(bg="blue")
            self.label["fg"] = "red"
            self.imagen["bg"] = "blue"
        else:
            self.config(bg="white")
            self.label["fg"] = "black"
            self.imagen["bg"] = "white"

ventana = tk.Tk()
ventana.title("Cambiar color de imagen y texto")

frame = FrameImagenTexto(ventana)
frame.pack()

boton = tk.Button(ventana, text="Click para cambiar color", command=frame.cambiar_color)
boton.pack()

ventana.mainloop()