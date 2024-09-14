import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox


def mostrar_opcion2(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.root2.title("Agregar Solicitudes")
    self.root2.geometry("1100x635")