from tkinter import *
import mysql.connector
from tkinter import messagebox


# Permite Agregar un Cliente a la Base de Datos
def Agregar_Usuarios(self):
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
    nombre = self.nombre_agregar.get().capitalize()
    cedula = self.cedula_agregar.get()
    usuario = self.usuario_agregar.get()
    clave = self.clave_agregar.get()
    unica = self.clave_unica.get()

    # Verifica que los campos no estén vacíos
    if (
        len(nombre) < 5
        or len(cedula) < 7
        or len(usuario) < 6
        or len(clave) < 6
        or len(unica) != 6
    ):
        messagebox.showerror("Error", "Faltan Datos, Intenta de Nuevo")
        return

    # Verifica si ya existe un Cliente con esos Mismos datos
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE Cedula = %s OR Cuenta = %s OR Clave_Unica = %s",
            (cedula, usuario, unica),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Si se encuentra un registro duplicado, mostrar un mensaje de error
            messagebox.showerror(
                message="Usuario ya Existente.",
                title="Error de Registro User",
            )
        else:
            # Si no se encuentra ningún duplicado, registra los datos
            cursor.execute(
                "INSERT INTO usuarios (id_RolUsuario, Cedula, Nombre, Cuenta, Clave, Clave_unica) VALUES (%s, %s, %s, %s, %s, %s)",
                (3, cedula, nombre, usuario, clave, unica),
            )
            connection.commit()
            messagebox.showinfo(
                message="Usuario Guardado Exitosamente.", title="Registro"
            )
            limpiar_campos(
                self, "Agregar"
            )  # Limpia los campos después de guardar el cliente
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def Modificar_Usuarios(self):
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
    usuario = self.usuario_modificar.get()
    clave = self.clave_modificar.get()
    nuevo_usuario = self.nuevo_usuario_modificar.get()
    nueva_clave = self.nueva_clave_modificar.get()
    unica = self.clave_unica.get()

    # Verifica que los campos no estén vacíos
    if (
        len(usuario) < 6
        or len(clave) < 6
        or len(nuevo_usuario) < 6
        or len(nueva_clave) < 6
        or len(unica) != 6
    ):
        messagebox.showerror("Error", "Faltan Datos, Intenta de Nuevo")
        return

    # Verifica si la clave única pertenece a la cuenta y la clave ingresadas
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE Cuenta = %s AND Clave = %s AND Clave_Unica = %s AND Nombre = %s",
            (usuario, clave, unica, self.nombre_cuenta),
        )
        resultado = cursor.fetchone()

        if resultado:
            # Verifica que los nuevos datos sean diferentes a los actuales
            if nuevo_usuario == resultado[0] and nueva_clave == resultado[2]:
                messagebox.showerror(
                    "Error", "Los nuevos datos no pueden ser iguales a los actuales"
                )
                return

            # Verifica si los nuevos datos ya están registrados en otra cuenta
            cursor.execute(
                "SELECT * FROM usuarios WHERE (Cuenta = %s OR Clave = %s) AND Clave_Unica != %s",
                (nuevo_usuario, nueva_clave, unica),
            )
            resultado_nuevo = cursor.fetchone()

            if resultado_nuevo:
                messagebox.showerror(
                    "Error", "Los nuevos datos ya están registrados en otra cuenta"
                )
                return

            # Si se encuentra la cuenta y los datos son diferentes, permite la modificación
            cursor.execute(
                "UPDATE usuarios SET Cuenta = %s, Clave = %s WHERE Cuenta = %s AND Clave_Unica = %s",
                (nuevo_usuario, nueva_clave, usuario, unica),
            )
            connection.commit()
            messagebox.showinfo(
                message="Datos Actualizados. Saliendo Programa...",
                title="Actualización",
            )
            self.root2.destroy()
        else:
            messagebox.showerror(
                message="Lo Siento no eres el Propietario de la Cuenta.",
                title="Error de Actualización",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


# Permite Eliminar un Cliente de la Base de Datos
def Eliminar_Usuarios(self):
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
    cedula = self.cedula_eliminar.get()
    unica = self.clave_unica.get()

    # Verifica que los campos no estén vacíos
    if len(cedula) < 7 or len(unica) != 6:
        messagebox.showerror("Error", "Datos inválidos. Intente otra vez.")
        return

    # Verifica si la clave única ingresada coincide con la cuenta en la que se inició sesión
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE Nombre = %s AND Clave_Unica = %s",
            (self.nombre_cuenta, unica),
        )
        resultado = cursor.fetchone()

        if not resultado:
            messagebox.showerror("Error", "Clave única incorrecta.")
            return

        # Verifica si ya existe un Cliente con esos Mismos datos para Eliminarlo
        cursor.execute("SELECT * FROM usuarios WHERE Cedula = %s", (cedula,))
        resultado = cursor.fetchone()

        if resultado:
            # Verifica que la cuenta a eliminar no sea la cuenta en la que se inició sesión
            if (
                resultado[3] == self.nombre_cuenta
            ):  # Asumiendo que el nombre de la cuenta está en la segunda columna
                messagebox.showerror("Error", "No puedes eliminar tu propia cuenta.")
                return

            # Si se encuentra el Cliente debe eliminarlo
            cursor.execute("DELETE FROM usuarios WHERE Cedula = %s", (cedula,))
            connection.commit()
            messagebox.showinfo(
                message="Cliente Borrado Exitosamente.", title="Eliminación"
            )
            limpiar_campos(
                self, "Eliminar"
            )  # Limpia los campos después de eliminar el cliente
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


# Elimina los Datos en la Entrada de Texto de la Interfaz Gráfica
def limpiar_campos(self, opcion):
    if opcion == "Agregar":
        self.nombre_agregar.delete(0, END)
        self.cedula_agregar.delete(0, END)
        self.usuario_agregar.delete(0, END)
        self.clave_agregar.delete(0, END)
        self.clave_unica.delete(0, END)

    elif opcion == "Eliminar":
        self.cedula_eliminar.delete(0, END)
        self.clave_unica.delete(0, END)
