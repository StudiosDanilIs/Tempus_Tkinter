import re
import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from util.Reloj import actualizar_reloj
from Modelo.Inicio.OpcionUsuarios import Eliminar_Usuarios


def toggle_imagenes(self):
    self.mostrar_grafico = not self.mostrar_grafico
    if self.mostrar_grafico:
        self.imagen_eliminar_boton.place_forget()
        self.imagen_grafico_boton.place(x=835, y=12)
    else:
        self.imagen_grafico_boton.place_forget()
        self.imagen_eliminar_boton.place(x=835, y=12)


def mostrar_opcion1(self):
    self.limpiar_contenido()
    self.root2.title("Inicio - Bienvenido a Tempus App")
    self.root2.geometry("1100x635")
    self.mostrar_grafico = True

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
    self.imagen_perfil_boton.place(x=40, y=29)
    self.nombre_label = Label(
        self.label_info,
        text=f"{self.nombre_cuenta}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Avenir", 18, "bold"),
    )
    self.nombre_label.place(x=90, y=15)
    self.rol_label = Label(
        self.label_info,
        text=f"{self.rol_programa}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Avenir", 14),
    )
    self.rol_label.place(x=90, y=45)

    # Muestra un CALENDARIO en la ventana principal
    self.fecha_label = tk.Label(
        self.label_info,
        font=("Avenir", 18, "bold"),
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.fecha_label.place(x=340, y=15)
    self.anno_label = tk.Label(
        self.label_info,
        font=("Avenir", 14),
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.anno_label.place(x=340, y=45)

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
    self.dia_label.place(x=610, y=15)
    self.hora_label = tk.Label(
        self.label_info,
        width=8,
        anchor="w",
        justify="left",
        font=("Avenir", 14),
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.hora_label.place(x=610, y=45)
    actualizar_reloj(self)

    # Frame para mostrar la información dinámica
    self.info_frame = Frame(self.label_info, bg="#f0f0f0")
    self.info_frame.place(x=70, y=100, width=800, height=700)

    if self.rol_programa == "Administrador":
        self.imagen_grafico = utl.leer_imagen("graficos.png", size=(38, 38))
        self.imagen_grafico_boton = Button(
            self.label_info,
            image=self.imagen_grafico,
            width=60,
            height=60,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: [
                mostrar_informacion(self, "Inicio Sistema"),
                toggle_imagenes(self),
            ],
        )
        self.imagen_grafico_boton.place(x=820, y=12)

        self.imagen_eliminar = utl.leer_imagen("ajustes.png", size=(38, 38))
        self.imagen_eliminar_boton = Button(
            self.label_info,
            image=self.imagen_eliminar,
            width=60,
            height=60,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: [
                mostrar_informacion(self, "Eliminar Usuario"),
                toggle_imagenes(self),
            ],
        )
        self.imagen_eliminar_boton.place(x=820, y=12)

        toggle_imagenes(self)

    mostrar_informacion(self, "Inicio Sistema")


def mostrar_informacion(self, opcion):
    # Limpiar el contenido del frame de información
    for widget in self.info_frame.winfo_children():
        widget.destroy()

    if opcion == "Eliminar Usuario":
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
        self.cedula_eliminar.bind("<Return>", lambda event: Eliminar_Usuarios(self))
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
        self.eliminar_usuarios_boton.place(x=112, y=160)

    elif opcion == "Inicio Sistema":
        self.titulo_label = Label(
            self.info_frame,
            text="Bienvenido",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 27),
        )
        self.titulo_label.place(x=120, y=85)
        
        self.titulo2_label = Label(
            self.info_frame,
            text="estas en un entorno\ncreado para solucionar\nproblemas en Tempus",
            anchor="w",
            justify=LEFT,
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 33, "bold"),
        )
        self.titulo2_label.place(x=120, y=127)


def validate_cedula(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False
