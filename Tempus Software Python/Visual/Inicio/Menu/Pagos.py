import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox


def mostrar_opcion4(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.root2.title("Verificar Pagos")

    # Informacion de la ventana
    logo = utl.leer_imagen(
        utl.resource_path("imagenes/menu/salir2.png"), size=(200, 200)
    )
    self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
    self.logo_inicio_label.image = logo
    self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
