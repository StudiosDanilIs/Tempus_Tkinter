import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
import util.PhotoImagenes as utl
from Modelo.Inicio.RecuperarCuenta import *


def SubventanaLogin(self):
    if not self.subventana_abierta:
        subventana = tk.Toplevel()
        subventana.title("Herramientas de Usuario")
        subventana.geometry("700x350")
        subventana.resizable(0, 0)
        subventana.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

        # Creación de un frame para el contenido de la subventana
        self.lgn_frame = Frame(subventana, bg="#FFFFFF")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        self.informacion_ventana_label = Label(
            self.lgn_frame,
            text="Herramientas de Usuario",
            anchor="w",
            bg="#FFFFFF",
            fg="#1E90FF",
            font=("Hipstelvetica", 20),
        )
        self.informacion_ventana_label.place(x=160, y=50)

        # Agregar usuario
        agregar = utl.leer_imagen(
            utl.resource_path("imagenes/agregar_usuario.png"), size=(120, 120)
        )
        self.boton_agregar = Button(
            self.lgn_frame,
            width=200,
            image=agregar,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
        )
        self.boton_agregar.image = agregar
        self.boton_agregar.place(x=60, y=130)

        # Eliminar usuario
        borrar = utl.leer_imagen(
            utl.resource_path("imagenes/quitar_usuario.png"), size=(120, 120)
        )
        self.boton_borrar = Button(
            self.lgn_frame,
            width=200,
            image=borrar,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
        )
        self.boton_borrar.image = borrar
        self.boton_borrar.place(x=250, y=130)

        # Modificar usuario
        modificar = utl.leer_imagen(
            utl.resource_path("imagenes/modificar_usuario.png"), size=(120, 120)
        )
        self.boton_modificar = Button(
            self.lgn_frame,
            width=200,
            image=modificar,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
        )
        self.boton_modificar.image = modificar
        self.boton_modificar.place(x=440, y=130)

        # Abrir solo la subventana si no está abierta
        self.subventana_abierta = True

        def cerrar_sesion(self):
            self.subventana_abierta = False
            subventana.destroy()
