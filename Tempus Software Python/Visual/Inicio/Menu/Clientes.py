from tkinter import *
import tkinter as tk
from tkinter import ttk
import util.PhotoImagenes as utl
from tkinter import messagebox
from Modelo.Inicio.OpcionClientes import (
    Agregar_Cliente,
    Modificar_Cliente,
    Eliminar_Cliente,
    Buscar_Cliente,
    Obtener_Clientes
)


def mostrar_opcion3(self):
    # Limpiar el contenido del frame principal
    self.limpiar_contenido()
    self.subventana_abierta = False
    self.root2.title("Area de Clientes")

    # Titulo de la ventana
    titel_label = tk.Label(
        self.label_info,
        text="Informacion del Cliente",
        fg="#1778FB",
        bg="#f0f0f0",
        font=("Poppins", 17, "bold"),
    )
    titel_label.place(x=25, y=30)

    # Area del Nombre del Cliente
    self.nombre_label = tk.Label(
        self.label_info,
        text="Nombre",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.nombre_label.place(x=25, y=75)

    self.nombre_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_name), "%P"),
    )
    self.nombre_entry.place(x=25, y=105)
    self.nombre_entry.bind("<Return>", lambda event: self.apellido_entry.focus_set())

    # Area del Apellido del Cliente
    self.apellido_label = tk.Label(
        self.label_info,
        text="Apellido",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.apellido_label.place(x=25, y=145)
    self.apellido_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_name), "%P"),
    )
    self.apellido_entry.place(x=25, y=175)
    self.apellido_entry.bind(
        "<Return>", lambda event: self.tipo_cedula_entry.focus_set()
    )

    # Area de Cedula del Cliente
    self.cedula_label = tk.Label(
        self.label_info,
        text="Cedula",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.cedula_label.place(x=25, y=215)
    self.tipo_cedula_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        justify=tk.CENTER,
        width=2,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        validate="key",
        validatecommand=(self.root2.register(validate_clientes), "%P"),
    )
    self.tipo_cedula_entry.place(x=25, y=245)
    self.tipo_cedula_entry.bind("<Return>", lambda event: self.cedula_entry.focus_set())
    self.cedula_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=23,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_document), "%P"),
    )
    self.cedula_entry.place(x=67, y=245)
    self.cedula_entry.bind("<Return>", lambda event: self.telefono_entry.focus_set())

    # Area de Telefono del Cliente
    self.telefono_label = tk.Label(
        self.label_info,
        text="Telefono",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.telefono_label.place(x=25, y=285)
    self.telefono_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_phone), "%P"),
    )
    self.telefono_entry.place(x=25, y=315)
    self.telefono_entry.bind("<Return>", lambda event: self.direccion_text.focus_set())

    # Area de Direccion del Cliente
    self.direccion_label = tk.Label(
        self.label_info,
        text="Direccion",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.direccion_label.place(x=25, y=355)
    self.direccion_text = tk.Text(
        self.label_info,
        height=2,
        width=28,
        font=("Poppins", 12, "bold"),
        fg="#0046A4",
        background="#f0f0f0",
        insertbackground="#1778FB",
        highlightthickness=2,
        highlightbackground="#1E90FF",
        relief=tk.FLAT,
    )
    self.direccion_text.place(x=25, y=385)
    self.direccion_text.bind("<Return>", lambda event: Agregar_Cliente(self))

    # Boton para añadir cliente
    self.guardar_clientes_button = tk.Button(
        self.label_info,
        text="Añadir Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Agregar_Cliente(self),
    )
    self.guardar_clientes_button.place(x=50, y=465)

    # Validar que tipo de Cuenta es para usar diferentes funciones para cada una
    if self.rol_programa == "Programador" or self.rol_programa == "Administrador":
        # Boton para modificar cliente
        self.modificar_clientes_button = tk.Button(
            self.label_info,
            text="Modificar Cliente",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: Modificar_Cliente(self),
        )
        self.modificar_clientes_button.place(x=50, y=515)

        # botón para eliminar cliente
        self.eliminar_clientes_button = tk.Button(
            self.label_info,
            text="Eliminar Cliente",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: Eliminar_Cliente(self),
        )
        self.eliminar_clientes_button.place(x=50, y=565)
    # Solo para Niveles Bajos de Cuenta
    else:
        # Boton para modificar cliente pero no Funciona solo esta ahi
        self.modificar_clientes_button = tk.Button(
            self.label_info,
            text="Modificar Cliente",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: messagebox.showerror(
                "Error", "No Tienes los Permisos Necesarios"
            ),
        )
        self.modificar_clientes_button.place(x=50, y=515)

        # Boton para Eliminar cliente pero no Funciona solo esta ahi
        self.eliminar_clientes_button = tk.Button(
            self.label_info,
            text="Eliminar Cliente",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: messagebox.showerror(
                "Error", "No Tienes los Permisos Necesarios"
            ),
        )
        self.eliminar_clientes_button.place(x=50, y=565)

    # Area para buscar cliente por Documento
    self.buscar_cliente_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_document), "%P"),
    )
    self.buscar_cliente_entry.place(x=320, y=30)
    self.buscar_cliente_entry.bind("<Return>", lambda event: Buscar_Cliente(self))

    self.lupa = utl.leer_imagen(utl.resource_path("imagenes/lupa.png"), size=(31, 31))
    self.buscar = Button(
        self.label_info,
        width=30,
        image=self.lupa,
        bg="#f0f0f0",
        activebackground="#f0f0f0",
        bd=0,
        cursor="hand2",
        fg="white",
        command=lambda: Buscar_Cliente(self),
    )
    self.buscar.place(x=585, y=30)
    
    self.eliminar_clientes_button = tk.Button(
        self.label_info,
        text="Refrescar Clientes",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Obtener_Clientes(self),
    )
    self.eliminar_clientes_button.place(x=702, y=30)
    
      
    
    self.info_frame = Frame(self.label_info, bg="#80C5FF")
    self.info_frame.place(x=320, y=80, width=590, height=515)

    self.tree = ttk.Treeview(self.info_frame, columns=("ID", "Nombre", "Apellido", "Cedula", "Telefono"), show="headings")
    self.tree.heading("ID", text="#")
    self.tree.heading("Nombre", text="Nombre")
    self.tree.heading("Apellido", text="Apellido")
    self.tree.heading("Cedula", text="Cedula")
    self.tree.heading("Telefono", text="Telefono")

    scrollbar = ttk.Scrollbar(self.info_frame, orient="vertical", command=self.tree.yview)
    self.tree.configure(yscrollcommand=scrollbar.set)

    self.tree.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configurar el grid para que se ajuste al tamaño del frame
    self.info_frame.grid_rowconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(1, weight=0)
    
    Obtener_Clientes(self)
        



# Funciones para validar Datos de Clientes
def validate_clientes(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 1:
        return False
    if new_value:
        allowed_values = ["V", "C", "J", "P"]
        return new_value.upper() in allowed_values
    return True


def validate_name(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 20:
        return False
    if new_value.isalpha() or new_value == "":
        return True
    return False


def validate_phone(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 11:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False


def validate_document(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 10:
        return False
    if new_value.isdigit() or new_value == "":
        return True
    return False
