import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD


def agregar_cliente(self):
    subventana = tk.Toplevel()
    subventana.title("Tempus - Agregar Clientes")
    subventana.geometry("420x482")
    subventana.resizable(0, 0)

    # Frame for client data
    self.lgn_frame = Frame(subventana, bg="#FFFFFF")
    self.lgn_frame.pack(fill=tk.BOTH)

    # Title label
    title_label = tk.Label(
        self.lgn_frame,
        text=" Datos del cliente\n Ingresa la información del cliente.",
        justify=LEFT,
        anchor="w",
        font=("Helvetica", 13, BOLD),
        bg="#1E90FF",
        fg="#FFFFFF",
        height=3,
    )
    title_label.pack(fill=tk.BOTH, pady=14, padx=18)




    # Username label and entry
    self.nombre_label = Label(
        self.lgn_frame,
        text="Usuario",
        justify=LEFT,
        anchor="w",
        bg="#FFFFFF",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.nombre_label.pack(fill=tk.X, pady=(15,6), padx=(20,20))
    
    
    self.nombre_entry = Entry(
        self.lgn_frame,
        relief=FLAT,
        bg="#FFFFFF",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        highlightbackground="#87CEFA",
        highlightthickness=2,
    )
    self.nombre_entry.pack(fill=tk.X, pady=(0,6), padx=(20,20))
    
    
    # Username label and entry
    self.apellido_label = Label(
        self.lgn_frame,
        text="Apellido",
        justify=LEFT,
        anchor="w",
        bg="#FFFFFF",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.apellido_label.pack(fill=tk.X, pady=(15,6), padx=(20,20))
    
    
    self.apellido_entry = Entry(
        self.lgn_frame,
        relief=FLAT,
        bg="#FFFFFF",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        highlightbackground="#87CEFA",
        highlightthickness=2,
    )
    self.apellido_entry.pack(fill=tk.X, pady=(0,6), padx=(20,20))
    
    
    
    # Username label and entry
    self.cedula_label = Label(
        self.lgn_frame,
        text="Cédula",
        justify=LEFT,
        anchor="w",
        bg="#FFFFFF",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.cedula_label.pack(fill=tk.X, pady=(15,6), padx=(20,20))
    
    
    self.cedula_entry = Entry(
        self.lgn_frame,
        relief=FLAT,
        bg="#FFFFFF",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        highlightbackground="#87CEFA",
        highlightthickness=2,
    )
    self.cedula_entry.pack(fill=tk.X, pady=(0,6), padx=(20,20))
    
    
    # Username label and entry
    self.telefono_label = Label(
        self.lgn_frame,
        text="Teléfono",
        justify=LEFT,
        anchor="w",
        bg="#FFFFFF",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.telefono_label.pack(fill=tk.X, pady=(15,6), padx=(20,20))
    
    
    self.telefono_entry = Entry(
        self.lgn_frame,
        relief=FLAT,
        bg="#FFFFFF",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
        highlightbackground="#87CEFA",
        highlightthickness=2,
    )
    self.telefono_entry.pack(fill=tk.X, pady=(0,6), padx=(20,20))
    
    
    guardar_button = Button(
        self.lgn_frame,
        text="Aceptar",
        font=("yu gothic ui", 13, "bold"),
        width=12,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#3047ff",
        fg="white",
        command=lambda: RecuperarSesion(self=self, subventana=subventana),
    )
    guardar_button.pack(pady=(24, 0), padx=(50, 30) , side = LEFT)

    # mostrar información de seguridad temporal
    cancelar_button = Button(
        self.lgn_frame,
        text="Cancelar",
        font=("yu gothic ui", 13, "bold"),
        width=12,
        bd=0,
        bg="#858F94",
        cursor="hand2",
        activebackground="#3047ff",
        fg="white",
        command=lambda: subventana.destroy(),
    )
    cancelar_button.pack(pady=(24, 0), padx=(30, 50), side = RIGHT)