import tkinter as tk
from tkinter import PhotoImage


class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inicio - Tempus Software")
        self.root.geometry("1200x700")
        self.root.resizable(0, 0)


if __name__ == "__main__":
    app = TempusPrincipal()
    app.root.mainloop()
