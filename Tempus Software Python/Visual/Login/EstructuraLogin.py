# LIBRERÍAS
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from tkinter.font import BOLD
import util.PhotoImagenes as utl
from Modelo.Login.VerificarCuenta import verificar_sesion as Verificar
from Visual.Login.InfoSubventana import InformacionTempus as Info


class CreateLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1100x645")
        self.root.resizable(0, 0)
        self.root.title("Login - Tempus Software")
        self.estado_oculto = True
        self.subventana_abierta = False
        self.presionado = False

        logo = "imagenes\\logo.ico"
        self.root.iconbitmap(True, logo)

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#FFFFFF")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # incorporación de la imagen de la ventana principal
        self.username_label = Label(
            self.lgn_frame,
            text="Hola.",
            anchor="w",
            bg="#FFFFFF",
            fg="#0000FF",
            font=("Montserrat", 40),
        )
        self.username_label.place(x=60, y=62)

        self.username_label = Label(
            self.lgn_frame,
            text="Bienvenido!",
            anchor="w",
            bg="#FFFFFF",
            fg="#0000FF",
            font=("Montserrat", 46, "bold"),
        )
        self.username_label.place(x=60, y=125)

        # opcion del usuario para iniciar sesión o registrarse
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#FFFFFF",
            fg="#5E5E5E",
            font=("Poppins", 13, "bold"),
        )
        self.username_label.place(x=75, y=223)
        # inserción de la entrada de texto para el usuario
        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#5E5E5E",
            relief=tk.FLAT,
            fg="#5E5E5E",
            font=("Poppins", 12, "bold"),
            insertbackground="#5E5E5E",
            width=35,
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.username_entry.place(x=75, y=250, height=40)
        self.username_entry.bind("<Return>", self.pasar_usuario)

        # opcion del Clave para iniciar sesión o registrarse
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#FFFFFF",
            fg="#5E5E5E",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=75, y=293)

        # inserción de la entrada de texto para la Clave
        self.password_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#5E5E5E",
            relief=tk.FLAT,
            fg="#5E5E5E",
            font=("Poppins", 12, "bold"),
            insertbackground="#5E5E5E",
            width=35,
            show="*",
            validate="key",
            validatecommand=(self.root.register(self.validate_tab), "%P"),
        )
        self.password_entry.place(x=75, y=320, height=40)

        self.password_entry.bind("<Return>", self.ingresar_datos)

        self.clave = utl.leer_imagen(
            utl.resource_path("imagenes/clave.png"), size=(33, 33)
        )

        self.login = Button(
            self.lgn_frame,
            width=30,
            image=self.clave,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.Revertir(self),
        )
        self.login.place(x=40, y=320)

        self.usuario = utl.leer_imagen(
            utl.resource_path("imagenes/usuario.png"), size=(33, 33)
        )

        self.login = Button(
            self.lgn_frame,
            width=30,
            image=self.usuario,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.login.place(x=40, y=252)

        estado_boton = tk.BooleanVar(
            value=False
        )  # Inicializamos la variable como False
        marcar_boton = tk.Checkbutton(
            self.lgn_frame,
            fg="#5E5E5E",
            bg="#FFFFFF",
            font=("Poppins", 12, "bold"),
            activebackground="#FFFFFF",
            text="Recordar Cuenta",
            variable=estado_boton,
        )
        marcar_boton.place(x=70, y=365)

        # botón para restaurar la contraseña y el usuario
        self.forgot_button = Button(
            self.lgn_frame,
            text="Restaurar Cuenta?",
            relief=FLAT,
            borderwidth=0,
            background="#FFFFFF",
            fg="#5E5E5E",
            bg="#FFFFFF",
            font=("Poppins", 12, "bold"),
            activebackground="#FFFFFF",
            cursor="hand2",
        )

        self.forgot_button.place(x=250, y=365)

        # botón para iniciar sesión
        self.boton_login = utl.leer_imagen(
            utl.resource_path("imagenes/boton1.png"), size=(170, 55)
        )
        self.login = Button(
            self.lgn_frame,
            image=self.boton_login,
            width=170,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Verificar(self),
        )
        self.login.place(x=70, y=420)

        # botón para iniciar sesión
        self.boton_login2 = utl.leer_imagen(
            utl.resource_path("imagenes/boton2.png"), size=(170, 55)
        )
        self.login2 = tk.Button(
            self.lgn_frame,
            image=self.boton_login2,
            width=170,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.login2.place(x=230, y=420)

        # botón para iniciar sesión con la tecla enter
        self.login.bind("<Return>", (lambda event: Verificar(self)))

        self.separator = tk.Frame(self.lgn_frame, width=250, height=2, bg="#666666")
        self.separator.place(x=110, y=510)

        # información de la versión del software
        self.forgot_button = Button(
            self.lgn_frame,
            text="Redes Sociales",
            relief=FLAT,
            borderwidth=0,
            background="#FFFFFF",
            fg="#5E5E5E",
            bg="#FFFFFF",
            font=("Poppins", 12, "bold"),
            activebackground="#FFFFFF",
            cursor="hand2",
        )
        self.forgot_button.place(x=70, y=540)

        self.boton_login3 = utl.leer_imagen(
            utl.resource_path("imagenes/facebook.png"), size=(35, 35)
        )
        self.login2 = Button(
            self.lgn_frame,
            image=self.boton_login3,
            width=50,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=self.abrir_perfil_facebook,
        )
        self.login2.place(x=220, y=530)

        self.boton_login4 = utl.leer_imagen(
            utl.resource_path("imagenes/whatsapp.png"), size=(35, 35)
        )
        self.login2 = Button(
            self.lgn_frame,
            image=self.boton_login4,
            width=50,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=self.abrir_perfil_whatsapp,
        )
        self.login2.place(x=265, y=530)

        self.boton_login5 = utl.leer_imagen(
            utl.resource_path("imagenes/instagram.png"), size=(35, 35)
        )
        self.login2 = Button(
            self.lgn_frame,
            image=self.boton_login5,
            width=50,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=self.abrir_perfil_instagram,
        )
        self.login2.place(x=310, y=530)

        self.forgot_button1 = Button(
            self.lgn_frame,
            text="Version Beta 1.0",
            relief=FLAT,
            borderwidth=0,
            background="#FFFFFF",
            fg="#5E5E5E",
            bg="#FFFFFF",
            font=("Poppins", 12, "bold"),
            activebackground="#FFFFFF",
            cursor="hand2",
            command=lambda: Info(self=self),
        )
        self.forgot_button1.place(x=40, y=600)

        self.boton_login9 = utl.leer_imagen(
            utl.resource_path("imagenes/pincel.png"), size=(35, 35)
        )
        self.login3 = Button(
            self.lgn_frame,
            image=self.boton_login9,
            width=50,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=self.cambio_fondo,
        )
        self.login3.place(x=180, y=600)

        self.boton_login6 = utl.leer_imagen(
            utl.resource_path("imagenes/fondo1.jpg"), size=(700, 700)
        )
        self.login2 = Button(
            self.lgn_frame,
            image=self.boton_login6,
            width=600,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
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

    def abrir_perfil_instagram(self):
        # Abre el perfil de Instagram en el navegador
        perfil_instagram = (
            "https://www.instagram.com/tempus.09/"  # Reemplaza con el perfil deseado
        )
        webbrowser.open(perfil_instagram)

    def abrir_perfil_facebook(self):
        # Abre el perfil de Instagram en el navegador
        perfil_instagram = "https://www.facebook.com/profile.php?id=100071946285434"  # Reemplaza con el perfil deseado
        webbrowser.open(perfil_instagram)

    def abrir_perfil_whatsapp(self):
        # Abre el perfil de Instagram en el navegador
        perfil_instagram = (
            "https://wa.me/+584247233495"  # Reemplaza con el perfil deseado
        )
        webbrowser.open(perfil_instagram)

    def cambio_fondo(self):
        self.presionado = not self.presionado
        if self.presionado:
            self.boton_login7 = utl.leer_imagen(
                utl.resource_path("imagenes/Fondo2.jpg"), size=(700, 700)
            )
            self.login2.config(image=self.boton_login7)
        else:
            self.boton_login10 = utl.leer_imagen(
                utl.resource_path("imagenes/Fondo3.jpg"), size=(700, 700)
            )
            self.login2.config(image=self.boton_login10)


if __name__ == "__main__":
    CreateLogin()
