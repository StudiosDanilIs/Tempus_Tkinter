import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

def Clave_Verificar(self):
    if not self.subventana_abierta:
        sub_clave = tk.Toplevel()
        sub_clave.title("Mi Aplicación")
        sub_clave.geometry("380x180")
        sub_clave.resizable(0, 0)
        sub_clave.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

        # Frame de recupera cuenta
        self.lgn_frame = tk.Frame(sub_clave, bg="#FFFFFF")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Entrada de clave a verificar
        self.clave_unica_entry = tk.Entry(self.lgn_frame,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            justify=CENTER,
            width=25,
            fg="#0046A4",
            font=("Poppins", 15, "bold"),
            insertbackground="#1E90FF",
        )
        self.clave_unica_entry.place(x=50, y=40)

        # Botón de guardar datos
        guardar_button = tk.Button(
            self.lgn_frame,
            text="Enviar",
            font=("yu gothic ui", 13, "bold"),
            width=10,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
            command=lambda: enviar_datos(self)
        )
        guardar_button.place(x=50, y=100)

        # Botón de cancelar datos
        cancelar_button = tk.Button(
            self.lgn_frame,
            text="Cancelar",
            font=("yu gothic ui", 13, "bold"),
            width=10,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
            command=lambda: cerrar_sesion(self)
        )
        cancelar_button.place(x=225, y=100)
    

        def enviar_datos(self):
            # Lógica para enviar datos
            pass

        def cerrar_sesion(self):
            self.sub_clave.destroy()
            
        self.subventana_abierta = True
                
        def cerrar_sesion(self):
            self.subventana_abierta = False
            sub_clave.destroy()