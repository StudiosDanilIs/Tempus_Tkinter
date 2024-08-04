from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl
from tkinter import Frame
import tkinter.messagebox as messagebox

from Visual.Inicio.SubEstructuraLogin import SubventanaLogin as MySubventana


def mostrar_opcion1(self):
    self.limpiar_contenido()
    self.subventana_abierta = False
        
    logo = utl.leer_imagen(utl.resource_path("imagenes/logo.png"), size=(200, 200))
    self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
    self.logo_inicio_label.image = logo
    self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

    # Etiqueta de bienvenida
    self.username_label = Label(
        self.label_info,
        text="Welcome to\n Tempus Software.",
        anchor="center",
        bg="#FFFFFF",
        fg="#000000",
        font=("Hipstelvetica", 20),
    )
    self.username_label.place(relx=0.5, rely=0.60, anchor=CENTER)

    # Etiqueta de Eslogan
    self.eslogan_label = Label(
        self.label_info,
        text="Tu aliado tecnológico: eficiencia y confianza al\n alcance de tu mano.",
        bg="#FFFFFF",
        fg="#000000",
        font=("Avenir", 13),
    )
    self.eslogan_label.place(relx=0.5, rely=0.70, anchor=CENTER)

    # Etiqueta de permisos
    self.rol_label = Button(
        self.label_info,
        text=f"Nivel de Permisos: {self.rol_programa}",
        font=("Avenir", 14),
        width=30,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#3047ff",
        fg="white",
        command=lambda: MySubventana(self),
    )
    self.rol_label.place(relx=0.5, rely=0.80, anchor=CENTER)
