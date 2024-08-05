from tkinter import *
import tkinter as tk
from tkinter import ttk

from SubVentanas.VerificarClave import Clave_Verificar as Clave 

def mostrar_opcion3(self):
    self.limpiar_contenido()
    self.subventana_abierta = False
    self.root2.title("Clientes")

    titel_label = tk.Label(
        self.label_info,
        text="Informacion del Cliente",
        fg="#1778FB",
        bg="#FFFFFF",
        font=("Poppins", 17, "bold"),
    )
    titel_label.place(x=10, y=10)

    # cedula opcion de recuperación
    self.nombre_label = tk.Label(
        self.label_info,
        text="Nombre",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("Poppins", 13, "bold"),
    )
    self.nombre_label.place(x=10, y=55)

    # entrada de cedula
    self.nombre_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_name), "%P"),
    )
    self.nombre_entry.place(x=10, y=85)
    
    self.nombre_entry.bind("<Return>", lambda event: self.apellido_entry.focus_set())

    # usurario opcion de recuperación
    self.apellido_label = tk.Label(
        self.label_info,
        text="Apellido",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("Poppins", 13, "bold"),
    )
    self.apellido_label.place(x=10, y=125)

    # entrada de usuario y  validación de tabulador
    self.apellido_entry = tk.Entry(  # Cambié el nombre de la variable
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_name), "%P"),
    )
    self.apellido_entry.place(x=10, y=155)
    self.apellido_entry.bind("<Return>", lambda event: self.cedula_entry2.focus_set())
    
    # clave opcion de recuperación
    self.cedula_label = tk.Label(  # Cambié el nombre de la variable
        self.label_info,
        text="Cedula",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("Poppins", 13, "bold"),
    )
    self.cedula_label.place(x=10, y=195)

    # Crear un estilo para el Combobox con borde de color
    self.cedula_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        justify=tk.CENTER,
        width=2,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        validate="key",
        validatecommand=(self.root2.register(validate_clientes), "%P"),
    )
    self.cedula_entry.place(x=10, y=225)

    self.cedula_entry2 = tk.Entry(  # Cambié el nombre de la variable
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=23,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_document), "%P"),
    )
    self.cedula_entry2.place(x=53, y=225)
    self.cedula_entry2.bind("<Return>", lambda event: self.telefono_entry.focus_set())

    # usurario opcion de recuperación
    self.telefono_label = tk.Label(  # Cambié el nombre de la variable
        self.label_info,
        text="Telefono",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("Poppins", 13, "bold"),
    )
    self.telefono_label.place(x=10, y=265)

    # entrada de usuario y  validación de tabulador
    self.telefono_entry = tk.Entry(  # Cambié el nombre de la variable
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(self.root2.register(validate_phone), "%P"),
    )
    self.telefono_entry.place(x=10, y=295)
    self.telefono_entry.bind("<Return>", lambda event: self.direccion_text.focus_set())

    # usurario opcion de recuperación
    self.direccion_label = tk.Label(  # Cambié el nombre de la variable
        self.label_info,
        text="Direccion",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("Poppins", 13, "bold"),
    )
    self.direccion_label.place(x=10, y=335)

    # entrada de usuario y  validación de tabulador
    self.direccion_text = tk.Text(
        self.label_info,
        height=2,
        width=28,
        font=("Poppins", 12, "bold"),
        fg="#0046A4",
        insertbackground="#1778FB",
        highlightthickness=2,
        highlightbackground="#1E90FF",
        relief=tk.FLAT,
    )
    self.direccion_text.place(x=10, y=365)
    self.direccion_text.bind("<Return>", lambda event: self.nombre_entry.focus_set())

    # botón de guardar datos
    guardar_button1 = tk.Button(  # Cambié el nombre de la variable
        self.label_info,
        text="Añadir Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Clave(self),
    )
    guardar_button1.place(x=35, y=445)

    # botón de guardar datos
    guardar_button2 = tk.Button(  # Cambié el nombre de la variable
        self.label_info,
        text="Modificar Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Clave(self),
    )
    guardar_button2.place(x=35, y=505)

    # botón de guardar datos
    guardar_button3 = tk.Button(  # Cambié el nombre de la variable
        self.label_info,
        text="Eliminar Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
        command=lambda: Clave(self),
    )
    guardar_button3.place(x=35, y=565)


def validate_clientes(new_value):
    # Verifica que no haya espacios en blanco
    if " " in new_value:
        return False

    # Verifica que la longitud del valor sea menor o igual a 1
    if len(new_value) > 1:
        return False

    # Verifica si el valor está en la lista permitida (si no está vacío)
    if new_value:
        allowed_values = ["V", "C", "J", "P"]
        return new_value.upper() in allowed_values

    # Si el valor está vacío o se está borrando, permitir
    return True


def validate_name(new_value):
    if " " in new_value:
        return False

    # Verifica que la longitud del valor sea menor o igual a 1
    if len(new_value) > 20:
        return False

    if new_value.isalpha() or new_value == "":
        return True

    # Si el valor contiene números, la validación falla
    return False


def validate_phone(new_value):
    if " " in new_value:
        return False

    # Verifica que la longitud del valor sea menor o igual a 1
    if len(new_value) > 11:
        return False

    if new_value.isdigit() or new_value == "":
        return True

    # Si el valor contiene caracteres no numéricos, la validación falla
    return False


def validate_document(new_value):
    if " " in new_value:
        return False

    # Verifica que la longitud del valor sea menor o igual a 1
    if len(new_value) > 10:
        return False

    if new_value.isdigit() or new_value == "":
        return True

    # Si el valor contiene caracteres no numéricos, la validación falla
    return False