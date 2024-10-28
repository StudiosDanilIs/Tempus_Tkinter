import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from Modelo.Inicio.OpcionesPagos import Cargar_Pagos, Agregar_Pago


def mostrar_opcion4(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.root2.title("Registrar y Verificar Pagos")
    self.root2.geometry("1100x635")

    self.info_frame = Frame(self.label_info, bg="#f0f0f0", colormap="new")
    self.info_frame.place(x=30, y=30, width=680, height=560)

    titel_label = tk.Label(
        self.label_info,
        text="Registrar pagos pendientes",
        fg="#1778FB",
        bg="#f0f0f0",
        font=("Poppins", 18, "bold"),
    )
    titel_label.place(x=30, y=25)

    self.title_label = tk.Label(
        self.label_info,
        text="Buscar solicitud",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 14, "bold"),
    )
    self.title_label.place(x=463, y=30)

    self.buscar_pagos_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=12,
        justify="center",
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_numeros), "%P"),
    )
    self.buscar_pagos_entry.place(x=625, y=30)
    self.buscar_pagos_entry.bind("<Return>", lambda event: Cargar_Pagos(self))

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
        command=lambda: Cargar_Pagos(self),
    )
    self.buscar.place(x=745, y=30)

    self.pago_label = tk.Label(
        self.label_info,
        text="Ingresar pago",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.pago_label.place(x=30, y=95)

    self.pago_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=19,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_numeros), "%P"),
    )
    self.pago_entry.place(x=30, y=128)

    self.fecha_pago_label = tk.Label(
        self.label_info,
        text="Fecha entrega",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.fecha_pago_label.place(x=250, y=95)

    if self.rol_programa != "System":
        style = ttk.Style()
        style.configure(
            "Custom.DateEntry",
            fieldbackground="#f0f0f0",
            background="#f0f0f0",
            foreground="#1778FB",
            bordercolor="#f0f0f0",
            relief="solid",
            borderwidth=1,
            arrowcolor="#1778FB",
        )

        self.fecha_pago_entry = DateEntry(
            self.info_frame,
            width=15,
            year=2024,
            date_pattern="YYYY/MM/DD",
            font=("Helvetica", 14),
            state="readonly",
            style="Custom.DateEntry",  # Aplicar el estilo personalizado
        )
        self.fecha_pago_entry.place(x=220, y=100)
        self.fecha_pago_entry.config(justify="center")

    self.tipo_elegir_label = Label(
        self.label_info,
        text="Deseas agregar la\nfecha de entrega",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.tipo_elegir_label.place(x=480, y=95)

    self.tipo_elegir = StringVar()
    self.tipo_elegir.set("2")

    self.radiobtn_pedido = Radiobutton(
        self.label_info,
        text="Si",
        variable=self.tipo_elegir,
        value="1",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 12, "bold"),
    )
    self.radiobtn_pedido.place(x=480, y=140)

    self.radiobtn_venta = Radiobutton(
        self.label_info,
        text="No",
        variable=self.tipo_elegir,
        value="2",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 12, "bold"),
    )
    self.radiobtn_venta.place(x=535, y=140)

    if self.rol_programa != "SystemLoad":
        style = ttk.Style()
        style.configure(
            "Custom.DateEntry",
            fieldbackground="#f0f0f0",
            background="#f0f0f0",
            foreground="#1778FB",
            bordercolor="#f0f0f0",
            relief="solid",
            borderwidth=1,
            arrowcolor="#1778FB",
        )

        self.fecha_entrega_entry = DateEntry(
            self.info_frame,
            width=18,
            year=2024,
            date_pattern="YYYY/MM/DD",
            font=("Helvetica", 14),
            state="readonly",
            style="Custom.DateEntry",  # Aplicar el estilo personalizado
        )
        self.fecha_entrega_entry.place(x=450, y=150)
        self.fecha_entrega_entry.config(justify="center")

    self.guardar_clientes_button = tk.Button(
        self.label_info,
        text="Registrar pago",
        font=("Poppins", 13, "bold"),
        width=17,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Agregar_Pago(self),
    )
    self.guardar_clientes_button.place(x=30, y=178)

    titel_label = tk.Label(
        self.label_info,
        text="Solicitud de cliente a pagar",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    titel_label.place(x=30, y=290)
    
    
    self.actualizar = utl.leer_imagen("actualizar.png", size=(27, 27))
    self.buscar = tk.Button(
        self.label_info,
        width=30,
        image=self.actualizar,
        bg="#f0f0f0",
        activebackground="#f0f0f0",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: Cargar_Pagos(self),
    )
    self.buscar.place(x=680, y=290)
    

    self.label_precio_total = tk.Label(
        self.label_info,
        text="Precio total:",
        anchor="w",
        justify="left",
        fg="#1778FB",
        bg="#f0f0f0",
        font=("Poppins", 15, "bold"),
    )
    self.label_precio_total.place(x=730, y=320)

    self.label_monto_restante = tk.Label(
        self.label_info,
        text="Monto a pagar:",
        anchor="w",
        justify="left",
        fg="#1778FB",
        bg="#f0f0f0",
        font=("Poppins", 15, "bold"),
    )
    self.label_monto_restante.place(x=730, y=400)

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
            "nombre",
            "documento",
            "precio",
            "abono",
            "fecha",
            "estado",
        ),
        show="headings",
        style="Treeview",
    )

    column_widths = {
        "nombre": 90,
        "documento": 80,
        "precio": 90,
        "abono": 90,
        "fecha": 80,
        "estado": 90,
    }

    # Configurar los encabezados de las columnas
    self.tree.heading("nombre", text="Nombre", anchor="center")
    self.tree.heading("documento", text="Documento", anchor="center")
    self.tree.heading("precio", text="Precio", anchor="center")
    self.tree.heading("abono", text="Abono", anchor="center")
    self.tree.heading("fecha", text="Fecha pago", anchor="center")
    self.tree.heading("estado", text="Estado", anchor="center")

    # Configurar la fuente para los encabezados y las filas
    self.tree.tag_configure("heading", font=("Poppins", 12, "bold"))
    self.tree.tag_configure("row", font=("Poppins", 10))

    # Configurar el ancho de las columnas y la alineación
    for col, width in column_widths.items():
        self.tree.column(col, minwidth=width, width=width, anchor="center")

    scrollbar_cover = tk.Frame(self.info_frame, bg="#DCEBFF")
    scrollbar_cover.grid(row=0, column=1, sticky="ns", pady=(290, 10))

    # Crear la barra de desplazamiento
    scrollbar = ttk.Scrollbar(
        self.info_frame,
        orient="vertical",
        command=self.tree.yview,
        style="Vertical.TScrollbar",
    )
    self.tree.configure(yscrollcommand=scrollbar.set)

    # Colocar el Treeview y la barra de desplazamiento en el marco
    self.tree.grid(row=0, column=0, sticky="nsew", pady=(290, 10))
    scrollbar.place(in_=scrollbar_cover, x=0, y=0, relheight=1)

    # Configurar el marco de información
    self.info_frame.grid_rowconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(1, weight=0)


def validate_numeros(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False
