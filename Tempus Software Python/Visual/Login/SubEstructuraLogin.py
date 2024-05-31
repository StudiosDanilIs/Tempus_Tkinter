import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from RelacionMariaDB.RecuperarCuenta import *


def SubventanaLogin(self):
    subventana = tk.Toplevel()
    subventana.title("Tempus - Recuperar Acceso")
    subventana.geometry("380x420")
    subventana.resizable(0, 0)
    
    self.lgn_frame = Frame(subventana, bg="#FFFFFF")
    self.lgn_frame.pack(fill=tk.BOTH)

    titel_label = Label(
        self.lgn_frame,
        text="Restaurar Cuenta",
        anchor="s",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("yu gothic ui", 15, "bold"),
    )
    titel_label.pack(fill=tk.X, padx=50, pady=23)

    self.cedula_label = Label(
        self.lgn_frame,
        text="Ingresa tu Cedula",
        anchor="w",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.cedula_label.pack(fill=tk.X, padx=25, pady=8)

    self.cedula_entry = Entry(
        self.lgn_frame,
        highlightthickness=0,
        relief=FLAT,
        bg="#FFFFFF",
        fg="#000000",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.cedula_entry.pack(fill=tk.X, padx=30, pady=0)

    self.cedula_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0
    )
    self.cedula_line.pack(fill=tk.X, padx=30, pady=1)

    self.nuevo_usuario_label = Label(
        self.lgn_frame,
        text="Nuevo Usuario",
        anchor="w",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.nuevo_usuario_label.pack(fill=tk.X, padx=25, pady=8)

    self.nuevo_usuario_entry = Entry(
        self.lgn_frame,
        highlightthickness=0,
        relief=FLAT,
        bg="#FFFFFF",
        fg="#000000",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.nuevo_usuario_entry.pack(fill=tk.X, padx=30, pady=0)

    self.nuevo_usuario_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0
    )
    self.nuevo_usuario_line.pack(fill=tk.X, padx=30, pady=1)

    self.nueva_clave_label = Label(
        self.lgn_frame,
        text="Nueva Calve",
        anchor="w",
        fg="#1E90FF",
        bg="#FFFFFF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.nueva_clave_label.pack(fill=tk.X, padx=25, pady=8)

    self.nueva_clave_entry = Entry(
        self.lgn_frame,
        highlightthickness=0,
        relief=FLAT,
        bg="#FFFFFF",
        fg="#000000",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.nueva_clave_entry.pack(fill=tk.X, padx=30, pady=0)

    self.nueva_clave_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0
    )
    self.nueva_clave_line.pack(fill=tk.X, padx=30, pady=1)

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
        command=lambda: RecuperarSesion(self=self, subventana=subventana),
    )
    guardar_button.pack(pady=20)


    self.forgot_button = Button(
        self.lgn_frame,
        text="Seguridad Tempus",
        font=("yu gothic ui", 13, "bold"),
        fg="#1E90FF",
        relief=FLAT,
        activebackground="#4169E1",
        borderwidth=0,
        background="#FFFFFF",
        cursor="hand2",
    )
    self.forgot_button.pack(pady=7)