from tkinter import *
import mysql.connector
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal

def verificar_sesion(self):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="210605",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    # Datos a Ingresar en la Base de Datos
    usuario = self.username_entry.get()
    password = self.password_entry.get()
    clave_unica = self.password_unica_entry.get()

    # Verificar si la clave única corresponde a la cuenta de administrador
    try:
        cursor.execute(
            "SELECT Cuenta FROM usuarios WHERE Clave_Unica = %s AND id_RolUsuario = (SELECT id_RolUsuario FROM rolusuario WHERE NombreRol = 'Administrador')",
            (clave_unica,),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Verificar si la cuenta y la contraseña son correctas y pertenecen a "Root System"
            cursor.execute(
                "SELECT Nombre, id_RolUsuario FROM usuarios WHERE Cuenta = %s AND Clave = %s AND id_RolUsuario = 0",
                (usuario, password),
            )
            resultado = cursor.fetchone()

            if resultado:
                # Muestra un mensaje de bienvenida y da acceso a la ventana principal
                messagebox.showinfo(
                    message="Bienvenido a Tempus Software", title="Mensaje"
                )
                self.root.destroy()
                VentanaPrincipal()
            else:
                messagebox.showerror(
                    message="La Cuenta no se Encuentra Registrada o no es 'Root System'.", title="Mensaje"
                )
        else:
            messagebox.showerror(
                message="Clave única incorrecta o no tienes permisos de administrador.",
                title="Mensaje",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()
