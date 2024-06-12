import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD


def mostrar_cliente(self):
    subventana = tk.Toplevel()
    subventana.title("Tempus - Clientes")
    subventana.geometry("420x490")

    # Username label and entry
    self.nombre_label = Label(
        subventana,
        text="Nombre",
        justify=LEFT,
        anchor="w",
        bg="#FFFFFF",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.nombre_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")