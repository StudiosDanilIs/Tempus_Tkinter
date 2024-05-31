import mysql.connector
from tkinter import *
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal


def conectar_base_de_datos():
    db_config = {
        "host": "127.0.0.1",  # Cambia esto al host correcto
        "user": "root",
        "password": "210605",
        "database": "registro",
    }

    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error de conexión: {err}", title="Mensaje")
        return None


def verificar_sesion(self, root):
    self.root = root
    connection = conectar_base_de_datos()

    if not connection:
        return

    cursor = connection.cursor()

    usuario = self.username_entry.get()
    password = self.password_entry.get()

    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = %s AND Clave = %s",
            (usuario, password),
        )
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo(message="Bienvenido a Tempus Software", title="Mensaje")
            self.root.destroy()
            VentanaPrincipal()
        else:
            messagebox.showerror(message="Los Datos son Inválidos", title="Mensaje")
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


# Llama a verificar_sesion desde donde sea necesario
