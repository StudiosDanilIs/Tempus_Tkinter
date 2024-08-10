import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from util.Funciones import actualizar_reloj
from SubVentanas.Inicio.SubEstructuraLogin import SubventanaLogin as MySubventana


def mostrar_opcion1(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.subventana_abierta = False
    self.root2.title("Ventana Principal")

    # Muestra un RELOJ DIGITAL en la ventana principal
    self.label_reloj = tk.Label(
        self.label_info, width=20, font=("Poppins", 48), bg="#f0f0f0", fg="#1E90FF"
    )
    self.label_reloj.place(x=90, y=200)

    # Muestra un CALENDARIO en la ventana principal
    self.label_dia = tk.Label(
        self.label_info, font=("Poppins", 24), bg="#f0f0f0", fg="#1E90FF"
    )
    self.label_dia.place(x=60, y=120)
    # Actualizar el reloj y el día cada segundo
    actualizar_reloj(self)

    # Etiqueta de bienvenida
    self.title_label = Label(
        self.label_info,
        text=f"Bienvenido de vuelta! {self.nombre_cuenta}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Montserrat", 20),
    )
    self.title_label.place(x=60, y=80)

    # Etiqueta de Eslogan
    self.eslogan_label = Label(
        self.label_info,
        text="Tu aliado tecnológico: eficiencia y confianza al\n alcance de tu mano.",
        bg="#f0f0f0",
        fg="#000000",
        font=("Avenir", 13),
    )
    self.eslogan_label.place(x=60, y=160)

    # Etiqueta de permisos
    self.rol_label = Button(
        self.label_info,
        text="Nivel de Permisos:",
        font=("Avenir", 14),
        width=30,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#3047ff",
        fg="white",
        command=lambda: MySubventana(self),
    )
    self.rol_label.place(x=60, y=200)
