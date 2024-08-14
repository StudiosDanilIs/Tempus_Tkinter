from tkinter import *
import mysql.connector
from tkinter import messagebox


# Permite Agregar un Cliente a la Base de Datos
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

    # Datos a Ingresar en la Base de Datos
    name = self.nombre_entry.get()
    apellido = self.apellido_entry.get()
    documento = self.tipo_cedula_entry.get()
    cedula = self.cedula_entry.get()
    telefono = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c")

    # Verifica que los campos no estén vacíos
    if (
        len(name) < 3
        or len(apellido) < 3
        or len(cedula) < 7
        or len(telefono) < 10
        or len(direccion) < 10
    ):
        messagebox.showerror("Error", "Datos Incorrectos")
        return

    # Verifica si ya existe un Cliente con esos Mismos datos
    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s OR Telefono = %s",
            (cedula, telefono),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Si se encuentra un registro duplicado, mostrar un mensaje de error
            messagebox.showerror(
                message="Datos ya Existentes.",
                title="Error de Registro",
            )
        else:
            # Si no se encuentra ningún duplicado, registra los datos
            cursor.execute(
                "INSERT INTO datoscliente (Nombre, Apellido, Documento, Cedula, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, apellido, documento, cedula, telefono, direccion),
            )
            connection.commit()
            messagebox.showinfo(
                message="Cliente Guardado Exitosamente.", title="Registro"
            )
            limpiar_campos(self)  # Limpia los campos después de guardar el cliente
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


# Permite Eliminar un Cliente de la Base de Datos
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

    # Datos a Ingresar en la Base de Datos
    cedula = self.cedula_entry.get()

    # Verifica que los campos no estén vacíos
    if len(cedula) < 7:
        messagebox.showerror("Error", "Documento Invalido Intente otra Vez")
        return

    # Verifica si ya existe un Cliente con esos Mismos datos para Eliminarlo
    try:
        cursor.execute("SELECT * FROM datoscliente WHERE Cedula = %s", (cedula,))
        resultado = cursor.fetchone()

        if resultado:
            # Si se encuentra el Cliente debe eliminarlo
            cursor.execute("DELETE FROM datoscliente WHERE Cedula = %s", (cedula,))
            connection.commit()
            messagebox.showinfo(
                message="Cliente Borrado Exitosamente.", title="Eliminación"
            )
            limpiar_campos(self)  # Limpia los campos después de eliminar el cliente
        else:
            # Si no se encuentra el Cliente mostrar un mensaje de error
            messagebox.showerror(
                message="No se encontró un Cliente con ese Documento.",
                title="Error de Eliminación",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


# Permite Buscar un Cliente en la Base de Datos
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

    # Datos a Ingresar en la Base de Datos
    busqueda_cedula = self.buscar_cliente_entry.get()

    # Verifica que los campos no estén vacíos
    if len(busqueda_cedula) < 7:
        messagebox.showerror("Error", "Documento Invalido Intente otra Vez")
        return

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


# Permite Modificar un Cliente en la Base de Datos
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

    # Datos a Ingresar en la Base de Datos
    name = self.nombre_entry.get()
    apellido = self.apellido_entry.get()
    documento = self.tipo_cedula_entry.get()
    cedula = self.cedula_entry.get()
    telefono = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c")

    # Verifica que los campos no estén vacíos
    if len(cedula) < 8:
        messagebox.showerror("Error", "Documento Invalido Intente otra Vez")
        return

    # Verifica si ya existe un Cliente con esos Mismos datos para Modificarlo
    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s OR Documento = %s",
            (cedula, documento),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Si se encuentra el Cliente debe Modificarlo
            cursor.execute(
                "UPDATE datoscliente SET Nombre = %s, Apellido = %s, Telefono = %s, Direccion = %s WHERE Cedula = %s AND Documento = %s",
                (name, apellido, telefono, direccion, cedula, documento),
            )
            connection.commit()
            messagebox.showinfo(
                message="Datos Actualizados Exitosamente.", title="Actualización"
            )
            limpiar_campos(self)  # Limpia los campos después de actualizar
        else:
            messagebox.showerror(
                message="No se encontró un cliente con ese Documento.",
                title="Error de Actualización",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def Obtener_Clientes(self):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="210605",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()

        # Obtener todos los registros
        cursor.execute("SELECT id_Cliente, Nombre, Apellido, Cedula, Telefono FROM datoscliente")
        resultados = cursor.fetchall()

        # Limpiar el Treeview antes de agregar nuevos datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Agregar los datos al Treeview
        for fila in resultados:
            self.tree.insert("", "end", values=fila)

    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error al obtener los clientes: {err}", title="Mensaje")
    finally:
        connection.close()


# Elimina los Datos en la Entrada de Texto de la Interfaz Gráfica
def limpiar_campos(self):
    self.nombre_entry.delete(0, END)
    self.apellido_entry.delete(0, END)
    self.tipo_cedula_entry.delete(0, END)
    self.cedula_entry.delete(0, END)
    self.telefono_entry.delete(0, END)
    self.direccion_text.delete("1.0", END)
