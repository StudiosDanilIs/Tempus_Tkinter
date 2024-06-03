import mysql.connector
from tkinter import *
from tkinter import messagebox


def RecuperarSesion(self, subventana):
    self.subventana = subventana

    db_config = {
        "host": "127.0.0.1",  # Cambia esto al host correcto
        "user": "root",
        "password": "210605",
        "database": "registro",
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    cedula = self.cedula_entry.get()
    nuevo_usuario = self.nuevo_usuario_entry.get()
    nueva_clave = self.nueva_clave_entry.get()

    # Validación de longitud mínima (por ejemplo, al menos 6 caracteres)
    if len(nuevo_usuario) < 6 or len(nueva_clave) < 6:
        messagebox.showerror("Error", "Debes ingresar valores mayores a 6 dígitos")
        return

    cursor.execute("SELECT Cedula FROM usuarios WHERE Cedula = %s", (cedula,))
    resultado_busqueda = cursor.fetchone()

    if resultado_busqueda:
        messagebox.showinfo(
            message="Datos identificados correctamente", title="Mensaje"
        )
        try:
            cursor.execute(
                "UPDATE usuarios SET Cuenta = %s, Clave = %s WHERE Cedula = %s",
                (nuevo_usuario, nueva_clave, cedula),
            )
            connection.commit()
            messagebox.showinfo(
                "Mensaje", "Excelente, datos actualizados correctamente"
            )
            self.subventana.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "No se pudieron actualizar los datos")
            print(f"Error al actualizar los datos: {e}")
    else:
        messagebox.showerror(
            message="Datos no encontrados. Verifica nuevamente", title="Mensaje"
        )

    connection.close()
