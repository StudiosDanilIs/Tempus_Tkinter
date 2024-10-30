import re
import tkinter as tk
from tkinter import *
import util.PhotoImagenes as utl
from Visual.Extras.InformacionVersion import InformacionTempus as Info
from Visual.Extras.CrearCuenta import CrearUsuario
from Visual.Extras.LoginRecuperar import LoginRecuperar
from Modelo.Login.VerificarCuenta import verificar_sesion as Verificar


class CreateLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.geometry("1000x645")
        self.root.title("Inicio de Sesión")
        self.presionado = False
        self.estado_oculto = True
        self.subventana_abierta = False
        icono = utl.resource_path("imagenes/logo2.ico")
        self.root.iconbitmap(True, icono)

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#f0f0f0")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Título de la ventana principal
        self.title_label = Label(
            self.lgn_frame,
            text="Hola.",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 40),
        )
        self.title_label.place(x=60, y=62)

        self.title2_label = Label(
            self.lgn_frame,
            text="Bienvenido!",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 46, "bold"),
        )
        self.title2_label.place(x=60, y=125)

        # Area del Usuario
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.username_label.place(x=80, y=263)

        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            width=35,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.username_entry.place(x=80, y=290, height=40)
        self.username_entry.bind(
            "<Return>", lambda event: self.password_entry.focus_set()
        )

        self.usuario = utl.leer_imagen("usuario.png", size=(35, 35))
        self.imagen_user_boton = Button(
            self.lgn_frame,
            width=34,
            image=self.usuario,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.imagen_user_boton.place(x=35, y=292)

        # Area de la Contraseña
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=80, y=333)

        self.password_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            width=35,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            show="*",
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.password_entry.place(x=80, y=360, height=40)
        self.password_entry.bind("<Return>", lambda event: Verificar(self))

        self.clave = utl.leer_imagen("clave.png", size=(35, 35))
        self.imagen_clave_boton = Button(
            self.lgn_frame,
            width=34,
            image=self.clave,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.Revertir(self),
        )
        self.imagen_clave_boton.place(x=35, y=362)

        # botón para restaurar la Cuenta
        self.recuperar_button = Button(
            self.lgn_frame,
            text="Recuperar cuenta?",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            cursor="hand2",
            command=lambda: LoginRecuperar(self.root),
        )
        self.recuperar_button.place(x=80, y=415)
        
        
        self.title_proteccion = Label(
            self.lgn_frame,
            text="Dolphin\nSecureRead",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 12, "bold"),
        )
        self.title_proteccion.place(x=255, y=410)
        
        self.imagen_proteccion = utl.leer_imagen("protegido.png", size=(43, 43))
        self.label_imagen_proteccion = Label(
            self.lgn_frame,
            image=self.imagen_proteccion,
            width=50,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            fg="white",
        )
        self.label_imagen_proteccion.place(x=355, y=410)
        

        # botón para iniciar sesión
        self.imagen_iniciar_sesion = utl.leer_imagen(
            "boton_iniciar_sesion.png", size=(170, 55)
        )
        self.login_boton = tk.Button(
            self.lgn_frame,
            image=self.imagen_iniciar_sesion,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Verificar(self),
        )
        self.login_boton.place(x=75, y=460)

        # botón para registrarse
        self.imagen_registrarse = utl.leer_imagen(
            "boton_registrarse.png", size=(170, 55)
        )
        self.registrarse_boton = tk.Button(
            self.lgn_frame,
            image=self.imagen_registrarse,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: CrearUsuario(self.root),
        )
        self.registrarse_boton.place(x=240, y=460)

        self.update_label = Label(
            self.lgn_frame,
            text="©Tempus2024",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
        )
        self.update_label.place(x=270, y=604)

        # Version del Programa
        self.version_boton = Button(
            self.lgn_frame,
            text="Versión 2.4.7",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            cursor="hand2",
            command=lambda: Info(self),
        )
        self.version_boton.place(x=35, y=600)

        # Fondo de la Ventana de Login
        self.imagen_fondo_login = utl.leer_imagen("fondo2.jpg", size=(500, 645))
        self.fondo_label = Label(
            self.lgn_frame,
            image=self.imagen_fondo_login,
            width=505,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
        )
        self.fondo_label.place(x=500)

        # Abrir la Ventana de Login
        self.root.mainloop()

    # Validación de Entradas de Texto para el Usuario y la Contraseña
    def validate_tab(self, new_value):
        pattern = r"^[a-zA-Z0-9@._-]*$"  # Incluye los símbolos permitidos

        # Verificar si hay espacios
        if " " in new_value:
            return False

        # Verificar la longitud
        if len(new_value) > 40:
            return False

        # Verificar el patrón
        if not re.match(pattern, new_value):
            return False

        # Verificar que solo haya un símbolo especial de cada tipo
        if (
            new_value.count("@") > 1
            or new_value.count(".") > 1
            or new_value.count("_") > 1
            or new_value.count("-") > 1
        ):
            return False

        return True

    # Revelar o Ocultar la Contraseña en el Campo de Entrada de Texto para la Contraseña
    def Revertir(self, event):
        self.estado_oculto = not self.estado_oculto
        if self.estado_oculto:
            self.password_entry.config(show="*")  # Mostrar asteriscos
        else:
            self.password_entry.config(show="")  # Mostrar texto normal


if __name__ == "__main__":
    CreateLogin()
