import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from Modelo.Inicio.RecuperarCuenta import *
import util.PhotoImagenes as utl


def SubventanaLogin(self):
    if not self.subventana_abierta:
        subventana = tk.Toplevel()
        subventana.title("Herramientas de Usuario")
        subventana.geometry("700x350")
        subventana.resizable(0, 0)
        subventana.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

        # frame de recupera cuenta
        self.lgn_frame = Frame(subventana, bg="#FFFFFF")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.username_label = Label(
            self.lgn_frame,
            text="Herramientas de Usuario",
            anchor="w",
            bg="#FFFFFF",
            fg="#1E90FF",
            font=("Hipstelvetica", 20),
        )
        self.username_label.place(x=160, y=50)

        # incorporación de la imagen de la ventana principal
        address = utl.leer_imagen(
            utl.resource_path("imagenes/agregar_usuario.png"), size=(120, 120)
        )
        self.sign_in_image_label = Button(
            self.lgn_frame,
            width=200,
            image=address,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
        )
        self.sign_in_image_label.image = address
        self.sign_in_image_label.place(x=60, y=130)

        # incorporación de la imagen de la ventana principal
        delete = utl.leer_imagen(
            utl.resource_path("imagenes/quitar_usuario.png"), size=(120, 120)
        )
        self.sign_in_image_label = Button(
            self.lgn_frame,
            width=200,
            image=delete,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
        )
        self.sign_in_image_label.image = delete
        self.sign_in_image_label.place(x=250, y=130)

        # incorporación de la imagen de la ventana principal
        update = utl.leer_imagen(
            utl.resource_path("imagenes/modificar_usuario.png"), size=(120, 120)
        )
        self.sign_in_image_label = Button(
            self.lgn_frame,
            width=200,
            image=update,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
        )
        self.sign_in_image_label.image = update
        self.sign_in_image_label.place(x=440, y=130)

        self.subventana_abierta = True
        
        def cerrar_sesion(self):
            self.subventana_abierta = False
            subventana.destroy()