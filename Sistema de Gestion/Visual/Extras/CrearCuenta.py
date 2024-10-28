import re
import tkinter as tk
from tkinter import *
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from Modelo.Inicio.OpcionUsuarios import Agregar_Usuarios


class CrearUsuario:
    def __init__(self, root):
        root = root
        root.destroy()

        self.miniVentana = tk.Tk()
        self.miniVentana.resizable(0, 0)
        self.miniVentana.geometry("1000x645")
        self.miniVentana.title("Inicio de Sesión")
        self.miniVentana.protocol(
            "WM_DELETE_WINDOW", lambda: self.miniVentana.destroy()
        )

        # creación de la ventana principal
        self.lgn_frame = Frame(self.miniVentana, bg="#f0f0f0")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Título de la ventana principal
        self.title_label = Label(
            self.lgn_frame,
            text="Crear",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 40),
        )
        self.title_label.place(x=570, y=52)

        self.title2_label = Label(
            self.lgn_frame,
            text="Usuario!",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 46, "bold"),
        )
        self.title2_label.place(x=570, y=115)

        # Area del Usuario
        self.nombre_agregar_label = Label(
            self.lgn_frame,
            text="Nombre",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.nombre_agregar_label.place(x=590, y=236)

        self.nombre_agregar = Entry(
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
            validatecommand=(self.miniVentana.register(self.validate_name), "%P"),
        )
        self.nombre_agregar.place(x=590, y=263, height=40)
        self.nombre_agregar.bind(
            "<Return>", lambda event: self.cedula_agregar.focus_set()
        )

        # Area de la Contraseña
        self.cedula_agregar_label = Label(
            self.lgn_frame,
            text="Cedula",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_agregar_label.place(x=590, y=310)

        self.cedula_agregar = Entry(
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
            validatecommand=(self.miniVentana.register(self.validate_document), "%P"),
        )
        self.cedula_agregar.place(x=590, y=337, height=40)
        self.cedula_agregar.bind(
            "<Return>", lambda event: self.usuario_agregar.focus_set()
        )

        self.usuario_agregar_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.usuario_agregar_label.place(x=590, y=384)

        self.usuario_agregar = Entry(
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
            validatecommand=(self.miniVentana.register(self.validate_tab), "%P"),
        )
        self.usuario_agregar.place(x=590, y=411, height=40)
        self.usuario_agregar.bind(
            "<Return>", lambda event: self.clave_agregar.focus_set()
        )

        self.clave_agregar_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#f0f0f0",
            fg="#232323",
            font=("Poppins", 13, "bold"),
        )
        self.clave_agregar_label.place(x=590, y=458)

        self.clave_agregar = Entry(
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
            validatecommand=(self.miniVentana.register(self.validate_tab), "%P"),
        )
        self.clave_agregar.place(x=590, y=485, height=40)
        self.clave_agregar.bind("<Return>", lambda event: Agregar_Usuarios(self))

        # botón para iniciar sesión
        self.imagen_iniciar_sesion = utl.leer_imagen("crear_usuario.png", size=(170, 55))
        self.login_boton = Button(
            self.lgn_frame,
            image=self.imagen_iniciar_sesion,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Agregar_Usuarios(self),
        )
        self.login_boton.place(x=585, y=540)
        self.login_boton.bind("<Return>", (lambda event: Agregar_Usuarios(self)))

        # botón para registrarse
        self.imagen_registrarse = utl.leer_imagen("salir.png", size=(170, 55))
        self.registrarse_boton = Button(
            self.lgn_frame,
            image=self.imagen_registrarse,
            width=170,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.miniVentana.destroy(),
        )
        self.registrarse_boton.place(x=755, y=540)

        # Fondo de la Ventana de Login
        self.imagen_fondo_login = utl.leer_imagen("fondo1.jpg", size=(500, 645))
        self.fondo_label = Label(
            self.lgn_frame,
            image=self.imagen_fondo_login,
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
    
    def validate_document(self, new_value):
        if " " in new_value:
            return False
        if len(new_value) > 10:
            return False
        if new_value.isdigit() or new_value == "":
            return True
        return False
    
    def validate_name(self, new_value):
        if " " in new_value:
            return False
        if len(new_value) > 20:
            return False
        if new_value.isalpha() or new_value == "":
            return True
        return False


if __name__ == "__main__":
    ventana = CrearUsuario()
    ventana.self.miniVentana.mainloop()
    CrearUsuario()
