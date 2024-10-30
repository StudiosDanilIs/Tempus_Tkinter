import re
import tkinter as tk
from tkinter import *
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from Modelo.Extras.VerificarSesion import verificar_sesion


class LoginRecuperar:
    def __init__(self, root):
        self.root = root
        self.root.destroy()
        
        self.miniVentana = tk.Tk()
        self.miniVentana.resizable(0, 0)
        self.miniVentana.geometry("1000x645")
        self.miniVentana.title("Login - Recuperar Usuario")
        self.miniVentana.protocol(
            "WM_DELETE_WINDOW", lambda: self.miniVentana.destroy()
        )

        # creación de la ventana principal
        self.lgn_frame = Frame(self.miniVentana, bg="#f0f0f0")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Título de la ventana principal
        self.title_label = Label(
            self.lgn_frame,
            text="Recuperar",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 40),
        )
        self.title_label.place(x=570, y=52)

        self.title2_label = Label(
            self.lgn_frame,
            text="Usuarios!",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 46, "bold"),
        )
        self.title2_label.place(x=570, y=115)

        # Area del Usuario
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario del sistema",
            anchor="w",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.username_label.place(x=590, y=236)

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
            validatecommand=(self.miniVentana.register(self.validate_tab), "%P"),
        )
        self.username_entry.place(x=590, y=263, height=40)
        self.username_entry.bind(
            "<Return>", lambda event: self.password_entry.focus_set()
        )

        # Area de la Contraseña
        self.password_label = Label(
            self.lgn_frame,
            text="Clave del sistema",
            anchor="w",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=590, y=310)

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
            validatecommand=(self.miniVentana.register(self.validate_tab), "%P"),
        )
        self.password_entry.place(x=590, y=337, height=40)
        self.password_entry.bind("<Return>", lambda event: verificar_sesion(self))

        self.title3_label = Label(
            self.lgn_frame,
            text="Esta sección del programa permite a los\nAdministradores de Tempus recuperar y modificar\nlos permisos de los usuarios registrados.\nEsta funcionalidad asegura el control y la\ngestión adecuada de los niveles de acceso\ndentro de la plataforma Tempus.",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.title3_label.place(x=555, y=480)

        # botón para iniciar sesión
        self.imagen_recuperar_iniciar = utl.leer_imagen(
            "boton_iniciar_sesion.png", size=(170, 55)
        )
        self.login_boton = Button(
            self.lgn_frame,
            image=self.imagen_recuperar_iniciar,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: verificar_sesion(self),
        )
        self.login_boton.place(x=585, y=395)
        self.login_boton.bind("<Return>", (lambda event: verificar_sesion(self)))

        # botón para registrarse
        self.imagen_salir_recuperar = utl.leer_imagen("salir.png", size=(170, 55))
        self.registrarse_boton = Button(
            self.lgn_frame,
            image=self.imagen_salir_recuperar,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.miniVentana.destroy(),
        )
        self.registrarse_boton.place(x=755, y=395)

        # Fondo de la Ventana de Login
        self.imagen_fondo_recuperar = utl.leer_imagen("fondo3.jpg", size=(500, 645))
        self.fondo_label = Label(
            self.lgn_frame,
            image=self.imagen_fondo_recuperar,
            width=501,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
        )
        self.fondo_label.place(x=0)

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


if __name__ == "__main__":
    ventana = CrearUsuario()
    ventana.self.miniVentana.mainloop()
    CrearUsuario()
