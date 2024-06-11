import mysql.connector
from tkinter import *
from tkinter import messagebox


def guardar_clientes(self):
    # conexion a la base de datos
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="Tempus09",
            passwd="TNQ[C8Zm2tE-qOq_",
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
    nombre = self.nombre_entry.get()
    apellido = self.apellido_entry.get()
    cedula = self.cedula_entry.get()
    telefono = self.telefono_entry.get()

    if len(nombre) < 6 or len(apellido) < 6 or len(cedula) < 8 or len(telefono) < 11:
        messagebox.showerror(
            "Error", "Verifica los Datos Ingresados al Menos uno esta Incorrecto"
        )
        return

    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s AND Telefono = %s",
            (cedula, telefono),
        )
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showerror(
                message="Lo Siento ya Esta Registrado ese Cliente", title="Mensaje"
            )

        else:
            try:
                cursor.execute(
                    f"INSERT INTO datoscliente VALUES ({nombre},{apellido},{cedula},{telefono})"
                )
                connection.commit()
                messagebox.showinfo(
                    "Mensaje", "Excelente, Cliente Registrado correctamente"
                )
            except mysql.connector.Error as e:
                messagebox.showerror("Error", "No se pudo Registrar los datos")
                print(f"Error al Registrar los datos: {e}")

    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()
