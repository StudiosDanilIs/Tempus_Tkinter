import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from util.Funciones import actualizar_reloj


def mostrar_opcion1(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.subventana_abierta = False
    self.root2.title("Inicio - Area de Cuentas")

    # Etiqueta de bienvenida
    self.imagen_perfil = utl.leer_imagen(
        utl.resource_path("imagenes/usuario_inicio.png"), size=(33, 37)
    )
    self.imagen_perfil_boton = Label(
        self.label_info,
        image=self.imagen_perfil,
        width=50,
        bg="#f0f0f0",
        activebackground="#f0f0f0",
        bd=0,
        cursor="hand2",
        fg="white",
    )
    self.imagen_perfil_boton.place(x=170, y=30)

    self.bienvenida_label = Label(
        self.label_info,
        text=f"{self.nombre_cuenta}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Avenir", 18, "bold"),
    )
    self.bienvenida_label.place(x=220, y=15)
    
    self.bienvenida_label = Label(
        self.label_info,
        text=f"{self.rol_programa}",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Avenir", 14),
    )
    self.bienvenida_label.place(x=220, y=45)

    # Frame para mostrar la información dinámica
    self.info_frame = Frame(self.label_info, bg="#f0f0f0")
    self.info_frame.place(x=70, y=100, width=800, height=700)

    # Botones para cambiar la información
    self.imagen_agregar = utl.leer_imagen(
        utl.resource_path("imagenes/editar.png"), size=(51, 59)
    )
    self.imagen_agregar_boton = Button(
        self.label_info,
        image=self.imagen_agregar,
        width=110,
        height=110,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Modificar Usuario"),
    )
    self.imagen_agregar_boton.place(x=0, y=0)

    self.imagen_eliminar = utl.leer_imagen(
        utl.resource_path("imagenes/agregar.png"), size=(51, 60)
    )
    self.imagen_eliminar_boton = Button(
        self.label_info,
        image=self.imagen_eliminar,
        width=110,
        height=110,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Agregar Usuario"),
    )
    self.imagen_eliminar_boton.place(x=0, y=111)

    self.imagen_modificar = utl.leer_imagen(
        utl.resource_path("imagenes/borrar.png"), size=(49, 60)
    )
    self.imagen_modificar_boton = Button(
        self.label_info,
        image=self.imagen_modificar,
        width=110,
        height=110,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Eliminar Usuario"),
    )
    self.imagen_modificar_boton.place(x=0, y=222)

    self.espacio_blanco = Label(
        self.label_info,
        width=15,
        height=40,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        fg="white",
    )
    self.espacio_blanco.place(x=0, y=333, width=112)

    # Muestra un CALENDARIO en la ventana principal
    self.label_dia = tk.Label(
        self.label_info,
        font=("Avenir", 18, "bold"),
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.label_dia.place(x=480, y=15)
    
    self.label_dia2 = tk.Label(
        self.label_info,
        font=("Avenir", 14),
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.label_dia2.place(x=480, y=45)

    # Muestra un RELOJ DIGITAL en la ventana principal
    self.label_reloj = tk.Label(
        self.label_info,
        width=8,
        anchor="w",
        justify="left",
        font=("Avenir", 18, "bold"),
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.label_reloj.place(x=740, y=15)
    
    self.label_reloj2 = tk.Label(
        self.label_info,
        width=8,
        anchor="w",
        justify="left",
        font=("Avenir", 14),
        bg="#f0f0f0",
        fg="#1E90FF",
    )
    self.label_reloj2.place(x=740, y=45)
    actualizar_reloj(self)

    mostrar_informacion(self, "Inicio Sistema")


def mostrar_informacion(self, opcion):
    # Limpiar el contenido del frame de información
    for widget in self.info_frame.winfo_children():
        widget.destroy()

    if opcion == "Modificar Usuario":
        label = Label(
            self.info_frame,
            text="Modificar Usuario",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        label.place(x=110, y=20)

        self.password_label = Label(
            self.info_frame,
            text="Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=70)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=100)

        self.password_label = Label(
            self.info_frame,
            text="Contraseña",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=140)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=170)

        self.password_label = Label(
            self.info_frame,
            text="Nuevo Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=210)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=240)

        self.password_label = Label(
            self.info_frame,
            text="Nueva Contraseña",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=280)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=310)

        self.password_label = Label(
            self.info_frame,
            text="Clave Única",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=350)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=380)

        self.guardar_clientes_button = tk.Button(
            self.info_frame,
            text="Modificar Datos",
            font=("Poppins", 13, "bold"),
            width=22,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
        )
        self.guardar_clientes_button.place(x=112, y=430)

    elif opcion == "Agregar Usuario":
        label = Label(
            self.info_frame,
            text="Agregar Usuario",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        label.place(x=110, y=20)

        self.password_label = Label(
            self.info_frame,
            text="Nombre",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=70)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=100)

        self.password_label = Label(
            self.info_frame,
            text="Cédula",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=140)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=170)

        self.password_label = Label(
            self.info_frame,
            text="Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=210)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=240)

        self.password_label = Label(
            self.info_frame,
            text="Contraseña",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=280)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=310)

        self.password_label = Label(
            self.info_frame,
            text="Clave Única",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=350)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=380)

        if self.rol_programa == "Administrador":
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Guardar Datos",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
            )
            self.guardar_clientes_button.place(x=112, y=430)

        else:
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Eliminar Datos",
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
            self.guardar_clientes_button.place(x=112, y=430)

    elif opcion == "Eliminar Usuario":
        label = Label(
            self.info_frame,
            text="Eliminar Usuario",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        label.place(x=110, y=20)

        self.password_label = Label(
            self.info_frame,
            text="Cédula",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=70)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=100)

        self.password_label = Label(
            self.info_frame,
            text="Clave Única",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.password_label.place(x=110, y=140)

        self.password_entry = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.password_entry.place(x=110, y=170)

        if self.rol_programa == "Administrador":
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Eliminar Datos",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
            )
            self.guardar_clientes_button.place(x=112, y=220)

        else:
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Eliminar Datos",
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
            self.guardar_clientes_button.place(x=112, y=220)

    elif opcion == "Inicio Sistema":
        self.title_label = Label(
            self.info_frame,
            text="Interfaz",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 30),
        )
        self.title_label.place(x=200, y=60)

        self.title2_label = Label(
            self.info_frame,
            text="para opciones\nde Usuario",
            anchor="w",
            justify=LEFT,
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 36, "bold"),
        )
        self.title2_label.place(x=200, y=107)
