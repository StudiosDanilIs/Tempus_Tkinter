# LIBRERÍAS
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from tkinter.font import BOLD
import util.PhotoImagenes as utl
from Modelo.Login.VerificarCuenta import verificar_sesion as Verificar
from SubVentanas.Login.InfoSubventana import InformacionTempus as Info


class CreateLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x645")
        self.root.resizable(0, 0)
        self.root.title("Inicio de Sesion")
        self.estado_oculto = True
        self.subventana_abierta = False
        self.presionado = False
        logo = "imagenes\\logo.ico"
        self.root.iconbitmap(True, logo)

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#f0f0f0")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # incorporación de la imagen de la ventana principal
        self.username_label = Label(
            self.lgn_frame,
            text="Hola.",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 40),
        )
        self.username_label.place(x=60, y=62)

        self.username_label = Label(
            self.lgn_frame,
            text="Bienvenido!",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 46, "bold"),
        )
        self.username_label.place(x=60, y=125)

        # opcion del usuario para iniciar sesión o registrarse
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.username_label.place(x=80, y=263)
        # inserción de la entrada de texto para el usuario
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
        self.username_entry.bind("<Return>", self.pasar_usuario)

        # opcion del Clave para iniciar sesión o registrarse
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=80, y=333)

        # inserción de la entrada de texto para la Clave
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

        self.password_entry.bind("<Return>", self.ingresar_datos)

        self.clave = utl.leer_imagen(
            utl.resource_path("imagenes/clave.png"), size=(33, 33)
        )

        self.login = Button(
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
        self.login.place(x=40, y=360)

        self.usuario = utl.leer_imagen(
            utl.resource_path("imagenes/usuario.png"), size=(33, 33)
        )

        self.login = Button(
            self.lgn_frame,
            width=30,
            image=self.usuario,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.login.place(x=40, y=292)

        estado_boton = tk.BooleanVar(
            value=False
        )  # Inicializamos la variable como False
        marcar_boton = tk.Checkbutton(
            self.lgn_frame,
            fg="#232323",
            bg="#f0f0f0",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            text="Recordar Cuenta",
            variable=estado_boton,
        )
        marcar_boton.place(x=75, y=405)

        # botón para restaurar la contraseña y el usuario
        self.forgot_button = Button(
            self.lgn_frame,
            text="Restaurar Cuenta?",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            fg="#232323",
            bg="#f0f0f0",
            font=("Poppins", 12, "bold"),
            activebackground="#f0f0f0",
            cursor="hand2",
            command=lambda: self.mensaje_opciones(),
        )

        self.forgot_button.place(x=255, y=405)

        # botón para iniciar sesión
        self.boton_login = utl.leer_imagen(
            utl.resource_path("imagenes/boton1.png"), size=(170, 55)
        )
        self.login = Button(
            self.lgn_frame,
            image=self.boton_login,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Verificar(self),
        )
        self.login.place(x=75, y=460)

        # botón para iniciar sesión
        self.boton_login2 = utl.leer_imagen(
            utl.resource_path("imagenes/boton2.png"), size=(170, 55)
        )
        self.login2 = tk.Button(
            self.lgn_frame,
            image=self.boton_login2,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.mensaje_opciones(),
        )
        self.login2.place(x=240, y=460)

        # botón para iniciar sesión con la tecla enter
        self.login.bind("<Return>", (lambda event: Verificar(self)))

        # información de la versión del software
        self.forgot_button1 = Button(
            self.lgn_frame,
            text="Version Beta 1.0",
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
        self.forgot_button1.place(x=40, y=600)

        self.boton_login6 = utl.leer_imagen(
            utl.resource_path("imagenes/fondo2.jpg"), size=(500, 645)
        )
        self.login2 = Button(
            self.lgn_frame,
            image=self.boton_login6,
            width=500,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
        )
        self.login2.place(x=500)

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

    def mensaje_opciones(self):
        messagebox.showerror("Error", "Inicia Sesion para Usar esta Opcion")
        
        
if __name__ == "__main__":
    CreateLogin()
