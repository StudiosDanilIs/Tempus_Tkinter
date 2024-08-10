from tkinter import *
import mysql.connector
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal


# Verifica los datos para iniciar sesión en el programa
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

    # Verificar si la cuenta y la contraseña son correctas
    try:
        cursor.execute(
            "SELECT Nombre, id_RolUsuario FROM usuarios WHERE Cuenta = %s AND Clave = %s",
            (usuario, password),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Se obtiene el nombre del usuario y el id del rol
            nombre = resultado[0]  # El nombre está en la primera columna
            id_rol = resultado[1]  # El id del rol está en la segunda columna

            # Consultar la tabla de roles para obtener el nombre del rol
            cursor.execute(
                "SELECT NombreRol FROM rolusuario WHERE id_RolUsuario = %s", (id_rol,)
            )
            nombre_rol = cursor.fetchone()[
                0
            ]  # Obtener el nombre del rol desde la consulta

            # Muestra un mensaje de bienvenida y da acceso a la ventana principal
            messagebox.showinfo(
                message=f"Bienvenido {nombre} a Tempus Software", title="Mensaje"
            )
            self.root.destroy()  # Cierra la ventana de inicio de sesión
            VentanaPrincipal(
                nombre, nombre_rol
            )  # Abre la ventana principal con el nombre del usuario y el rol
        else:
            messagebox.showerror(
                message="La Cuenta no se Encuentra Registrada.", title="Mensaje"
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()
