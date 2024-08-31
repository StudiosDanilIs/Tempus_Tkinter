import mysql.connector
from tkinter import *
from tkinter import messagebox


def ModificarUsuarios(self, root2):
    self.root2 = root2
    try:
        connection = mysql.connector.connect(
            host="bwgmj3osiuz7xl3trcvk-mysql.services.clever-cloud.com",
            user="usgdjhacbrtwcr8d",
            passwd="ytoPadfaz6Y4CZ6AwTnn",
            db="bwgmj3osiuz7xl3trcvk",
            port=3306,
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    cedula = self.cedula_agregar.get()
    nuevo_usuario = self.nuevo_usuario_agregar.get()
    nueva_clave = self.nueva_clave_agregar.get()

    if len(nuevo_usuario) < 6 or len(nueva_clave) < 6:
        messagebox.showerror("Error", "Datos muy cortos, No Validos")
        return

    cursor.execute("SELECT Cedula FROM usuarios WHERE Cedula = %s", (cedula,))
    resultado_busqueda = cursor.fetchone()

    # Verificar si se encontró la cédula
    if resultado_busqueda:
        messagebox.showinfo(
            message="Cédula identificada correctamente", title="Mensaje"
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
            self.root2.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "No se pudieron actualizar los datos")
            print(f"Error al actualizar los datos: {e}")

    else:
        messagebox.showerror(
            message="Cédula no encontrada. Verifica nuevamente", title="Mensaje"
        )

    connection.close()
