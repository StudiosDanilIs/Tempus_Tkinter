# LIBRERÍAS
from tkinter import *
from PIL import ImageTk, Image as imim
import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import util.PhotoImagenes as utl


# módulos de la aplicación
from Modelo.Login.VerificarCuenta import verificar_sesion as Verificar
from Visual.Login.InfoSubventana import InformacionTempus as Info


class CreateLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("480x670")
        self.root.resizable(0, 0)
        self.root.title("Login - Tempus Software")       
        
        logo = "imagenes\\logo.ico"
        self.root.iconbitmap(True, logo) 

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#E6F0F3")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # incorporación de la imagen de la ventana principal
        logo = utl.leer_imagen("imagenes//logo.png", (242, 242))
        self.sign_in_image_label = Label(self.lgn_frame, image=logo, bg="#E6F0F3")
        self.sign_in_image_label.image = logo
        self.sign_in_image_label.pack(side="top", fill=tk.X, pady=30)


        # opcion del usuario para iniciar sesión o registrarse
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#E6F0F3",
            fg="#1E90FF",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.pack(fill=tk.X, padx=25, pady=8)
        # inserción de la entrada de texto para el usuario
        vcmd = self.root.register(self.validate_tab)
        self.username_entry = Entry(
            self.lgn_frame,
            relief=FLAT,
            bg="#E6F0F3",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#1E90FF",
            validate="key",
            validatecommand=(vcmd, "%P"),
        )
        self.username_entry.pack(fill=tk.X, padx=30, pady=0)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#1E90FF", highlightthickness=0
        )
        self.username_line.pack(fill=tk.X, padx=30, pady=1)

        # opcion del Clave para iniciar sesión o registrarse
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#E6F0F3",
            fg="#1E90FF",
            font=("yu gothic ui", 13, "bold"),
        )
        self.password_label.pack(fill=tk.X, padx=25, pady=8)
        # inserción de la entrada de texto para la Clave
        vcmd = self.root.register(self.validate_tab)
        self.password_entry = Entry(
            self.lgn_frame,
            relief=FLAT,
            bg="#E6F0F3",
            font=("yu gothic ui", 12, "bold"),
            show="*",
            insertbackground="#1E90FF",
            validate="key",
            validatecommand=(vcmd, "%P"),
        )
        self.password_entry.pack(fill=tk.X, padx=30, pady=0)
        
        self.password_entry.bind("<Return>", self.manejar_tecla)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#1E90FF", highlightthickness=0
        )
        self.password_line.pack(fill=tk.X, padx=30, pady=1)

        # botón para iniciar sesión
        self.login = Button(
            self.lgn_frame,
            text="Iniciar Sesion",
            font=("yu gothic ui", 13, "bold"),
            width=42,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
            command=lambda: Verificar(self),
        )
        self.login.pack(pady=35)
        # botón para iniciar sesión con la tecla enter
        self.login.bind("<Return>", (lambda event: Verificar(self)))

        # botón para restaurar la contraseña y el usuario
        self.forgot_button = Button(
            self.lgn_frame,
            text="Restaurar Acceso",
            font=("yu gothic ui", 13, "bold"),
            fg="#1E90FF",
            relief=FLAT,
            activebackground="#4169E1",
            borderwidth=0,
            background="#E6F0F3",
            cursor="hand2",
        )

        self.forgot_button.pack(pady=2)

        # información de la versión del software
        self.forgot_button = Button(
            self.lgn_frame,
            text="Version Alpha 2.0",
            font=("yu gothic ui", 13, "bold"),
            fg="#1E90FF",
            relief=FLAT,
            activebackground="#4169E1",
            borderwidth=0,
            background="#E6F0F3",
            cursor="hand2",
            command=lambda: Info(self=self),
        )
        self.forgot_button.pack(pady=2)
        
        self.root.mainloop()
    
    def manejar_tecla(self, event):
        if event.keysym == "Return":
            Verificar(self)
            
    def validate_tab(self, new_value):
        # Verifica que no haya espacios en blanco
        return not " " in new_value
        
        
if __name__ == "__main__":
    CreateLogin()