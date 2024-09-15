import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Frame
import util.PhotoImagenes as utl
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox
from Modelo.Inicio.OpcionesHistorial import (
    Solicitudes_Clientes,
    Cargar_Solicitudes,
    Agregar_Fecha_Entrega
)
from util.CreateExcel import obtener_datos_solicitud, guardar_datos_en_excel


def mostrar_opcion5(self):
    self.limpiar_contenido()
    self.root2.title("Historial de Solicitudes")
    self.root2.geometry("1170x635")

    self.info_frame = Frame(self.label_info, bg="#f0f0f0", colormap="new")
    self.info_frame.place(x=125, y=15, width=865, height=600)

    # Botones para cambiar la información
    self.imagen_historial_completo = utl.leer_imagen("agregar.png", size=(51, 59))
    self.boton_historial_completo = Button(
        self.label_info,
        image=self.imagen_historial_completo,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Historial Pedido"),
    )
    self.boton_historial_completo.place(x=0, y=0)

    self.imagen_historial_cliente = utl.leer_imagen("editar.png", size=(51, 60))
    self.boton_historial_cliente = Button(
        self.label_info,
        image=self.imagen_historial_cliente,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Historial Venta"),
    )
    self.boton_historial_cliente.place(x=0, y=105)
    
    self.imagen_hist2orial_cliente = utl.leer_imagen("editar.png", size=(51, 60))
    self.boton_historial_cliente = Button(
        self.label_info,
        image=self.imagen_hist2orial_cliente,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Historial Reparacion"),
    )
    self.boton_historial_cliente.place(x=0, y=210)
    
    self.imagen_historia3l_cliente = utl.leer_imagen("editar.png", size=(51, 60))
    self.boton_historial_cliente = Button(
        self.label_info,
        image=self.imagen_historia3l_cliente,
        width=105,
        height=105,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: mostrar_informacion(self, "Historial x Cliente"),
    )
    self.boton_historial_cliente.place(x=0, y=315)

    self.espacio_blanco = Label(
        self.label_info,
        width=15,
        height=40,
        bg="#FFFFFF",
        activebackground="#FFFFFF",
        bd=0,
        fg="white",
    )
    self.espacio_blanco.place(x=0, y=420, width=107)

    mostrar_informacion(self, "Inicio Historial")


