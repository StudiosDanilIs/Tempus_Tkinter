from tkinter import *
import mysql.connector
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal


# Verifica los datos para iniciar sesión en el programa
def verificar_sesion(self):
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
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
            nombre_rol_result = cursor.fetchone()

            if nombre_rol_result:
                nombre_rol = nombre_rol_result[0]

                # Verificar si el rol es "System"
                if nombre_rol == "SistemLoad":
                    # Mostrar un mensaje de error y no permitir el inicio de sesión
                    messagebox.showerror(
                        message="Lo Siento pero esta Cuenta no tiene Permiso", title="Error"
                    )
                else:
                    # Muestra un mensaje de bienvenida para otros roles
                    messagebox.showinfo(
                        message=f"Bienvenido {nombre} a Tempus Software", title="Mensaje"
                    )
                    self.root.destroy()  # Cierra la ventana de inicio de sesión
                    ventana_principal = VentanaPrincipal(nombre, nombre_rol)
                    # Establecer un temporizador para cerrar la sesión después de 15 minutos
                    ventana_principal.root2.after(
                        18 * 60 * 1000, lambda: cerrar_sesion(ventana_principal)
                    )
            else:
                messagebox.showerror(
                    message="No se pudo obtener el nombre del rol.", title="Mensaje"
                )
        else:
            messagebox.showerror(
                message="La Cuenta no se Encuentra Registrada.", title="Mensaje"
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()

def cerrar_sesion(ventana_principal):
    messagebox.showinfo(message="Tu sesión ha expirado. Saliendo Ahora", title="Cerrando")
    ventana_principal.cerrar()
