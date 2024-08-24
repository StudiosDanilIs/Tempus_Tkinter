import re
import tkinter as tk
from tkinter import *
from tkinter import Frame
import tkinter.messagebox as messagebox
from BaseDatos.ModificarUsuarios import ModificarUsuarios

class VentanaPrincipal:
    def __init__(self, nombre, nombre_rol):
        self.root2 = tk.Tk()
        self.root2.resizable(0, 0)
        self.root2.geometry("750x450")
        self.nombre = nombre
        self.nombre_rol = nombre_rol
        
        self.label_info = Frame(self.root2, bg="#f0f0f0")
        self.label_info.pack(expand=tk.YES, fill=tk.BOTH)
        
        titulo_label = Label(
            self.label_info,
            text=f"{self.nombre}",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 18, "bold"),
        )
        titulo_label.place(x=110, y=20)
        
        titulo_label = Label(
            self.label_info,
            text=f"{self.nombre_rol}",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 15),
        )
        titulo_label.place(x=110, y=50)
        
        
        self.titulo_label = Label(
            self.label_info,
            text="Restaurar Usuarios Olvidados",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 17, "bold"),
        )
        self.titulo_label.place(x=300, y=30)

        self.cedula_agregar_label = Label(
            self.label_info,
            text="Cédula del Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_agregar_label.place(x=110, y=140)

        self.cedula_agregar = Entry(
            self.label_info,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.cedula_agregar.place(x=110, y=170)
        self.cedula_agregar.bind(
            "<Return>", lambda event: self.nombre_agregar.focus_set()
        )

        self.nombre_agregar_label = Label(
            self.label_info,
            text="Nombre",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nombre_agregar_label.place(x=400, y=140)

        self.nombre_agregar = Entry(
            self.label_info,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
        )
        self.nombre_agregar.place(x=400, y=170)
        self.nombre_agregar.bind(
            "<Return>", lambda event: self.nuevo_usuario_agregar.focus_set()
        )

        self.nuevo_usuario_agregar_label = Label(
            self.label_info,
            text="Nuevo Usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nuevo_usuario_agregar_label.place(x=110, y=240)

        self.nuevo_usuario_agregar = Entry(
            self.label_info,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(self.validate_ingresar), "%P"),
        )
        self.nuevo_usuario_agregar.place(x=110, y=270)
        self.nuevo_usuario_agregar.bind(
            "<Return>", lambda event: self.nueva_clave_agregar.focus_set()
        )
        
        self.nueva_clave_agregar_label = Label(
            self.label_info,
            text="Nueva Clave",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nueva_clave_agregar_label.place(x=400, y=240)
        
        self.nueva_clave_agregar = Entry(
            self.label_info,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            width=25,
            validate="key",
            validatecommand=(self.root2.register(self.validate_ingresar), "%P"),
        )
        self.nueva_clave_agregar.place(x=400, y=270)
        self.nueva_clave_agregar.bind("<Return>", lambda event: ModificarUsuarios(self, self.root2))
        
        self.agregar_usuarios_boton = tk.Button(
            self.label_info,
            text="Guardar Datos",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=lambda: ModificarUsuarios(self, self.root2)
        )
        self.agregar_usuarios_boton.place(x=120, y=350)
        
        
        self.cancelar_boton = tk.Button(
            self.label_info,
            text="Cerrar Sesión",
            font=("Poppins", 13, "bold"),
            width=20,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#1778FB",
            fg="white",
            command=self.root2.destroy,
        )
        self.cancelar_boton.place(x=415, y=350)
        

    def cerrar(self):
        self.root2.destroy()


    def validate_ingresar(self, new_value):
        # Permitir solo letras, números y un símbolo especial (por ejemplo, @)
        pattern = r"^[a-zA-Z0-9@._-]*$"  # Incluye los símbolos permitidos

        # Verificar si hay espacios
        if " " in new_value:
            return False

        # Verificar la longitud
        if len(new_value) > 40:
            return False

        # Verificar el patrón
        if not re.match(pattern, new_value):
            return False

        # Verificar que solo haya un símbolo especial de cada tipo
        if (
            new_value.count("@") > 1
            or new_value.count(".") > 1
            or new_value.count("_") > 1
            or new_value.count("-") > 1
        ):
            return False

        return True


# Crear una instancia de la ventana principal
if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.root2.mainloop()