import mysql.connector
from tkinter import *
from tkinter import messagebox


def Agregar_Cliente(self):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
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

    # Obtener los datos del formulario
    name = self.nombre_entry.get()
    apellido = self.apellido_entry.get()
    documento = self.indicador_cedula_entry.get()
    cedula = self.cedula_entry.get()
    telefono = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c")

    if (
        len(name) < 3
        or len(apellido) < 3
        or len(cedula) < 7
        or len(telefono) < 10
        or len(direccion) < 10
    ):
        messagebox.showerror("Error", "Ingrese los Datos Completos")
        return

    # Verificar si ya existe un registro con la misma cédula o teléfono
    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s OR Telefono = %s",
            (cedula, telefono),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Si se encuentra un registro duplicado, mostrar un mensaje de error
            messagebox.showerror(
                message="Los Datos ya se Encuentran Registrados.",
                title="Error de Registro",
            )
        else:
            # Si no se encuentra ningún duplicado, registrar los datos
            cursor.execute(
                "INSERT INTO datoscliente (Nombre, Apellido, Documento, Cedula, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, apellido, documento, cedula, telefono, direccion),
            )
            connection.commit()
            messagebox.showinfo(message="Registro exitoso.", title="Registro")
            limpiar_campos(self)
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def Eliminar_Cliente(self):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
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

    # Obtener los datos del formulario
    cedula = self.cedula_entry.get()

    if len(cedula) < 7:
        messagebox.showerror("Error", "Cédula Incorrecta")
        return

    # Verificar si la cédula existe en la base de datos
    try:
        cursor.execute("SELECT * FROM datoscliente WHERE Cedula = %s", (cedula,))
        resultado = cursor.fetchone()

        if resultado:
            # Si se encuentra el registro, eliminarlo
            cursor.execute("DELETE FROM datoscliente WHERE Cedula = %s", (cedula,))
            connection.commit()
            messagebox.showinfo(
                message="Cliente eliminado exitosamente.", title="Eliminación"
            )
            limpiar_campos(self)
        else:
            # Si no se encuentra el registro, mostrar un mensaje de error
            messagebox.showerror(
                message="No se encontró un cliente con esa cédula.",
                title="Error de Eliminación",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def Buscar_Cliente(self):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
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

    # Obtener la cédula del formulario
    busqueda_cedula = self.buscar_cliente_entry.get()

    if len(busqueda_cedula) < 7:
        messagebox.showerror("Error", "Cédula Incorrecta")
        return

    # Buscar los datos del cliente en la base de datos
    try:
        cursor.execute(
            "SELECT Nombre, Apellido, Documento, Cedula, Telefono, Direccion FROM datoscliente WHERE Cedula = %s",
            (busqueda_cedula,),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Mostrar los datos en los campos de entrada
            self.nombre_entry.delete(0, END)
            self.nombre_entry.insert(0, resultado[0])
            self.apellido_entry.delete(0, END)
            self.apellido_entry.insert(0, resultado[1])
            self.indicador_cedula_entry.delete(0, END)
            self.indicador_cedula_entry.insert(0, resultado[2])
            self.cedula_entry.delete(0, END)
            self.cedula_entry.insert(0, resultado[3])
            self.telefono_entry.delete(0, END)
            self.telefono_entry.insert(0, resultado[4])
            self.direccion_text.delete("1.0", END)
            self.direccion_text.insert("1.0", resultado[5])

            self.buscar_cliente_entry.delete(0, END)
        else:
            messagebox.showerror(
                message="No se encontró un cliente con esa cédula.",
                title="Error de Búsqueda",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def Modificar_Cliente(self):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
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

    # Obtener los datos del formulario
    name = self.nombre_entry.get()
    apellido = self.apellido_entry.get()
    documento = self.indicador_cedula_entry.get()
    cedula = self.cedula_entry.get()
    telefono = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c")

    if len(cedula) < 8:
        messagebox.showerror("Error", "Cédula Incorrecta")
        return

    # Verificar si la cédula existe en la base de datos
    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s OR Documento = %s",
            (cedula, documento),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Actualizar los datos del cliente sin modificar la cédula y el documento
            cursor.execute(
                "UPDATE datoscliente SET Nombre = %s, Apellido = %s, Telefono = %s, Direccion = %s WHERE Cedula = %s AND Documento = %s",
                (name, apellido, telefono, direccion, cedula, documento)
            )
            connection.commit()
            messagebox.showinfo(message="Datos actualizados exitosamente.", title="Actualización")
            limpiar_campos(self)  # Limpiar los campos después de actualizar
        else:
            messagebox.showerror(
                message="No se encontró un cliente con esa cédula.",
                title="Error de Actualización",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def limpiar_campos(self):
    self.nombre_entry.delete(0, END)
    self.apellido_entry.delete(0, END)
    self.indicador_cedula_entry.delete(0, END)
    self.cedula_entry.delete(0, END)
    self.telefono_entry.delete(0, END)
    self.direccion_text.delete("1.0", END)
