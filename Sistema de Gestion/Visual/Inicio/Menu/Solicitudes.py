from tkinter import *
import tkinter as tk
from tkinter import ttk
import util.PhotoImagenes as utl
from tkcalendar import DateEntry
from tkinter import messagebox
from Modelo.Inicio.OpcionSolicitudes import (
    Agregar_Solicitud,
    Buscar_Solicitud,
    Modificar_Solicitud,
    Eliminar_Solicitud,
)


def mostrar_opcion3(self):
    self.subventana_abierta = False
    self.limpiar_contenido()
    self.root2.title("Crear Solicitudes")
    self.root2.geometry("1100x635")

    titulo_label = tk.Label(
        self.label_info,
        text="Creación de solicitudes",
        bg="#f0f0f0",
        fg="#1778FB",
        font=("Montserrat", 17, "bold"),
    )
    titulo_label.place(x=25, y=30)

    self.cedula_agregar_label = tk.Label(
        self.label_info,
        text="Cédula cliente",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.cedula_agregar_label.place(x=25, y=80)

    self.cedula_agregar = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        width=26,
        validate="key",
        validatecommand=(self.root2.register(validate_precios), "%P"),
    )
    self.cedula_agregar.place(x=25, y=113)
    self.cedula_agregar.bind(
        "<Return>", lambda event: self.descripcion_agregar.focus_set()
    )

    self.tipo_solicitud_label = Label(
        self.label_info,
        text="Tipo de solicitud",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.tipo_solicitud_label.place(x=25, y=158)

    self.tipo_solicitud = StringVar()
    self.tipo_solicitud.set("Pedido")

    self.radiobtn_pedido = Radiobutton(
        self.label_info,
        text="Pedidos",
        variable=self.tipo_solicitud,
        value="Pedido",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 12, "bold"),
    )
    self.radiobtn_pedido.place(x=25, y=191)

    self.radiobtn_venta = Radiobutton(
        self.label_info,
        text="Ventas",
        variable=self.tipo_solicitud,
        value="Venta",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 12, "bold"),
    )
    self.radiobtn_venta.place(x=125, y=191)

    self.radiobtn_reparacion = Radiobutton(
        self.label_info,
        text="Reparaciones",
        variable=self.tipo_solicitud,
        value="Reparacion",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 12, "bold"),
    )
    self.radiobtn_reparacion.place(x=25, y=224)

    self.fecha_solicitud_agregar_label = tk.Label(
        self.label_info,
        text="Fecha de solicitud",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.fecha_solicitud_agregar_label.place(x=25, y=269)

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

        self.fecha_solicitud_agregar = DateEntry(
            self.label_info,
            width=18,
            year=2024,
            date_pattern="YYYY/MM/DD",
            font=("Helvetica", 14),
            state="readonly",
            style="Custom.DateEntry",  # Aplicar el estilo personalizado
        )
        self.fecha_solicitud_agregar.place(x=25, y=302)
        self.fecha_solicitud_agregar.config(justify="center")

    self.descripcion_agregar_label = tk.Label(
        self.label_info,
        text="Descripción",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.descripcion_agregar_label.place(x=325, y=80)

    self.descripcion_agregar = tk.Text(
        self.label_info,
        height=5,
        width=26,
        font=("Poppins", 12, "bold"),
        fg="#0046A4",
        background="#f0f0f0",
        insertbackground="#1778FB",
        highlightthickness=2,
        highlightbackground="#1E90FF",
        relief=tk.FLAT,
    )
    self.descripcion_agregar.place(x=325, y=113)

    self.garantia_agregar_label = tk.Label(
        self.label_info,
        text="Garantía",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.garantia_agregar_label.place(x=325, y=234)

    self.garantia_agregar = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        width=26,
        validate="key",
        validatecommand=(self.root2.register(validate_garantia), "%P"),
    )
    self.garantia_agregar.place(x=325, y=267)
    self.garantia_agregar.bind(
        "<Return>", lambda event: self.precio_agregar.focus_set()
    )

    self.precio_agregar_label = tk.Label(
        self.label_info,
        text="Precio",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.precio_agregar_label.place(x=325, y=312)

    self.precio_agregar = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        width=26,
        validate="key",
        validatecommand=(self.root2.register(validate_precios), "%P"),
    )
    self.precio_agregar.place(x=325, y=345)
    self.precio_agregar.bind("<Return>", lambda event: self.abono_entry.focus_set())

    self.abono_label = tk.Label(
        self.label_info,
        text="Abonó",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.abono_label.place(x=625, y=80)

    self.abono_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        width=26,
        validate="key",
        validatecommand=(self.root2.register(validate_precios), "%P"),
    )
    self.abono_entry.place(x=625, y=113)

    self.fecha_abono_label = tk.Label(
        self.label_info,
        text="Fecha abono",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.fecha_abono_label.place(x=625, y=158)

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

        self.fecha_abono_entry = DateEntry(
            self.label_info,
            width=18,
            year=2024,
            date_pattern="YYYY/MM/DD",
            font=("Helvetica", 14),
            state="readonly",
            style="Custom.DateEntry",  # Aplicar el estilo personalizado
        )
        self.fecha_abono_entry.place(x=625, y=191)
        self.fecha_abono_entry.config(justify="center")

    self.tipo_elegir_label = Label(
        self.label_info,
        text="Deseas agregar la\nfecha de entrega",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.tipo_elegir_label.place(x=625, y=236)

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
    self.radiobtn_pedido.place(x=625, y=278)

    self.radiobtn_venta = Radiobutton(
        self.label_info,
        text="No",
        variable=self.tipo_elegir,
        value="2",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 12, "bold"),
    )
    self.radiobtn_venta.place(x=680, y=278)

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
            self.label_info,
            width=18,
            year=2024,
            date_pattern="YYYY/MM/DD",
            font=("Helvetica", 14),
            state="readonly",
            style="Custom.DateEntry",  # Aplicar el estilo personalizado
        )
        self.fecha_entrega_entry.place(x=625, y=312)
        self.fecha_entrega_entry.config(justify="center")

    self.title_label = tk.Label(
        self.label_info,
        text="Buscar solicitud",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 14, "bold"),
    )
    self.title_label.place(x=493, y=30)

    self.buscar_id_entry = tk.Entry(
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
        validatecommand=(self.root2.register(validate_precios), "%P"),
    )
    self.buscar_id_entry.place(x=655, y=30)
    self.buscar_id_entry.bind("<Return>", lambda event: Buscar_Solicitud(self))

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
        command=lambda: Buscar_Solicitud(self),
    )
    self.buscar.place(x=775, y=30)

    self.guardar_pedido_button = tk.Button(
        self.label_info,
        text="Agregar solicitud",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Agregar_Solicitud(self),
    )
    self.guardar_pedido_button.place(x=625, y=375)

    if self.rol_programa == "Administrador":
        self.modificar_solicitud_button = tk.Button(
            self.label_info,
            text="Modificar solicitud",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            state="disabled",
            command=lambda: Modificar_Solicitud(self),
        )
        self.modificar_solicitud_button.place(x=625, y=417)
    else:
        self.modificar_solicitud_button = tk.Button(
            self.label_info,
            text="Modificar solicitud",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            state="disabled",
            command=lambda: messagebox.showerror(
                "Error", "No Tienes los Permisos Necesarios"
            ),
        )
        self.modificar_solicitud_button.place(x=625, y=417)

    titulo_label = tk.Label(
        self.label_info,
        text="Eliminar solicitud",
        bg="#f0f0f0",
        fg="#1778FB",
        font=("Montserrat", 17, "bold"),
    )
    titulo_label.place(x=25, y=405)

    self.eliminar_solicitud_label = tk.Label(
        self.label_info,
        text="Numero solicitud",
        anchor="w",
        justify="left",
        bg="#f0f0f0",
        fg="#1E90FF",
        font=("Poppins", 13, "bold"),
    )
    self.eliminar_solicitud_label.place(x=25, y=450)

    self.eliminar_solicitud_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        width=19,
        justify="center",
        validate="key",
        validatecommand=(self.root2.register(validate_precios), "%P"),
    )
    self.eliminar_solicitud_entry.place(x=25, y=483)

    if self.rol_programa == "Administrador":
        self.eliminar_solicitud_button1 = tk.Button(
            self.label_info,
            text="Eliminar solicitud",
            font=("Poppins", 13, "bold"),
            width=17,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: Eliminar_Solicitud(self),
        )
        self.eliminar_solicitud_button1.place(x=25, y=530)
    else:
        self.eliminar_solicitud_button2 = tk.Button(
            self.label_info,
            text="Eliminar solicitud",
            font=("Poppins", 13, "bold"),
            width=17,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: messagebox.showerror(
                "Error", "No Tienes los Permisos Necesarios"
            ),
        )
        self.eliminar_solicitud_button2.place(x=25, y=530)


def validate_cedula(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False


def validate_garantia(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 3:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False


def validate_precios(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False
