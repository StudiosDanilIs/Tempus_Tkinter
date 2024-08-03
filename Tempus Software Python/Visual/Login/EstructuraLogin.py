# LIBRERÍAS
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import util.PhotoImagenes as utl
from Modelo.Login.VerificarCuenta import verificar_sesion as Verificar
from Visual.Login.InfoSubventana import InformacionTempus as Info


class CreateLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x645")
        self.root.resizable(0, 0)
        self.root.title("Login - Tempus Software")
        self.estado_oculto = True
        self.subventana_abierta = False

        logo = "imagenes\\logo.ico"
        self.root.iconbitmap(True, logo)

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#E6F0F3")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # incorporación de la imagen de la ventana principal
        logo = utl.leer_imagen(utl.resource_path("imagenes/logo.png"), size=(242, 242))
        self.sign_in_image_label = Label(self.lgn_frame, image=logo, bg="#E6F0F3")
        self.sign_in_image_label.image = logo
        self.sign_in_image_label.place(x=130, y=30)

        # opcion del usuario para iniciar sesión o registrarse
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#E6F0F3",
            fg="#1E90FF",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.place(x=35, y=285)
        # inserción de la entrada de texto para el usuario
        self.username_entry = Entry(
            self.lgn_frame,
            relief=FLAT,
            bg="#E6F0F3",
            fg="#0046A4",
            font=("Poppins", 12, "bold"),
            insertbackground="#0046A4",
            width=42,
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.username_entry.place(x=40, y=315)
        self.username_entry.bind("<Return>", self.pasar_usuario)

        self.username_line = Canvas(
            self.lgn_frame, width=385, height=2.0, bg="#1E90FF", highlightthickness=0
        )
        self.username_line.place(x=40, y=340)

        # opcion del Clave para iniciar sesión o registrarse
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#E6F0F3",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=35, y=375)

        # inserción de la entrada de texto para la Clave
        self.password_entry = Entry(
            self.lgn_frame,
            relief=FLAT,
            bg="#E6F0F3",
            fg="#0046A4",
            font=("Poppins", 12, "bold"),
            show="*",
            width=42,
            insertbackground="#0046A4",
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.password_entry.place(x=40, y=402)

        self.password_entry.bind("<Return>", self.ingresar_datos)

        self.password_line = Canvas(
            self.lgn_frame, width=385, height=2.0, bg="#1E90FF", highlightthickness=0
        )
        self.password_line.place(x=40, y=427)

        self.oculto = utl.leer_imagen(
            utl.resource_path("imagenes/oculto.png"), size=(33, 33)
        )
        self.login = Button(
            self.lgn_frame,
            width=30,
            image=self.oculto,
            bg="#E6F0F3",
            activebackground="#E6F0F3",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.Revertir(self),
        )
        self.login.place(x=425, y=400)

        # botón para restaurar la contraseña y el usuario
        self.forgot_button = Button(
            self.lgn_frame,
            text="Restaurar Cuenta",
            font=("Poppins", 12, "bold"),
            fg="#1E90FF",
            relief=FLAT,
            activebackground="#E6F0F3",
            borderwidth=0,
            background="#E6F0F3",
            cursor="hand2",
        )

        self.forgot_button.place(x=170, y=460)

        # botón para iniciar sesión
        self.boton_login = utl.leer_imagen(
            utl.resource_path("imagenes/boton.png"), size=(200, 45)
        )
        self.login = Button(
            self.lgn_frame,
            width=280,
            image=self.boton_login,
            bg="#E6F0F3",
            activebackground="#E6F0F3",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Verificar(self),
        )
        self.login.place(x=100, y=500)

        # botón para iniciar sesión con la tecla enter
        self.login.bind("<Return>", (lambda event: Verificar(self)))

        # información de la versión del software
        self.forgot_button = Button(
            self.lgn_frame,
            text="Version Alpha 2.0",
            font=("Poppins", 12, "bold"),
            fg="#1E90FF",
            relief=FLAT,
            activebackground="#E6F0F3",
            borderwidth=0,
            background="#E6F0F3",
            cursor="hand2",
            command=lambda: Info(self=self),
        )
        self.forgot_button.place(x=170, y=585)

        self.root.mainloop()

    def pasar_usuario(self, event):
        self.password_entry.focus_set()

    def ingresar_datos(self, event):
        if event.keysym == "Return":
            Verificar(self)

    def validate_tab(self, new_value):
        # Verifica que no haya espacios en blanco
        return not (" " in new_value) and len(new_value) <= 50

    def Revertir(self, event):
        self.estado_oculto = not self.estado_oculto
        # Actualiza el modo de visualización del campo de entrada
        if self.estado_oculto:
            self.password_entry.config(show="*")  # Mostrar asteriscos
        else:
            self.password_entry.config(show="")  # Mostrar texto normal


if __name__ == "__main__":
    CreateLogin()
