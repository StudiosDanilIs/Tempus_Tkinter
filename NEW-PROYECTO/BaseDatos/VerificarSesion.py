from tkinter import *
import mysql.connector
from tkinter import messagebox
from Visual.Inicio import VentanaPrincipal

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
                "SELECT Nombre, id_RolUsuario FROM usuarios WHERE Cuenta = %s AND Clave = %s AND id_RolUsuario = '1'",
                (usuario, password),
            )
            resultado = cursor.fetchone()

            if resultado:
                nombre = resultado[0]
                id_rol = resultado[1]

                cursor.execute(
                    "SELECT NombreRol FROM rolusuario WHERE id_RolUsuario = %s",
                    (id_rol,),
                )
                nombre_rol_result = cursor.fetchone()

                if nombre_rol_result:
                    nombre_rol = nombre_rol_result[0]
                    # Muestra un mensaje de bienvenida y da acceso a la ventana principal
                    messagebox.showinfo(
                        message=f"Bienvenido {nombre} a Tempus Software", title="Mensaje"
                    )
                    self.root.destroy()
                    ventana_principal = VentanaPrincipal(nombre, nombre_rol)
                    # Establecer un temporizador para cerrar la sesión después de 1 minuto
                    ventana_principal.root2.after(
                        2 * 60 * 1000, lambda: cerrar_sesion(ventana_principal)
                    )
                else:
                    messagebox.showerror(
                        message="No se pudo obtener el nombre del rol.", title="Mensaje"
                    )
            else:
                messagebox.showerror(
                    message="Perdón pero esta Cuenta no existe.",
                    title="Mensaje",
                )
        else:
            messagebox.showerror(
                message="Clave única invalida no es Admin",
                title="Mensaje",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()

def cerrar_sesion(ventana_principal):
    messagebox.showinfo(message="Tu sesión ha expirado. Saliendo Ahora", title="Cerrando")
    ventana_principal.cerrar()
