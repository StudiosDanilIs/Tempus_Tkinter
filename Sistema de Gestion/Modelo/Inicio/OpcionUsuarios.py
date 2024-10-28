from tkinter import *
import mysql.connector
from tkinter import messagebox


# Permite Agregar un Cliente a la Base de Datos
def Agregar_Usuarios(self):
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    # Verificar la cantidad de usuarios de tipo empleado ya registrados
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id_RolUsuario = 3")
    numero_empleados = cursor.fetchone()[0]

    if numero_empleados >= 7:
        messagebox.showerror("Error", "No se pueden crear más de 7 cuentas de tipo empleado.")
        connection.close()
        return

    # Datos a Ingresar en la Base de Datos
    nombre = self.nombre_agregar.get().capitalize()
    cedula = self.cedula_agregar.get()
    usuario = self.usuario_agregar.get()
    clave = self.clave_agregar.get()

    # Verifica que los campos no estén vacíos
    if len(nombre) < 5 or len(cedula) < 7 or len(usuario) < 6 or len(clave) < 6:
        messagebox.showerror("Error", "Faltan Datos, Intenta de Nuevo")
        connection.close()
        return

    # Verifica si ya existe un Cliente con esos Mismos datos
    try:
        cursor.execute(
            "SELECT * FROM usuarios WHERE Cedula = %s OR Cuenta = %s OR Clave = %s",
            (cedula, usuario, clave),
        )
        resultado = cursor.fetchone()
        if resultado:
            # Si se encuentra un registro duplicado, mostrar un mensaje de error
            messagebox.showerror(
                message="Usuario ya Existente.", title="Error de Registro User"
            )
        else:
            # Si no se encuentra ningún duplicado, registra los datos
            cursor.execute(
                "INSERT INTO usuarios (id_RolUsuario, Cedula, Nombre, Cuenta, Clave) VALUES (%s, %s, %s, %s, %s)",
                (3, cedula, nombre, usuario, clave),
            )
            connection.commit()
            messagebox.showinfo(
                message="Usuario Guardado Exitosamente.", title="Registro"
            )
            limpiar_campos(self, "Agregar")  # Limpia los campos después de guardar el cliente
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()



# Permite Eliminar un Cliente de la Base de Datos
def Eliminar_Usuarios(self):
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    # Datos a Ingresar en la Base de Datos
    cedula = self.cedula_eliminar.get()

    # Verifica que los campos no estén vacíos
    if len(cedula) < 7:
        messagebox.showerror("Error", "Datos inválidos. Intente otra vez.")
        return

    # Verifica si la clave única ingresada coincide con la cuenta en la que se inició sesión
    try:
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

    elif opcion == "Eliminar":
        self.cedula_eliminar.delete(0, END)
