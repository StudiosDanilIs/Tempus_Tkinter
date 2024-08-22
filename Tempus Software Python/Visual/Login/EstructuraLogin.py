import re
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
import util.PhotoImagenes as utl
from SubVentanas.Login.InfoSubventana import InformacionTempus as Info
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
        logo = "imagenes\\logo2.ico"
        self.root.iconbitmap(True, logo)

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
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.username_label.place(x=80, y=263)

        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#232323",
            relief=tk.FLAT,
            fg="#232323",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#232323",
            width=35,
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.username_entry.place(x=80, y=290, height=40)
        self.username_entry.bind(
            "<Return>", lambda event: self.password_entry.focus_set()
        )

        self.usuario = utl.leer_imagen(
            utl.resource_path("imagenes/usuario.png"), size=(33, 33)
        )
        self.imagen_user_boton = Button(
            self.lgn_frame,
            width=30,
            image=self.usuario,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.imagen_user_boton.place(x=40, y=292)

        # Area de la Contraseña
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=80, y=333)

        self.password_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#232323",
            relief=tk.FLAT,
            fg="#232323",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#232323",
            width=35,
            show="*",
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.password_entry.place(x=80, y=360, height=40)
        self.password_entry.bind("<Return>", lambda event: Verificar(self))

        self.clave = utl.leer_imagen(
            utl.resource_path("imagenes/clave.png"), size=(33, 33)
        )
        self.imagen_clave_boton = Button(
            self.lgn_frame,
            width=30,
            image=self.clave,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.Revertir(self),
        )
        self.imagen_clave_boton.place(x=40, y=362)

        # Boton de Chetboc para guardar la cuenta
        estado_boton = tk.BooleanVar(value=False)
        self.marcar_boton = tk.Checkbutton(
            self.lgn_frame,
            fg="#232323",
            bg="#f0f0f0",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            text="Guardar Cuenta",
            variable=estado_boton,
        )
        self.marcar_boton.place(x=75, y=405)

        # botón para restaurar la Cuenta
        self.recuperar_button = Label(
            self.lgn_frame,
            text="Recuperar Cuenta?",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            fg="#232323",
            bg="#f0f0f0",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            cursor="hand2",
        )
        self.recuperar_button.place(x=255, y=410)

        # botón para iniciar sesión
        self.imagen_iniciar_sesion = utl.leer_imagen(
            utl.resource_path("imagenes/boton_iniciar_sesion.png"), size=(170, 55)
        )
        self.login_boton = Button(
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
        self.login_boton.bind("<Return>", (lambda event: Verificar(self)))

        # botón para registrarse
        self.imagen_registrarse = utl.leer_imagen(
            utl.resource_path("imagenes/boton_registrarse.png"), size=(170, 55)
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
            command=lambda: self.mensaje_error(),
        )
        self.registrarse_boton.place(x=240, y=460)

        # Actualizar el Programa
        self.imagen_update = utl.leer_imagen(
            utl.resource_path("imagenes/git.png"), size=(35, 35)
        )
        self.update_boton = Button(
            self.lgn_frame,
            image=self.imagen_update,
            width=50,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.abrir_perfil_github(),
        )
        self.update_boton.place(x=40, y=595)

        self.update_label = Label(
            self.lgn_frame,
            text="Actualizar",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            fg="#232323",
            bg="#f0f0f0",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
        )
        self.update_label.place(x=82, y=604)

        # Version del Programa
        self.version_boton = Button(
            self.lgn_frame,
            text="Versión Beta 3.5.1",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            fg="#232323",
            bg="#f0f0f0",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            cursor="hand2",
            command=lambda: Info(self=self),
        )
        self.version_boton.place(x=270, y=600)

        # Fondo de la Ventana de Login
        self.imagen_fondo_login = utl.leer_imagen(
            utl.resource_path("imagenes/fondo2.jpg"), size=(500, 645)
        )
        self.fondo_label = Label(
            self.lgn_frame,
            image=self.imagen_fondo_login,
            width=501,
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

    # Mensaje para Opciones no Disponibles en EL Programa
    def mensaje_error(self):
        messagebox.showerror("Error", "Inicia Sesion para Usar esta Opcion")

    # Abrir el Perfil de GitHub para Actualizar el Programa
    def abrir_perfil_github(self):
        # Abre el perfil de Instagram en el navegador
        perfil_github = "https://github.com/StudiosDanilIs/Tempus_Tkinter"  # Reemplaza con el perfil deseado
        webbrowser.open(perfil_github)


if __name__ == "__main__":
    CreateLogin()
