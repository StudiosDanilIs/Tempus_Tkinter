from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime, timedelta
from VentanaPrincipal import VentanaPrincipal

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
            # Verificar si la cuenta y la contraseña son correctas y pertenecen a "System"
            cursor.execute(
                "SELECT Nombre, id_RolUsuario, Time_Sesion FROM usuarios WHERE Cuenta = %s AND Clave = %s AND id_RolUsuario = '1'",
                (usuario, password),
            )
            resultado = cursor.fetchone()

            if resultado:
                nombre = resultado[0]
                id_rol = resultado[1]
                Time_Sesion = resultado[2]

                # Actualizar la hora de inicio de sesión y la duración de la sesión
                cursor.execute(
                    "UPDATE usuarios SET Time_Sesion = %s WHERE Cuenta = %s",
                    (2, usuario),
                )
                connection.commit()

                # Muestra un mensaje de bienvenida y da acceso a la ventana principal
                messagebox.showinfo(
                    message="Bienvenido a Tempus Software", title="Mensaje"
                )
                self.root.destroy()
                ventana_principal = VentanaPrincipal()
                # Establecer un temporizador para cerrar la sesión después de 1 minuto
                ventana_principal.root2.after(2 * 60 * 1000, lambda: cerrar_sesion(ventana_principal))
            else:
                messagebox.showerror(
                    message="La Cuenta no se Encuentra Registrada o no es 'System'.",
                    title="Mensaje",
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

def cerrar_sesion(ventana_principal):
    messagebox.showinfo(message="Tu sesión ha expirado.", title="Mensaje")
    ventana_principal.cerrar()
