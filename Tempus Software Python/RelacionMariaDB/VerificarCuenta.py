import mysql.connector
from tkinter import *
from tkinter import messagebox
from Visual.Inicio.InicioTempus import VentanaPrincipal


def verificar_sesion(self, root):
    self.root = root
    
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1", user="Tempus09", passwd="/Du1s8wFpIqSwsKh", db="registro", port=3306
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(message=f"Error de conexión: {err}", title="Mensaje")


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
