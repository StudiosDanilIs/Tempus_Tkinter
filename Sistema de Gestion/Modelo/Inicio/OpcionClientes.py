from tkinter import *
import mysql.connector
from tkinter import messagebox

# Permite Agregar un Cliente a la Base de Datos
def Agregar_Cliente(self):
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
    name = self.nombre_entry.get().capitalize()
    apellido = self.apellido_entry.get().capitalize()
    documento = self.tipo_cedula_entry.get().capitalize()
    cedula_agregar = self.cedula_entry.get().lstrip('0')  # Remover ceros al principio
    telefono_agregar = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c").capitalize()

    # Validar cédula
    if not cedula_agregar.isdigit() or int(cedula_agregar) < 1000 or cedula_agregar != self.cedula_entry.get():
        messagebox.showerror(
            "Error", "Documento inválido ya que el ingresado no debe tener ceros por delante."
        )
        return

    # Validar teléfono
    if not telefono_agregar.isdigit() or telefono_agregar.count('0') > 1 or len(telefono_agregar) < 10:
        messagebox.showerror(
            "Error", "Número de teléfono inválido. Debe contener solo un cero y al menos 10 dígitos."
        )
        return

    # Verificar que los campos no estén vacíos
    if (
        len(name) < 3
        or len(apellido) < 3
        or len(cedula_agregar) < 5
        or len(telefono_agregar) < 10
        or len(direccion) < 10
    ):
        messagebox.showerror("Error", "Datos Incorrectos")
        return

    # Verificar si ya existe un Cliente con esos mismos datos
    try:
        cursor.execute(
            "SELECT * FROM datoscliente WHERE Cedula = %s OR Telefono = %s",
            (cedula_agregar, telefono_agregar),
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
                (name, apellido, documento, cedula_agregar, telefono_agregar, direccion),
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



# Permite Buscar un Cliente en la Base de Datos
def Buscar_Cliente(self):
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
            
            self.modificando = True
            self.guardar_clientes_button.config(state="disabled")
            self.modificar_clientes_button.config(state="normal")
            
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
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor(buffered=True)
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    # Datos a Ingresar en la Base de Datos
    name = self.nombre_entry.get().capitalize()
    apellido = self.apellido_entry.get().capitalize()
    documento = self.tipo_cedula_entry.get().capitalize()
    cedula = self.cedula_entry.get()
    telefono = self.telefono_entry.get()
    direccion = self.direccion_text.get("1.0", "end-1c").capitalize()

    # Verifica que los campos no estén vacíos
    if len(cedula) < 8:
        messagebox.showerror("Error", "Documento Invalido, Intente otra Vez")
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
            self.guardar_clientes_button.config(state="normal")
            self.modificar_clientes_button.config(state="disabled")
            self.modificando = False
        else:
            messagebox.showerror(
                message="No se encontró un cliente con ese Documento.",
                title="Error de Actualización",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()



def Obtener_Clientes(self, cargar_datos=False):
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor()

        if cargar_datos:
            # Limpiar el Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Obtener los datos y agregarlos al Treeview
            cursor.execute(
                "SELECT id_Cliente, Nombre, Apellido, Cedula, Telefono "
                "FROM datoscliente "
                "ORDER BY id_Cliente DESC "
                "LIMIT 75"
            )
            resultados = cursor.fetchall()

            for fila in resultados:
                self.tree.insert("", "end", values=fila)

    except mysql.connector.Error as err:
        # Manejar errores
        messagebox.showerror(
            message=f"Error al obtener los clientes: {err}", title="Mensaje"
        )
    finally:
        # Cerrar la conexión
        try:
            connection.close()
        except NameError:
            pass


# Elimina los Datos en la Entrada de Texto de la Interfaz Gráfica
def limpiar_campos(self):
    self.nombre_entry.delete(0, END)
    self.apellido_entry.delete(0, END)
    self.tipo_cedula_entry.delete(0, END)
    self.cedula_entry.delete(0, END)
    self.telefono_entry.delete(0, END)
    self.direccion_text.delete("1.0", END)
