import tkinter as tk
from tkinter import *
from tkinter import Frame
import tkinter.messagebox as messagebox

class VentanaPrincipal:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.resizable(0, 0)
        self.root2.geometry("500x400")

    def cerrar(self):
        self.root2.destroy()

# Crear una instancia de la ventana principal
if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.root2.mainloop()