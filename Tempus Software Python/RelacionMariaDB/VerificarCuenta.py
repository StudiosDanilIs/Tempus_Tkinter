import mysql.connector
from tkinter import *
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal

# Define db_config si aún no lo has hecho
db_config = {
    "host": "localhost",
    "user": "root",
    "passwd": "",
    "db": "registro",
    "port": 3306,
}

def conectar_base_de_datos():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.Error as err:
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
            "SELECT * FROM usuarios WHERE Cuenta = %s AND Clave = %s",
            (usuario, password),
        )
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo(message="Bienvenido a Tempus Software", title="Mensaje")
            VentanaPrincipal()
            self.root.destroy()
        else:
            messagebox.showerror(message="Los Datos son Inválidos", title="Mensaje")
    except mysql.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()
