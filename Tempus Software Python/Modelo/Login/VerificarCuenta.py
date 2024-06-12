import mysql.connector
from tkinter import *
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal


# verificar la conexion a la base de datos y verificar si el usuario y la contraseña son correctos
def verificar_sesion(self):
    # conexion a la base de datos
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="210605",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()
    # mensaje de error si no se puede conectar a la base de datos
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )
    # instancia de la clase VentanaPrincipal si el usuario y la contraseña son correctos
    usuario = self.username_entry.get()
    password = self.password_entry.get()

    # consulta a la base de datos para verificar si el usuario y la contraseña son correctos
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE Cuenta = %s AND Clave = %s",
            (usuario, password),
        )
        resultado = cursor.fetchone()
        # si el usuario y la contraseña son correctos, se muestra un mensaje de bienvenida y se abre la ventana principal
        if resultado:
            # Obtener el ID del rol del usuario
            id_rol = resultado[1]  # Ajusta según tu estructura de datos

            # Consultar la tabla de roles para obtener el nombre del rol
            cursor.execute("SELECT NombreRol FROM rolusuario WHERE id_RolUsuario = %s", (id_rol,))
            nombre_rol = cursor.fetchone()[0]  # Obtener el primer resultado (nombre del rol)

            # Mostrar el nivel de permisos en un mensaje de bienvenida
            messagebox.showinfo(message=f"Bienvenido {nombre_rol} a Tempus Software", title="Mensaje")
            self.root.destroy()
            VentanaPrincipal(nombre_rol)
        # si el usuario y la contraseña son incorrectos, se muestra un mensaje de error
        else:
            messagebox.showerror(message="Los Datos son Inválidos", title="Mensaje")
    # mensaje de error si no se puede ejecutar la consulta
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()
