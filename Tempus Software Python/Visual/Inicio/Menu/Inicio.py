from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl
from tkinter import Frame
import tkinter.messagebox as messagebox
from SubVentanas.Inicio.SubEstructuraLogin import SubventanaLogin as MySubventana
from util.Funciones import actualizar_reloj


def mostrar_opcion1(self):
    self.limpiar_contenido()
    self.subventana_abierta = False
    self.root2.title("Inicio Sistema")   
    
    self.label_reloj = tk.Label(self.label_info, width=20, font=("Poppins", 48), bg="#f0f0f0", fg="#1E90FF")
    self.label_reloj.place(x=90, y=200)

    self.label_dia = tk.Label(self.label_info, font=("Poppins", 24), bg="#f0f0f0", fg="#1E90FF")
    self.label_dia.place(x=60, y=120)

    actualizar_reloj(self)
        
      
    # Etiqueta de bienvenida
    self.username_label = Label(
        self.label_info,
        text="Bienvenido de vuelta!",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Montserrat", 20),
    )
    self.username_label.place(x=60, y=80)

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