import mysql.connector
from tkinter import *
from tkinter import messagebox


# Conexión a la base de datos
def RecuperarSesion(self, subventana):
    self.subventana = subventana
    # conexión a la base de datos
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="Tempus09",
            passwd="TNQ[C8Zm2tE-qOq_",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()
    # Manejo de excepciones para la conexión a la base de datos
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    # instanciamos los objetos de la ventana
    cedula = self.cedula_entry.get()
    nuevo_usuario = self.nuevo_usuario_entry.get()
    nueva_clave = self.nueva_clave_entry.get()

    # Validación de longitud mínima (por ejemplo, al menos 6 caracteres)
    if len(nuevo_usuario) < 6 or len(nueva_clave) < 6 or len(cedula) < 8:
        messagebox.showerror("Error", "Datos No Aceptados Intente Nuevamente")
        return

    # cedula encorada en la base de datos
    cursor.execute("SELECT Cedula FROM usuarios WHERE Cedula = %s", (cedula,))
    resultado_busqueda = cursor.fetchone()

    # Verificar si se encontró la cédula
    if resultado_busqueda:
        messagebox.showinfo(
            message="Datos identificados correctamente", title="Mensaje"
        )
        # Actualizar los datos en la base de datos
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
        # Si ocurre un error al actualizar los datos, mostrar un mensaje de error
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "No se pudieron actualizar los datos")
            print(f"Error al actualizar los datos: {e}")

    # Si no se encontró la cédula, mostrar un mensaje de error
    else:
        messagebox.showerror(
            message="Datos no encontrados. Verifica nuevamente", title="Mensaje"
        )

    connection.close()
