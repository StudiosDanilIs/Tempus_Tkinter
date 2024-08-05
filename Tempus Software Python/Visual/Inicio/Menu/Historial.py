from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl
from tkinter import Frame
import tkinter.messagebox as messagebox

def mostrar_opcion5(self):
    self.limpiar_contenido()
    self.root2.title("Historial")
    logo = utl.leer_imagen(utl.resource_path("imagenes/menu/historial2.png"), size=(200, 200))
    self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
    self.logo_inicio_label.image = logo
    self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)