def mostrar_informacion(self, opcion):
    # Limpiar el contenido del frame de información
    for widget in self.info_frame.winfo_children():
        widget.destroy()

    if opcion == "Historial Pedido":
        titel_label = tk.Label(
            self.info_frame,
            text="Historial de Pedidos",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 19, "bold"),
        )
        titel_label.place(x=0, y=0)
        
        Historial(self)
        Cargar_Solicitudes(self, "Pedido")
        
    elif opcion == "Historial Venta":   
        titel_label = tk.Label(
            self.info_frame,
            text="Historial de Ventas",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 19, "bold"),
        )
        titel_label.place(x=0, y=0)
        
        Historial(self)
        Cargar_Solicitudes(self, "Venta")
         
    elif opcion == "Historial Reparacion": 
        titel_label = tk.Label(
            self.info_frame,
            text="Historial de Reparaciones",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 19, "bold"),
        )
        titel_label.place(x=0, y=0)
        
        Historial(self)
        Cargar_Solicitudes(self, "Reparacion")
    
    elif opcion == "Historial x Cliente":
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
        self.cedula_buscar_label.place(x=500, y=10)

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
        self.cedula_buscar_entry.place(x=655, y=10)
        self.cedula_buscar_entry.bind("<Return>", lambda event: Solicitudes_Clientes(self))

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
            command=lambda: Solicitudes_Clientes(self),
        )
        self.buscar.place(x=834, y=10)

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
            background=[("selected", "#1778FB")],
            foreground=[("selected", "#1778FB")],
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

        self.frame_lista = Frame(self.info_frame, bg="#f0f0f0", colormap="new")
        self.frame_lista.place(x=0, y=55, width=865, height=600)

        # Crear el Treeview con el estilo personalizado
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("id", "fecha", "tipo", "descripcion", "estado", "fecha_entrega"),
            show="headings",
            style="Treeview",
        )

        column_widths = {
            "id": 60,
            "fecha": 90,
            "tipo": 100,
            "descripcion": 350,
            "estado": 100,
            "fecha_entrega": 90,
        }

        # Configurar los encabezados de las columnas
        self.tree.heading("id", text="N°", anchor="center")
        self.tree.heading("fecha", text="Fecha", anchor="center")
        self.tree.heading("tipo", text="Tipo", anchor="center")
        self.tree.heading("descripcion", text="Detalles", anchor="center")
        self.tree.heading("estado", text="Estado", anchor="center")
        self.tree.heading("fecha_entrega", text="Entrega", anchor="center")

        # Configurar la fuente para los encabezados y las filas
        self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
        self.tree.tag_configure("row", font=("Poppins", 10))

        # Configurar el ancho de las columnas y la alineación
        for col, width in column_widths.items():
            self.tree.column(col, minwidth=width, width=width, anchor="center")

        scrollbar_cover = tk.Frame(self.frame_lista, bg="#f0f0f0")
        scrollbar_cover.grid(row=0, column=1, sticky="ns", pady=(0, 295))

        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(
            self.frame_lista,
            orient="vertical",
            command=self.tree.yview,
            style="Vertical.TScrollbar",
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la barra de desplazamiento en el marco
        self.tree.grid(row=0, column=0, sticky="nsew", pady=(0, 295))
        scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

        # Configurar el marco de información
        self.frame_lista.grid_rowconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(0, weight=1)
        self.frame_lista.grid_columnconfigure(1, weight=0)
        
        #Demás informacion 
        titel_label = tk.Label(
            self.frame_lista,
            text="Agregar fecha de entrega:",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 14, "bold"),
        )
        titel_label.place(x=0, y=310)

        self.numero_orden_label1 = tk.Label(
            self.frame_lista,
            text="N° de orden",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.numero_orden_label1.place(x=0, y=352)

        self.numero_orden_entry1 = tk.Entry(
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
        self.numero_orden_entry1.place(x=0, y=382)

        self.fecha_entrega_label = tk.Label(
            self.frame_lista,
            text="Fecha entrega",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.fecha_entrega_label.place(x=235, y=352)

        if self.rol_programa != "System":
            style = ttk.Style()
            style.configure('Custom.DateEntry',
                            fieldbackground='#f0f0f0',
                            background='#f0f0f0',
                            foreground='#1778FB',
                            bordercolor='#f0f0f0',
                            relief='solid',
                            borderwidth=1,
                            arrowcolor='#1778FB')

            self.fecha_entrega_entry = DateEntry(
                self.frame_lista,
                width=17,
                year=2024,
                date_pattern="yyyy/MM/dd",
                font=("Helvetica", 14),
                state="readonly",
                style='Custom.DateEntry'  # Aplicar el estilo personalizado
            )
            self.fecha_entrega_entry.place(x=235, y=382)
            self.fecha_entrega_entry.config(justify="center")

        self.modificar_fecha_boton = tk.Button(
            self.frame_lista,
            text="Actualizar fecha",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: Agregar_Fecha_Entrega(self),
        )
        self.modificar_fecha_boton.place(x=470, y=382)

        #Informacion mas abajo
        self.titel_label = tk.Label(
            self.frame_lista,
            text="Descargar pdf por cliente:",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 14, "bold"),
        )
        self.titel_label.place(x=0, y=437)

        self.numero_orden_label2 = tk.Label(
            self.frame_lista,
            text="N° de orden",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.numero_orden_label2.place(x=0, y=479)

        self.numero_orden_entry2 = tk.Entry(
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
        self.numero_orden_entry2.place(x=0, y=509)

        self.descargar_pdf_boton = tk.Button(
            self.frame_lista,
            text="Descargar",
            font=("Poppins", 13, "bold"),
            width=17,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: descargar_datos(self),
        )
        self.descargar_pdf_boton.place(x=235, y=509)
        #self.descargar_pdf_boton.bind("<Return>", lambda event: Descargar_Archivo(self))

    elif opcion == "Inicio Historial":
        self.titulo_label = Label(
            self.info_frame,
            text="Interfaz",
            anchor="w",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 30),
        )
        self.titulo_label.place(x=200, y=135)

        self.titulo2_label = Label(
            self.info_frame,
            text="para operaciones\ndel historial",
            anchor="w",
            justify=LEFT,
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 36, "bold"),
        )
        self.titulo2_label.place(x=200, y=182)



def Historial(self):
    self.frame_lista = Frame(self.info_frame, bg="#f0f0f0", colormap="new")
    self.frame_lista.place(x=0, y=55, width=865, height=585)

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
        columns=(
            "id",
            "fecha",
            "tipo",
            "cedula",
            "descripcion",
            "precio",
            "estado",
            "garantia",
        ),
        show="headings",
        style="Treeview",
    )

    column_widths = {
        "id": 50,
        "fecha": 90,
        "tipo": 90,
        "cedula": 90,
        "descripcion": 300,
        "precio": 80,
        "estado": 90,
        "garantia": 75,
    }

    # Configurar los encabezados de las columnas
    self.tree.heading("id", text="N°", anchor="center")
    self.tree.heading("fecha", text="Fecha", anchor="center")
    self.tree.heading("tipo", text="Tipo", anchor="center")
    self.tree.heading("cedula", text="Cliente", anchor="center")
    self.tree.heading("descripcion", text="Detalles", anchor="center")
    self.tree.heading("precio", text="Precio", anchor="center")
    self.tree.heading("estado", text="Estado", anchor="center")
    self.tree.heading("garantia", text="Garantia", anchor="center")

    # Configurar la fuente para los encabezados y las filas
    self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
    self.tree.tag_configure("row", font=("Poppins", 10))

    # Configurar el ancho de las columnas y la alineación
    for col, width in column_widths.items():
        self.tree.column(col, minwidth=width, width=width, anchor="center")

    scrollbar_cover = tk.Frame(self.frame_lista, bg="#DCEBFF")
    scrollbar_cover.grid(row=0, column=1, sticky="ns", pady=(0, 80))

    # Crear la barra de desplazamiento
    scrollbar = ttk.Scrollbar(
        self.frame_lista,
        orient="vertical",
        command=self.tree.yview,
        style="Vertical.TScrollbar",
    )
    self.tree.configure(yscrollcommand=scrollbar.set)

    # Colocar el Treeview y la barra de desplazamiento en el marco
    self.tree.grid(row=0, column=0, sticky="nsew", pady=(0, 80))
    scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

    # Configurar el marco de información
    self.frame_lista.grid_rowconfigure(0, weight=1)
    self.frame_lista.grid_columnconfigure(0, weight=1)
    self.frame_lista.grid_columnconfigure(1, weight=0)
    
    
 
def descargar_datos(self):
    numero_solicitud = self.numero_orden_entry2.get()
    if len(numero_solicitud) < 1:
        messagebox.showerror("Error", "Ingrese un numero por favor")
        return
    
    datos_solicitud = obtener_datos_solicitud(numero_solicitud)
    if datos_solicitud is not None:
        guardar_datos_en_excel(datos_solicitud) 
    