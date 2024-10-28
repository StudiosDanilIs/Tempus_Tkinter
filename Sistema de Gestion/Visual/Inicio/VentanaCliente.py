from tkinter import *
import tkinter as tk
from tkinter import ttk
import util.PhotoImagenes as utl
from tkinter import messagebox
import mysql.connector


def VentanaEmergente(self):
    self.ventana_emergente = tk.Tk()
    self.ventana_emergente.title("Agregar Cliente Sección Emergente")
    self.ventana_emergente.geometry("320x565")
    self.ventana_emergente.resizable(0, 0)
    self.ventana_emergente.configure(bg="#f0f0f0")
    self.ventana_emergente.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

    # Creando frame principal para organizar elementos
    self.frame_cliente = Frame(self.ventana_emergente, bg="#f0f0f0")
    self.frame_cliente.pack(expand=tk.YES, fill=tk.BOTH)

    self.titel_label = tk.Label(
        self.frame_cliente,
        text="Agregar Clientes",
        fg="#1778FB",
        bg="#f0f0f0",
        font=("Poppins", 17, "bold"),
    )
    self.titel_label.place(x=25, y=30)

    # Área del Nombre del Cliente
    self.nombre_label = tk.Label(
        self.frame_cliente,
        text="Nombre",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.nombre_label.place(x=25, y=75)
    self.nombre_entry = tk.Entry(
        self.frame_cliente,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.ventana_emergente.register(validate_name), "%P"),
    )
    self.nombre_entry.place(x=25, y=108)
    self.nombre_entry.bind("<Return>", lambda event: self.apellido_entry.focus_set())

    # Área del Apellido del Cliente
    self.apellido_label = tk.Label(
        self.frame_cliente,
        text="Apellido",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.apellido_label.place(x=25, y=152)
    self.apellido_entry = tk.Entry(
        self.frame_cliente,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.ventana_emergente.register(validate_name), "%P"),
    )
    self.apellido_entry.place(x=25, y=185)
    self.apellido_entry.bind(
        "<Return>", lambda event: self.tipo_cedula_entry.focus_set()
    )

    # Área de Cédula del Cliente
    self.cedula_label = tk.Label(
        self.frame_cliente,
        text="Cédula",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.cedula_label.place(x=25, y=229)
    self.tipo_cedula_entry = tk.Entry(
        self.frame_cliente,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        justify=tk.CENTER,
        width=2,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        validate="key",
        validatecommand=(self.ventana_emergente.register(validate_clientes), "%P"),
    )
    self.tipo_cedula_entry.place(x=25, y=262)
    self.tipo_cedula_entry.bind("<Return>", lambda event: self.cedula_entry.focus_set())
    self.cedula_entry = tk.Entry(
        self.frame_cliente,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=23,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.ventana_emergente.register(validate_document), "%P"),
    )
    self.cedula_entry.place(x=67, y=262)
    self.cedula_entry.bind("<Return>", lambda event: self.telefono_entry.focus_set())

    # Área de Teléfono del Cliente
    self.telefono_label = tk.Label(
        self.frame_cliente,
        text="Teléfono",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.telefono_label.place(x=25, y=306)
    self.telefono_entry = tk.Entry(
        self.frame_cliente,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        background="#f0f0f0",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.ventana_emergente.register(validate_phone), "%P"),
    )
    self.telefono_entry.place(x=25, y=339)
    self.telefono_entry.bind("<Return>", lambda event: self.direccion_text.focus_set())

    # Área de Dirección del Cliente
    self.direccion_label = tk.Label(
        self.frame_cliente,
        text="Dirección",
        fg="#1E90FF",
        bg="#f0f0f0",
        font=("Poppins", 13, "bold"),
    )
    self.direccion_label.place(x=25, y=383)
    self.direccion_text = tk.Text(
        self.frame_cliente,
        height=4,
        width=28,
        font=("Poppins", 12, "bold"),
        fg="#0046A4",
        background="#f0f0f0",
        insertbackground="#1778FB",
        highlightthickness=2,
        highlightbackground="#1E90FF",
        relief=tk.FLAT,
    )
    self.direccion_text.place(x=25, y=416)

    # Botón para añadir cliente
    self.guardar_clientes_button = tk.Button(
        self.frame_cliente,
        text="Agregar cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Agregar_Cliente(self),
    )
    self.guardar_clientes_button.place(x=50, y=513)


def cerrar_sesion(self):
    self.ventana_emergente.destroy()


def validate_clientes(new_value):
    if " " in new_value:
        return False
    if len(new_value) > 1:
        return False
    if new_value:
        allowed_values = ["V", "J", "P", "E"]
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


def Agregar_Cliente(self):
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )
    
    # Datos a Ingresar en la Base de Datos
    name = self.nombre_entry.get().capitalize()
    apellido = self.apellido_entry.get().capitalize()
    documento = self.tipo_cedula_entry.get().capitalize()
    cedula_agregar = self.cedula_entry.get().lstrip('0')  # Remover ceros al principio
    telefono_agregar = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c").capitalize()

    # Validar cédula
    if not cedula_agregar.isdigit() or int(cedula_agregar) < 1000 or cedula_agregar != self.cedula_entry.get():
        messagebox.showerror(
            "Error", "Documento inválido ya que el ingresado no debe tener ceros por delante."
        )
        return

    # Validar teléfono
    if not telefono_agregar.isdigit() or telefono_agregar.count('0') > 1 or len(telefono_agregar) < 10:
        messagebox.showerror(
            "Error", "Número de teléfono inválido. Debe contener solo un cero y al menos 10 dígitos."
        )
        return

    # Verificar que los campos no estén vacíos
    if (
        len(name) < 3
        or len(apellido) < 3
        or len(cedula_agregar) < 5
        or len(telefono_agregar) < 10
        or len(direccion) < 10
    ):
        messagebox.showerror("Error", "Datos Incorrectos")
        return

    # Verificar si ya existe un Cliente con esos mismos datos
    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s OR Telefono = %s",
            (cedula_agregar, telefono_agregar),
        )
        resultado = cursor.fetchone()
        if resultado:
            # Si se encuentra un registro duplicado, mostrar un mensaje de error
            messagebox.showerror(
                message="Datos ya Existentes.",
                title="Error de Registro",
            )
        else:
            # Si no se encuentra ningún duplicado, registra los datos
            cursor.execute(
                "INSERT INTO datoscliente (Nombre, Apellido, Documento, Cedula, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, apellido, documento, cedula_agregar, telefono_agregar, direccion),
            )
            connection.commit()
            messagebox.showinfo(
                message="Cliente Guardado Exitosamente.", title="Registro"
            )
            cerrar_sesion(self)  # Limpia los campos después de guardar el cliente
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()
