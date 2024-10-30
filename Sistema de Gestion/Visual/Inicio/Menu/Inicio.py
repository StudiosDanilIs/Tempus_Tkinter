import re
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from util.Reloj import actualizar_reloj
from Modelo.Inicio.OpcionUsuarios import Eliminar_Usuarios, Cargar_Usuarios


def toggle_imagenes(self):
    self.mostrar_grafico = not self.mostrar_grafico
    if self.mostrar_grafico:
        self.imagen_eliminar_boton.place_forget()
        self.imagen_grafico_boton.place(x=795, y=0)
        
        self.title_usuario.place_forget()
        self.title_inicio.place(x=855, y=22)
    else:
        self.imagen_grafico_boton.place_forget()
        self.imagen_eliminar_boton.place(x=795, y=0)
        
        self.title_inicio.place_forget()
        self.title_usuario.place(x=855, y=22)


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
    self.info_frame.place(x=70, y=100, width=820, height=530)

    if self.rol_programa == "Administrador":
        self.imagen_grafico = utl.leer_imagen("marcado.png", size=(70, 65))
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
        self.imagen_grafico_boton.place(x=870, y=0)

        self.imagen_eliminar = utl.leer_imagen("desmarcado.png", size=(70, 65))
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
        self.imagen_eliminar_boton.place(x=870, y=0)
        
        self.title_inicio = Button(
            self.label_info,
            text="Inicio",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
            activebackground="#f0f0f0",
            command=lambda: [
                mostrar_informacion(self, "Inicio Sistema"),
                toggle_imagenes(self),
            ],
        )
        self.title_inicio.place(x=860, y=22)
        
        self.title_usuario = Button(
            self.label_info,
            text="Usuario",
            relief=FLAT,
            borderwidth=0,
            background="#f0f0f0",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
            activebackground="#f0f0f0",
            command=lambda: [
                mostrar_informacion(self, "Eliminar Usuario"),
                toggle_imagenes(self),
            ],
        )
        self.title_usuario.place(x=855, y=22)
        

        toggle_imagenes(self)

    mostrar_informacion(self, "Inicio Sistema")


def mostrar_informacion(self, opcion):
    # Limpiar el contenido del frame de información
    for widget in self.info_frame.winfo_children():
        widget.destroy()

    if opcion == "Inicio Sistema":
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
        
        
        self.title_proteccion = Label(
            self.info_frame,
            text="Dolphin\nSecureRead",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.title_proteccion.place(x=670, y=480)
        
        self.imagen_proteccion = utl.leer_imagen("protegido.png", size=(43, 43))
        self.label_imagen_proteccion = Label(
            self.info_frame,
            image=self.imagen_proteccion,
            width=50,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            fg="white",
        )
        self.label_imagen_proteccion.place(x=770, y=480)
        

    elif opcion == "Eliminar Usuario":
        self.titulo_label = Label(
            self.info_frame,
            text="Opción para eliminar usuarios",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Montserrat", 17, "bold"),
        )
        self.titulo_label.place(x=0, y=0)
        self.cedula_eliminar_label = Label(
            self.info_frame,
            text="Cédula usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_eliminar_label.place(x=0, y=50)
        self.cedula_eliminar = Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=24,
            validate="key",
            validatecommand=(self.root2.register(validate_cedula), "%P"),
        )
        self.cedula_eliminar.place(x=0, y=80)
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
        self.eliminar_usuarios_boton.place(x=0, y=120)

        self.total_admin = Label(
            self.info_frame,
            text="Cuentas Admin: ",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 14, "bold"),
        )
        self.total_admin.place(x=300, y=70)

        self.total_empleado = Label(
            self.info_frame,
            text="Cuentas Empleado: ",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 14, "bold"),
        )
        self.total_empleado.place(x=300, y=120)

        self.titel_label = tk.Label(
            self.info_frame,
            text="Lista de usuarios registrados",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.titel_label.place(x=0, y=180)

        self.actualizar = utl.leer_imagen("actualizar.png", size=(27, 27))
        self.buscar = tk.Button(
            self.info_frame,
            width=30,
            image=self.actualizar,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: Cargar_Usuarios(self),
        )
        self.buscar.place(x=775, y=175)
        Historial(self)


def Historial(self):
    # Configuración del estilo
    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "Treeview",
        font=("Poppins", 10),
        foreground="#1778FB",
        background="#DCEBFF",
    )
    style.map(
        "Treeview.Heading",
        background=[("selected", "#DCEBFF")],
        foreground=[("selected", "#DCEBFF")],
    )

    style.configure(
        "Treeview.Heading",
        background="#DCEBFF",
        foreground="#1778FB",
        padding=3,
        font=("Poppins", 12, "bold"),
        relief="flat",
        borderwidth=3,
        anchor="center",
        width=100,
        height=60,
    )
    style.configure(
        "Treeview", font=("Poppins", 10), foreground="#1778FB", background="#DCEBFF"
    )
    style.configure(
        "Vertical.TScrollbar",
        troughcolor="#FFFFFF",
        background="#FFFFFF",
        relief="flat",
        borderwidth=1,
        width=10,
        highlightcolor="#FFFFFF",
        highlightbackground="#FFFFFF",
        highlightthickness=1,
    )

    # Crear el Treeview con el estilo personalizado
    self.tree = ttk.Treeview(
        self.info_frame,
        columns=(
            "numero",
            "nombre",
            "cedula",
            "permiso",
        ),
        show="headings",
        style="Treeview",
    )

    column_widths = {
        "numero": 80,
        "nombre": 80,
        "cedula": 80,
        "permiso": 80,
    }

    # Configurar los encabezados de las columnas
    self.tree.heading("numero", text="N° usuario", anchor="center")
    self.tree.heading("nombre", text="Nombre", anchor="center")
    self.tree.heading("cedula", text="Cedula", anchor="center")
    self.tree.heading("permiso", text="Tipo permiso", anchor="center")

    # Configurar la fuente para los encabezados y las filas
    self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
    self.tree.tag_configure("row", font=("Poppins", 10))

    # Configurar el ancho de las columnas y la alineación
    for col, width in column_widths.items():
        self.tree.column(col, minwidth=width, width=width, anchor="center")

    scrollbar_cover = tk.Frame(self.info_frame, bg="#DCEBFF")
    scrollbar_cover.grid(row=0, column=1, sticky="ns", pady=(210, 30), padx=(0, 0))

    # Crear la barra de desplazamiento
    scrollbar = ttk.Scrollbar(
        self.info_frame,
        orient="vertical",
        command=self.tree.yview,
        style="Vertical.TScrollbar",
    )
    self.tree.configure(yscrollcommand=scrollbar.set)

    # Colocar el Treeview y la barra de desplazamiento en el marco
    self.tree.grid(row=0, column=0, sticky="nsew", pady=(210, 30), padx=(0, 0))
    scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

    # Configurar el marco de información
    self.info_frame.grid_rowconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(1, weight=0)


def validate_cedula(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False
