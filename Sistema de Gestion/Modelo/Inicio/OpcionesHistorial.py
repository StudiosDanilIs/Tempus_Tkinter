from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox


def Cargar_Solicitudes(self, opcion):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="210605",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()
                
        if opcion == "Pedido": 
            query = """
            SELECT s.id_Solicitud AS ID, s.Fecha_Solicitud AS Fecha, s.Tipo_Solicitud AS Tipo, 
            CONCAT(dc.Documento, dc.Cedula) AS Cedula, s.Descripcion, s.Precio, s.Estado, s.Garantia
            FROM solicitudes s
            INNER JOIN datoscliente dc ON s.Cedula_Cliente = dc.Cedula
            WHERE s.Tipo_Solicitud = 'Pedido'
            ORDER BY s.id_Solicitud DESC
            """
        elif opcion == "Venta": 
            query = """
            SELECT s.id_Solicitud AS ID, s.Fecha_Solicitud AS Fecha, s.Tipo_Solicitud AS Tipo, 
            CONCAT(dc.Documento, dc.Cedula) AS Cedula, s.Descripcion, s.Precio, s.Estado, s.Garantia
            FROM solicitudes s
            INNER JOIN datoscliente dc ON s.Cedula_Cliente = dc.Cedula
            WHERE s.Tipo_Solicitud = 'Venta'
            ORDER BY s.id_Solicitud DESC
            """
        elif opcion == "Reparacion": 
            query = """
            SELECT s.id_Solicitud AS ID, s.Fecha_Solicitud AS Fecha, s.Tipo_Solicitud AS Tipo, 
            CONCAT(dc.Documento, dc.Cedula) AS Cedula, s.Descripcion, s.Precio, s.Estado, s.Garantia
            FROM solicitudes s
            INNER JOIN datoscliente dc ON s.Cedula_Cliente = dc.Cedula
            WHERE s.Tipo_Solicitud = 'Reparacion'
            ORDER BY s.id_Solicitud DESC
            """
        cursor.execute(query)
        resultados = cursor.fetchall()

        # Limpiar el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        if resultados:
            for fila in resultados:
                precio_formateado = f"{fila[5]:,.0f} $"
                garantia_con_dias = f"{fila[7]} días"  # Agregar "días" al valor de Garantia
                fila = list(fila)
                fila[5] = precio_formateado
                fila[7] = garantia_con_dias
                self.tree.insert("", "end", values=fila)
        else:
            messagebox.showinfo(
                message="No hay solicitudes disponibles", title="Mensaje"
            )

    except mysql.connector.Error as err:
        messagebox.showerror(
            message=f"Error al obtener las Solicitudes: {err}", title="Mensaje"
        )
    finally:
        if "connection" in locals():
            connection.close()


# Permite Agregar un Cliente a la Base de Datos
def Solicitudes_Clientes(self):
    try:
        cedula_busqueda = self.cedula_buscar_entry.get()

        if len(cedula_busqueda) < 8:
            messagebox.showerror("Error", "Ingresa la cedula")
            return

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="210605",
            db="registro",
            port=3306,
        )
        cursor = connection.cursor()

        query = """
            SELECT s.id_Solicitud AS ID, s.Fecha_Solicitud AS Fecha, s.Tipo_Solicitud AS Tipo, s.Descripcion, s.Estado, s.Fecha_Entrega
            FROM solicitudes s
            INNER JOIN datoscliente dc ON s.Cedula_Cliente = dc.Cedula
            WHERE dc.Cedula = %s
            ORDER BY s.id_Solicitud DESC
        """
        cursor.execute(query, (cedula_busqueda,))
        resultados = cursor.fetchall()

        # Limpiar el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        if resultados:
            for fila in resultados:
                self.tree.insert("", "end", values=fila)
        else:
            messagebox.showerror(
                message="La Cedula no tiene Solicitudes", title="Mensaje"
            )

    except mysql.connector.Error as err:
        messagebox.showerror(
            message=f"Error al obtener las Solicitudes: {err}", title="Mensaje"
        )
    finally:
        if "connection" in locals():
            connection.close()


def Agregar_Fecha_Entrega(self):
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
    numero_orden = self.numero_orden_entry1.get()
    fecha_entrega = self.fecha_entrega_entry.get()

    # Verifica si ya existe un Cliente con esos Mismos datos para Modificarlo
    try:
        cursor.execute(
            "SELECT Fecha_Solicitud FROM solicitudes WHERE id_Solicitud = %s",
            (numero_orden,),
        )
        resultado = cursor.fetchone()

        if resultado:
            fecha_solicitud = resultado[0]
            try:
                # Convertir fecha_entrega a datetime.date
                fecha_entrega_dt = datetime.strptime(fecha_entrega, "%Y/%m/%d").date()

                if fecha_entrega_dt >= fecha_solicitud:
                    # Si se encuentra el Cliente debe Modificarlo
                    cursor.execute(
                        "UPDATE solicitudes SET Fecha_Entrega = %s, Estado = %s WHERE id_Solicitud = %s",
                        (fecha_entrega, "Entregado", numero_orden),
                    )
                    connection.commit()
                    messagebox.showinfo(
                        message="Fecha agregada exitosamente.", title="Actualización"
                    )
                    limpiar_campos(self)  # Limpia los campos después de actualizar
                else:
                    messagebox.showerror(
                        message="La fecha de entrega no puede ser menor a la fecha de solicitud.",
                        title="Error de Actualización",
                    )
            except ValueError as e:
                messagebox.showerror(
                    message=f"Formato de fecha incorrecto: {e}",
                    title="Error de Formato",
                )
        else:
            messagebox.showerror(
                message="El número de la solicitud no existe.",
                title="Error de Actualización",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def limpiar_campos(self):
    self.numero_orden_entry1.delete(0, END)
    self.numero_orden_entry2.delete(0, END)
    self.fecha_entrega_entry.delete(0, END)
