from tkinter import *
import mysql.connector
from tkinter import messagebox


# Permite Agregar un Cliente a la Base de Datos
def Buscar_Solicitudes(self):
    try:
        connection = mysql.connector.connect(
            host="localhost",
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
    busqueda_cedula = self.cedula_buscar_entry.get()

    # Buscar los datos del cliente en la base de datos
    try:
        cursor.execute(
            "SELECT Nombre, Apellido, Documento, Cedula, Telefono, Direccion FROM datoscliente WHERE Cedula = %s",
            (busqueda_cedula,),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Muestra los datos del cliente en los campos correspondientes
            self.nombre_entry.delete(0, END)
            self.nombre_entry.insert(0, resultado[0])
            self.apellido_entry.delete(0, END)
            self.apellido_entry.insert(0, resultado[1])
            self.tipo_cedula_entry.delete(0, END)
            self.tipo_cedula_entry.insert(0, resultado[2])
            self.cedula_entry.delete(0, END)
            self.cedula_entry.insert(0, resultado[3])
            self.telefono_entry.delete(0, END)
            self.telefono_entry.insert(0, resultado[4])
            self.direccion_text.delete("1.0", END)
            self.direccion_text.insert("1.0", resultado[5])

            # Borra el contenido del campo de búsqueda
            self.buscar_cliente_entry.delete(0, END)
        else:
            messagebox.showerror(
                message="No se encontró un cliente con ese Documento.",
                title="Error de Búsqueda",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()    