import mysql.connector
from tkinter import messagebox

def guardar_clientes(self, subventana):
    self.subventana = subventana
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="210605",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()

        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        cedula = self.cedula_entry.get()
        telefono = self.telefono_entry.get()

        if len(nombre) < 6 or len(apellido) < 6 or len(cedula) < 8 or len(telefono) < 11:
            messagebox.showerror(
                "Error", "Verifica los Datos Ingresados al Menos uno esta Incorrecto"
            )
            return

        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s AND Telefono = %s",
            (cedula, telefono),
        )
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showerror(
                message="Lo Siento ya Está Registrado ese Cliente", title="Mensaje"
            )
        else:
            cursor.execute(
                "INSERT INTO datoscliente (Nombre, Apellido, Cedula, Telefono) VALUES (%s, %s, %s, %s)",
                (nombre, apellido, cedula, telefono),
            )
            connection.commit()
            messagebox.showinfo(
                "Mensaje", "Excelente, Cliente Registrado correctamente"
            )
            self.subventana.destroy()

    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error: {err}", title="Mensaje")
    finally:
        connection.close()
