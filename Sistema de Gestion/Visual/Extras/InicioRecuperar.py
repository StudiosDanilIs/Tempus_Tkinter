import re
import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from Modelo.Extras.ModificarUsuarios import ModificarUsuarios

class RestaurarUsuarios:
    def __init__(self, nombre, nombre_rol):
        self.root2 = tk.Tk()
        self.root2.resizable(0, 0)
        self.root2.geometry("600x400")
        self.root2.title("Operaciones de usuarios")
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
        titulo_label.place(x=40, y=20)
        
        titulo_label = Label(
            self.label_info,
            text=f"{self.nombre_rol}",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 15),
        )
        titulo_label.place(x=40, y=50)
        
        self.titulo_label = Label(
            self.label_info,
            text="Recuperar y Cambiar",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 18, "bold"),
        )
        self.titulo_label.place(x=280, y=20)
        
        self.titulo_label = Label(
            self.label_info,
            text="niveles de permisos",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 15),
        )
        self.titulo_label.place(x=280, y=50)
        
        self.cedula_agregar_label = Label(
            self.label_info,
            text="Cédula del usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.cedula_agregar_label.place(x=40, y=130)
        
        self.cedula_agregar = Entry(
            self.label_info,
            highlightthickness=2,
            highlightbackground="#1778FB",
            relief=tk.FLAT,
            fg="#0046A4",
            background="#f0f0f0",
            font=("Poppins", 12, "bold"),
            insertbackground="#1E90FF",
            justify="center",
            width=22,
            validate="key",
            validatecommand=(self.root2.register(self.validate_document), "%P"),
        )
        self.cedula_agregar.place(x=40, y=160)
        self.cedula_agregar.bind(
            "<Return>", lambda event: self.nuevo_usuario_agregar.focus_set()
        )
        
        self.tipo_cuenta_label = Label(
            self.label_info,
            text="Tipo de cuenta",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.tipo_cuenta_label.place(x=290, y=130)
        
        self.tipo_cuenta = StringVar()
        self.tipo_cuenta.set("3")
        
        self.radiobtn_admin = Radiobutton(
            self.label_info,
            text="Administrador",
            variable=self.tipo_cuenta,
            value="2",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 12, "bold"),
        )
        self.radiobtn_admin.place(x=290, y=160)
        
        self.radiobtn_empleado = Radiobutton(
            self.label_info,
            text="Empleado",
            variable=self.tipo_cuenta,
            value="3",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 12, "bold"),
        )
        self.radiobtn_empleado.place(x=430, y=160)
        
        self.nuevo_usuario_agregar_label = Label(
            self.label_info,
            text="Nuevo usuario",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nuevo_usuario_agregar_label.place(x=40, y=230)
        
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
        self.nuevo_usuario_agregar.place(x=40, y=260)
        self.nuevo_usuario_agregar.bind(
            "<Return>", lambda event: self.nueva_clave_agregar.focus_set()
        )
        
        self.nueva_clave_agregar_label = Label(
            self.label_info,
            text="Nueva clave",
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Poppins", 13, "bold"),
        )
        self.nueva_clave_agregar_label.place(x=290, y=230)
        
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
            show="*",
            validate="key",
            validatecommand=(self.root2.register(self.validate_ingresar), "%P"),
        )
        self.nueva_clave_agregar.place(x=290, y=260)
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
        self.agregar_usuarios_boton.place(x=60, y=310)
        
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
            command=self.root2.destroy
        )
        self.cancelar_boton.place(x=290, y=310)
    
    def cerrar(self):
        self.root2.destroy()
    
    def validate_ingresar(self, new_value):
        pattern = r"^[a-zA-Z0-9@._-]*$"  # Incluye los símbolos permitidos
        if " " in new_value:
            return False
        if len(new_value) > 40:
            return False
        if not re.match(pattern, new_value):
            return False
        if (
            new_value.count("@") > 1
            or new_value.count(".") > 1
            or new_value.count("_") > 1
            or new_value.count("-") > 1
        ):
            return False
        return True
    
    def validate_document(self, new_value):
        if " " in new_value:
            return False
        if len(new_value) > 10:
            return False
        if new_value.isdigit() or new_value == "":
            return True
        return False

# Crear una instancia de la ventana principal
if __name__ == "__main__":
    ventana = RestaurarUsuarios("NombreUsuario", "RolUsuario")
    ventana.root2.mainloop()
