import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
import util.PhotoImagenes as utl


def Pedidos(self):
    if not self.subventana_abierta:
        miniVentana = tk.Toplevel()
        miniVentana.title("Detalles de la Version")
        miniVentana.geometry("830x450")
        miniVentana.resizable(0, 0)
        miniVentana.configure(bg="#f0f0f0")
        miniVentana.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

        # Configuración del estilo
        titel_label = tk.Label(
            self.label_info,
            text="Buscar Solicitudes por Cliente",
            fg="#1778FB",
            bg="#f0f0f0",
            font=("Poppins", 19, "bold"),
        )
        titel_label.place(x=25, y=15)

        # Area del Nombre del Cliente
        self.cedula_buscar_label = tk.Label(
            self.label_info,
            text="Cedula del Cliente",
            fg="#1E90FF",
            bg="#f0f0f0",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_buscar_label.place(x=540, y=25)

        self.cedula_buscar_entry = tk.Entry(
            self.label_info,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            width=18,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
        )
        self.cedula_buscar_entry.place(x=695, y=25)
        
        self.lupa = utl.leer_imagen("lupa.png", size=(27, 27))
        self.buscar = tk.Button(
            self.label_info,
            width=30,
            image=self.lupa,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.buscar.place(x=874, y=25)
        
        
        
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
            "Treeview",
            background=[("selected", "#DCEBFF")],
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
            "Vertical.TScrollbar",
            troughcolor="#1778FB",
            background="#1778FB",
            relief="flat",
            borderwidth=1,
            width=10,
            highlightcolor="#1778FB",
            highlightbackground="#1778FB",
            highlightthickness=1
        )

        # Crear el marco de información
        self.info_frame = tk.Frame(self.label_info, bg="#DCEBFF", colormap='new')    
        self.info_frame.place(x=30, y=85, width=870, height=260)
        

        # Crear el Treeview con el estilo personalizado
        self.tree = ttk.Treeview(
            self.info_frame,
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
            "descargar": 150
        }

        # Configurar los encabezados de las columnas
        self.tree.heading("ID", text="#", anchor="center")
        self.tree.heading("fecha", text="Fecha", anchor="center")
        self.tree.heading("descripcion", text="Descripcion", anchor="center")
        self.tree.heading("precio", text="Precio", anchor="center")
        self.tree.heading("garantia", text="Garantía", anchor="center")
        self.tree.heading("descargar", text="Descargar PDF", anchor="center")

        # Configurar la fuente para los encabezados y las filas
        self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
        self.tree.tag_configure("row", font=("Poppins", 10))

        # Configurar el ancho de las columnas y la alineación        
        for col, width in column_widths.items():
            self.tree.column(col, minwidth=width, width=width, anchor="center")
        

        scrollbar_cover = tk.Frame(self.info_frame, bg="#DCEBFF")
        scrollbar_cover.grid(row=0, column=1, sticky="ns")
        
        # Crear la barra de desplazamiento
        scrollbar = ttk.Scrollbar(
            self.info_frame,
            orient="vertical",
            command=self.tree.yview,
            style="Vertical.TScrollbar",
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la barra de desplazamiento en el marco
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

        # Configurar el marco de información
        self.info_frame.grid_rowconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=0)


        # permite que la subventana se abra solo si no está abierta
        self.subventana_abierta = True

        def cerrar_sesion(self):
            self.subventana_abierta = False
            miniVentana.destroy()