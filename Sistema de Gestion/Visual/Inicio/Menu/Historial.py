import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkcalendar import DateEntry
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox


def mostrar_opcion5(self):
    self.limpiar_contenido()
    self.root2.title("Historial de Solicitudes")

    self.info_frame = Frame(self.label_info, bg="#f0f0f0", colormap="new")
    self.info_frame.place(x=125, y=15, width=805, height=900)

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

    self.espacio_blanco = Label(
        self.label_info,
        width=15,
        height=40,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        fg="white",
    )
    self.espacio_blanco.place(x=0, y=210, width=107)

    mostrar_informacion(self, "Agregar Usuario")


def mostrar_informacion(self, opcion):
    # Limpiar el contenido del frame de información
    for widget in self.info_frame.winfo_children():
        widget.destroy()

    if opcion == "Agregar Usuario":

        self.frame_lista = Frame(self.info_frame, bg="#DCEBFF", colormap="new")
        self.frame_lista.place(x=0, y=55, width=805, height=535)

        titel_label = tk.Label(
            self.info_frame,
            text="Historial de Pedidos",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 19, "bold"),
        )
        titel_label.place(x=0, y=0)

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
            self.frame_lista,
            columns=("cedula", "fecha", "descripcion", "precio", "garantia", "fecha entrega"),
            show="headings",
            style="Treeview",
        )

        column_widths = {
            "cedula": 90,  # Adjust widths as needed
            "fecha": 80,
            "descripcion": 300,
            "precio": 90,
            "garantia": 70,
            "fecha entrega": 80,
        }

        # Configurar los encabezados de las columnas
        self.tree.heading("cedula", text="Cédula", anchor="center")
        self.tree.heading("fecha", text="Fecha", anchor="center")
        self.tree.heading("descripcion", text="Descripcion", anchor="center")
        self.tree.heading("garantia", text="Garantía", anchor="center")
        self.tree.heading("precio", text="Precio", anchor="center")
        self.tree.heading("fecha entrega", text="Entrega", anchor="center")

        # Configurar la fuente para los encabezados y las filas
        self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
        self.tree.tag_configure("row", font=("Poppins", 10))

        # Configurar el ancho de las columnas y la alineación
        for col, width in column_widths.items():
            self.tree.column(col, minwidth=width, width=width, anchor="center")

        scrollbar_cover = tk.Frame(self.frame_lista, bg="#DCEBFF")
        scrollbar_cover.grid(row=0, column=1, sticky="ns")

        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(
            self.frame_lista,
            orient="vertical",
            command=self.tree.yview,
            style="Vertical.TScrollbar",
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la barra de desplazamiento en el marco
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

        # Configurar el marco de información
        self.frame_lista.grid_rowconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(1, weight=0)

    elif opcion == "Modificar Usuario":
        titel_label = tk.Label(
            self.info_frame,
            text="Buscar solicitudes por cliente",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 19, "bold"),
        )
        titel_label.place(x=0, y=0)

        # Area del Nombre del Cliente
        self.cedula_buscar_label = tk.Label(
            self.info_frame,
            text="Cédula del cliente",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_buscar_label.place(x=440, y=10)

        self.cedula_buscar_entry = tk.Entry(
            self.info_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            width=18,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
        )
        self.cedula_buscar_entry.place(x=595, y=10)
        
        self.lupa = utl.leer_imagen("lupa.png", size=(27, 27))
        self.buscar = tk.Button(
            self.info_frame,
            width=30,
            image=self.lupa,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.buscar.place(x=774, y=10)    

        
        self.frame_lista = Frame(self.info_frame, bg="#f0f0f0", colormap="new")
        self.frame_lista.place(x=0, y=55, width=805, height=600)    
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
            "Treeview.TScrollbar",
            troughcolor="#f0f0f0",
            background="#f0f0f0",
            relief="flat",
            borderwidth=1,
            width=7,
            highlightcolor="#f0f0f0",
            highlightbackground="#f0f0f0",
            highlightthickness=1,
        )

        # Crear el Treeview con el estilo personalizado
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("ID", "fecha", "descripcion", "precio", "garantia", "descargar"),
            show="headings",
            style="Treeview",
        )

        column_widths = {
            "ID": 50,  # Adjust widths as needed
            "fecha": 120,
            "descripcion": 300,
            "precio": 100,
            "garantia": 100,
            "descargar": 135,
        }

        # Configurar los encabezados de las columnas
        self.tree.heading("ID", text="N°", anchor="center")
        self.tree.heading("fecha", text="Fecha", anchor="center")
        self.tree.heading("descripcion", text="Descripcion", anchor="center")
        self.tree.heading("precio", text="Precio", anchor="center")
        self.tree.heading("garantia", text="Garantia", anchor="center")
        self.tree.heading("descargar", text="Descargar pdf", anchor="center")

        # Configurar la fuente para los encabezados y las filas
        self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
        self.tree.tag_configure("row", font=("Poppins", 10))

        # Configurar el ancho de las columnas y la alineación
        for col, width in column_widths.items():
            self.tree.column(col, minwidth=width, width=width, anchor="center")

        scrollbar_cover = tk.Frame(self.frame_lista, bg="#f0f0f0")
        scrollbar_cover.grid(row=0, column=1, sticky="ns", pady=(0, 240))
        

        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(
            self.frame_lista,
            orient="vertical",
            command=self.tree.yview,
            style="Vertical.TScrollbar",
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la barra de desplazamiento en el marco
        self.tree.grid(row=0, column=0, sticky="nsew", pady=(0, 240))
        scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

        # Configurar el marco de información
        self.frame_lista.grid_rowconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(1, weight=0)
        
        
        titel_label = tk.Label(
            self.frame_lista,
            text="Agregar fecha de entrega:",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 17, "bold"),
        )
        titel_label.place(x=0, y=375)
        
        
        self.nombre_label = tk.Label(
            self.frame_lista,
            text="N° de orden",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.nombre_label.place(x=0, y=425)

        self.nombre_entry = tk.Entry(
            self.frame_lista,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            width=22,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
        )
        self.nombre_entry.place(x=0, y=455)
        
        
        self.nombre_label = tk.Label(
            self.frame_lista,
            text="Cédula cliente",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.nombre_label.place(x=235, y=425)

        self.nombre_entry = tk.Entry(
            self.frame_lista,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            width=22,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
        )
        self.nombre_entry.place(x=235, y=455)
        
        
        self.nombre_label = tk.Label(
            self.frame_lista,
            text="Fecha entrega",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.nombre_label.place(x=470, y=425)
                
        self.nombre_entry = DateEntry(
            self.frame_lista,
            width=20,
            background="#DCEBFF",
            foreground="#1778FB",
            year=2024,
            date_pattern="dd /MM /yyyy",
            font=("Helvetica", 13),
            state="readonly",
        )
        self.nombre_entry.place(x=470, y=455)
        
        
        self.modificar_clientes_button = tk.Button(
            self.frame_lista,
            text="Enviar datos",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
        )
        self.modificar_clientes_button.place(x=0, y=505)