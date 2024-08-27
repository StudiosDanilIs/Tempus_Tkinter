import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import util.PhotoImagenes as utl
from BaseDatos.VerificarSesion import verificar_sesion as Validar

class Secret_Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.geometry("480x600")
        self.root.title("Iniciar Sesión")

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#f0f0f0")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Título de la ventana principal
        self.title_label = Label(
            self.lgn_frame,
            text="Restaurar",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 40),
        )
        self.title_label.place(x=60, y=20)

        self.title2_label = Label(
            self.lgn_frame,
            text="Sesión!",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 46, "bold"),
        )
        self.title2_label.place(x=120, y=90)

        # Area del Usuario
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 13, "bold"),
        )
        self.username_label.place(x=80, y=220)

        self.username_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#1778FB",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1778FB",
            foreground="#000000",
            width=35,
        )
        self.username_entry.place(x=80, y=250, height=40)
        self.username_entry.bind(
            "<Return>", lambda event: self.password_entry.focus_set()
        )

        # Area de la Contraseña
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=80, y=300)

        self.password_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#1778FB",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1778FB",
            foreground="#000000",
            width=35,
            show="*",
        )
        self.password_entry.place(x=80, y=330, height=40)
        self.password_entry.bind("<Return>", lambda event: self.password_unica_entry.focus_set())
        
        # Area de la Contraseña
        self.password_unica_label = Label(
            self.lgn_frame,
            text="Clave Única",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Poppins", 13, "bold"),
        )
        self.password_unica_label.place(x=80, y=380)

        self.password_unica_entry = Entry(
            self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#1778FB",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1778FB",
            foreground="#000000",
            width=35,
            show="*",
        )
        self.password_unica_entry.place(x=80, y=410, height=40)
        self.password_unica_entry.bind("<Return>", lambda event: Validar(self))
        
        # botón para registrarse
        self.imagen_registrarse2 = utl.leer_imagen("boton_iniciar_sesion.png", size=(170, 55))
        self.registrarse_boton = tk.Button(
            self.lgn_frame,
            image=self.imagen_registrarse2,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Validar(self),
        )
        self.registrarse_boton.place(x=75, y=500)

        # botón para iniciar sesión
        self.imagen_iniciar_sesion1 = utl.leer_imagen("boton_salir.png", size=(170, 55))
        self.login_boton = Button(
            self.lgn_frame,
            image=self.imagen_iniciar_sesion1,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=self.root.destroy
        )
        self.login_boton.place(x=240, y=500)

        # Abrir la Ventana de Login
        self.root.mainloop()

if __name__ == "__main__":
    Secret_Login()        