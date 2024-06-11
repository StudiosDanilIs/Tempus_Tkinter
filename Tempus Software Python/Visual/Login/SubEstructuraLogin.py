import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from Modelo.Login.RecuperarCuenta import *


def SubventanaLogin(self):
    subventana = tk.Toplevel()
    subventana.title("Tempus - Recuperar Acceso")
    subventana.geometry("380x480")
    subventana.resizable(0, 0)

    # frame de recupera cuenta
    self.lgn_frame = Frame(subventana, bg="#E6F0F3")
    self.lgn_frame.pack(fill=tk.BOTH)

    titel_label = Label(
        self.lgn_frame,
        text="Restaurar Cuenta",
        anchor="s",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("yu gothic ui", 15, "bold"),
    )
    titel_label.pack(fill=tk.X, padx=50, pady=23)

    # cedula opcion de recuperación
    self.cedula_label = Label(
        self.lgn_frame,
        text="Ingresa tu Cédula",
        anchor="w",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("yu gothic ui", 13, "bold"),
    )
    self.cedula_label.pack(fill=tk.X, padx=25, pady=8)

    # entrada de cedula
    vcmd = self.root.register(validate_numeros)
    self.cedula_entry = Entry(
        self.lgn_frame,
        highlightthickness=0,
        relief=FLAT,
        bg="#E6F0F3",
        fg="#000000",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(vcmd, "%P"),
    )
    self.cedula_entry.pack(fill=tk.X, padx=30, pady=0)

    self.cedula_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0
    )
    self.cedula_line.pack(fill=tk.X, padx=30, pady=1)

    # usurario opcion de recuperación
    self.nuevo_usuario_label = Label(
        self.lgn_frame,
        text="Nuevo Usuario",
        anchor="w",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("yu gothic ui", 13, "bold"),
    )
    self.nuevo_usuario_label.pack(fill=tk.X, padx=25, pady=(30, 8))

    # entrada de usuario y  validación de tabulador
    vcmd = self.root.register(validate_tab)
    self.nuevo_usuario_entry = Entry(
        self.lgn_frame,
        highlightthickness=0,
        relief=FLAT,
        bg="#E6F0F3",
        fg="#000000",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(vcmd, "%P"),
    )
    self.nuevo_usuario_entry.pack(fill=tk.X, padx=30, pady=0)

    self.nuevo_usuario_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0
    )
    self.nuevo_usuario_line.pack(fill=tk.X, padx=30, pady=1)

    # clave opcion de recuperación
    self.nueva_clave_label = Label(
        self.lgn_frame,
        text="Nueva Clave",
        anchor="w",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("yu gothic ui", 13, "bold"),
    )
    self.nueva_clave_label.pack(fill=tk.X, padx=25, pady=(30, 8))

    # entrada de clave y  validación de tabulador
    vcmd = self.root.register(validate_tab)
    self.nueva_clave_entry = Entry(
        self.lgn_frame,
        highlightthickness=0,
        relief=FLAT,
        bg="#E6F0F3",
        fg="#000000",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        validate="key",
        validatecommand=(vcmd, "%P"),
    )
    self.nueva_clave_entry.pack(fill=tk.X, padx=30, pady=0)

    self.nueva_clave_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0
    )
    self.nueva_clave_line.pack(fill=tk.X, padx=30, pady=1)

    # botón de guardar datos
    guardar_button = Button(
        self.lgn_frame,
        text="Guardar Datos",
        font=("yu gothic ui", 13, "bold"),
        width=22,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#3047ff",
        fg="white",
        command=lambda: RecuperarSesion(self, subventana),
    )
    guardar_button.pack(pady=(35, 0))

    # mostrar información de seguridad temporal
    self.forgot_button = Button(
        self.lgn_frame,
        text="Seguridad Tempus",
        font=("yu gothic ui", 13, "bold"),
        fg="#1E90FF",
        relief=FLAT,
        activebackground="#4169E1",
        borderwidth=0,
        background="#E6F0F3",
        cursor="hand2",
    )
    self.forgot_button.pack(pady=15)


# Función para validar que no haya espacios en blanco en la entrada
def validate_tab(new_value):
    # Verifica que no haya espacios en blanco
    return not " " in new_value


def validate_numeros(new_value):
    if new_value == '':
        return True
    else:
        return new_value.isdigit()