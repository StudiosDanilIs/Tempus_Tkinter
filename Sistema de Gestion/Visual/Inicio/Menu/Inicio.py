import re
import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from util.Funciones import actualizar_reloj
from Modelo.Inicio.OpcionUsuarios import (
    Agregar_Usuarios,
    Modificar_Usuarios,
    Eliminar_Usuarios,
)


def mostrar_opcion1(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.root2.title("Inicio - Area de Cuentas")
    self.root2.geometry("1100x635")

    # Etiqueta de bienvenida
    self.imagen_perfil = utl.leer_imagen("usuario_inicio.png", size=(33, 33))
    self.imagen_perfil_boton = Label(
        self.label_info,
        image=self.imagen_perfil,
        width=50,
        bg="#f0f0f0",
        activebackground="#f0f0f0",
        bd=0,
        fg="white",
    )
    self.imagen_perfil_boton.place(x=170, y=29)

    self.nombre_label = Label(
        self.label_info,
        text=f"{self.nombre_cuenta}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Avenir", 18, "bold"),
    )
    self.nombre_label.place(x=220, y=15)

    self.rol_label = Label(
        self.label_info,
        text=f"{self.rol_programa}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Avenir", 14),
    )
    self.rol_label.place(x=220, y=45)

    # Frame para mostrar la información dinámica
    self.info_frame = Frame(self.label_info, bg="#f0f0f0")
    self.info_frame.place(x=70, y=100, width=800, height=700)

    # Botones para cambiar la información
    self.imagen_agregar = utl.leer_imagen("agregar.png", size=(51, 59))
    self.imagen_agregar_boton = Button(
        self.label_info,
        image=self.imagen_agregar,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Agregar Usuario"),
    )
    self.imagen_agregar_boton.place(x=0, y=0)

    self.imagen_modificar = utl.leer_imagen("editar.png", size=(51, 60))
    self.imagen_modificar_boton = Button(
        self.label_info,
        image=self.imagen_modificar,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Modificar Usuario"),
    )
    self.imagen_modificar_boton.place(x=0, y=105)

    self.imagen_eliminar = utl.leer_imagen("borrar.png", size=(49, 60))
    self.imagen_eliminar_boton = Button(
        self.label_info,
        image=self.imagen_eliminar,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Eliminar Usuario"),
    )
    self.imagen_eliminar_boton.place(x=0, y=210)

    self.espacio_blanco = Label(
        self.label_info,
        width=15,
        height=40,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        fg="white",
    )
    self.espacio_blanco.place(x=0, y=310, width=107)

    # Muestra un CALENDARIO en la ventana principal
    self.fecha_label = tk.Label(
        self.label_info,
        font=("Avenir", 18, "bold"),
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.fecha_label.place(x=480, y=15)

    self.anno_label = tk.Label(
        self.label_info,
        font=("Avenir", 14),
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.anno_label.place(x=480, y=45)

    # Muestra un RELOJ DIGITAL en la ventana principal
    self.dia_label = tk.Label(
        self.label_info,
        width=8,
        anchor="w",
        justify="left",
        font=("Avenir", 18, "bold"),
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.dia_label.place(x=740, y=15)

    self.hora_label = tk.Label(
        self.label_info,
        width=8,
        anchor="w",
        justify="left",
        font=("Avenir", 14),
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.hora_label.place(x=740, y=45)
    actualizar_reloj(self)

    mostrar_informacion(self, "Inicio Sistema")


def mostrar_informacion(self, opcion):
    # Limpiar el contenido del frame de información
    for widget in self.info_frame.winfo_children():
        widget.destroy()

    if opcion == "Agregar Usuario":
        titulo_label = Label(
            self.info_frame,
            text="Agregar usuario",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        titulo_label.place(x=110, y=20)

        self.nombre_agregar_label = Label(
            self.info_frame,
            text="Nombre",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nombre_agregar_label.place(x=110, y=70)

        self.nombre_agregar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_name), "%P"),
        )
        self.nombre_agregar.place(x=110, y=100)
        self.nombre_agregar.bind(
            "<Return>", lambda event: self.cedula_agregar.focus_set()
        )

        self.cedula_agregar_label = Label(
            self.info_frame,
            text="Cédula",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_agregar_label.place(x=110, y=140)

        self.cedula_agregar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_cedula), "%P"),
        )
        self.cedula_agregar.place(x=110, y=170)
        self.cedula_agregar.bind(
            "<Return>", lambda event: self.usuario_agregar.focus_set()
        )

        self.usuario_agregar_label = Label(
            self.info_frame,
            text="Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.usuario_agregar_label.place(x=110, y=210)

        self.usuario_agregar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_ingresar), "%P"),
        )
        self.usuario_agregar.place(x=110, y=240)
        self.usuario_agregar.bind(
            "<Return>", lambda event: self.clave_agregar.focus_set()
        )

        self.clave_agregar_label = Label(
            self.info_frame,
            text="Contraseña",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.clave_agregar_label.place(x=110, y=280)

        self.clave_agregar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_ingresar), "%P"),
        )
        self.clave_agregar.place(x=110, y=310)
        self.clave_agregar.bind("<Return>", lambda event: self.clave_unica.focus_set())

        self.clave_unica_label = Label(
            self.info_frame,
            text="Clave única",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.clave_unica_label.place(x=110, y=350)

        self.clave_unica = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_clave_unica), "%P"),
        )
        self.clave_unica.place(x=110, y=380)
        self.clave_unica.bind("<Return>", lambda event: Agregar_Usuarios(self))

        if self.rol_programa == "Administrador":
            self.agregar_usuarios_boton = tk.Button(
                self.info_frame,
                text="Guardar usuario",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
                command=lambda: Agregar_Usuarios(self),
            )
            self.agregar_usuarios_boton.place(x=112, y=430)

        else:
            self.agregar_usuarios_boton = tk.Button(
                self.info_frame,
                text="Guardar usuario",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
                command=lambda: messagebox.showerror(
                    "Error", "No Tienes los Permisos Necesarios"
                ),
            )
            self.agregar_usuarios_boton.place(x=112, y=430)

    elif opcion == "Modificar Usuario":
        titulo_label = Label(
            self.info_frame,
            text="Modificar usuario",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        titulo_label.place(x=110, y=20)

        self.usuario_modificar_label = Label(
            self.info_frame,
            text="Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.usuario_modificar_label.place(x=110, y=70)

        self.usuario_modificar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_ingresar), "%P"),
        )
        self.usuario_modificar.place(x=110, y=100)
        self.usuario_modificar.bind(
            "<Return>", lambda event: self.clave_modificar.focus_set()
        )

        self.clave_modificar_label = Label(
            self.info_frame,
            text="Contraseña",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.clave_modificar_label.place(x=110, y=140)

        self.clave_modificar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_ingresar), "%P"),
        )
        self.clave_modificar.place(x=110, y=170)
        self.clave_modificar.bind(
            "<Return>", lambda event: self.nuevo_usuario_modificar.focus_set()
        )

        self.nuevo_usuario_modificar_label = Label(
            self.info_frame,
            text="Nuevo usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nuevo_usuario_modificar_label.place(x=110, y=210)

        self.nuevo_usuario_modificar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_ingresar), "%P"),
        )
        self.nuevo_usuario_modificar.place(x=110, y=240)
        self.nuevo_usuario_modificar.bind(
            "<Return>", lambda event: self.nueva_clave_modificar.focus_set()
        )

        self.nueva_clave_modificar_label = Label(
            self.info_frame,
            text="Nueva contraseña",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nueva_clave_modificar_label.place(x=110, y=280)

        self.nueva_clave_modificar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_ingresar), "%P"),
        )
        self.nueva_clave_modificar.place(x=110, y=310)
        self.nueva_clave_modificar.bind(
            "<Return>", lambda event: self.clave_unica.focus_set()
        )

        self.clave_unica_label = Label(
            self.info_frame,
            text="Ingresa clave única",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.clave_unica_label.place(x=110, y=360)

        self.clave_unica = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_clave_unica), "%P"),
        )
        self.clave_unica.place(x=110, y=390)
        self.clave_unica.bind("<Return>", lambda event: Modificar_Usuarios(self))

        self.modificar_usuarios_boton = tk.Button(
            self.info_frame,
            text="Actualizar usuario",
            font=("Poppins", 13, "bold"),
            width=22,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: Modificar_Usuarios(self),
        )
        self.modificar_usuarios_boton.place(x=112, y=440)

    elif opcion == "Eliminar Usuario":
        titulo_label = Label(
            self.info_frame,
            text="Eliminar usuario",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        titulo_label.place(x=110, y=20)

        self.cedula_eliminar_label = Label(
            self.info_frame,
            text="Cédula",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_eliminar_label.place(x=110, y=70)

        self.cedula_eliminar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_cedula), "%P"),
        )
        self.cedula_eliminar.place(x=110, y=100)
        self.cedula_eliminar.bind(
            "<Return>", lambda event: self.clave_unica.focus_set()
        )

        self.clave_unica_label = Label(
            self.info_frame,
            text="Ingresa clave única",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.clave_unica_label.place(x=110, y=150)

        self.clave_unica = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(validate_clave_unica), "%P"),
        )
        self.clave_unica.place(x=110, y=180)
        self.clave_unica.bind("<Return>", lambda event: Eliminar_Usuarios(self))

        if self.rol_programa == "Administrador":
            self.eliminar_usuarios_boton = tk.Button(
                self.info_frame,
                text="Eliminar usuario",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
                command=lambda: Eliminar_Usuarios(self),
            )
            self.eliminar_usuarios_boton.place(x=112, y=230)

        else:
            self.eliminar_usuarios_boton = tk.Button(
                self.info_frame,
                text="Eliminar usuario",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
                command=lambda: messagebox.showerror(
                    "Error", "No Tienes los Permisos Necesarios"
                ),
            )
            self.eliminar_usuarios_boton.place(x=112, y=230)

    elif opcion == "Inicio Sistema":
        self.titulo_label = Label(
            self.info_frame,
            text="Interfaz",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 30),
        )
        self.titulo_label.place(x=200, y=65)

        self.titulo2_label = Label(
            self.info_frame,
            text="para opciones\nde usuario",
            anchor="w",
            justify=LEFT,
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 36, "bold"),
        )
        self.titulo2_label.place(x=200, y=112)


# Funciones para validar Datos de Clientes
def validate_name(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 20:
        return False
    if new_value.isalpha() or new_value == "":
        return True
    return False


def validate_clave_unica(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 6:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False


def validate_cedula(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False


def validate_ingresar(new_value):
    # Permitir solo letras, números y un símbolo especial (por ejemplo, @)
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
