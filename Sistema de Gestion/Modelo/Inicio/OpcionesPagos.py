from decimal import Decimal, InvalidOperation
from datetime import datetime
from tkinter import messagebox, END
import mysql.connector
from util.CreateExcel import obtener_datos_solicitud, guardar_datos_en_excel


def Cargar_Pagos(self):
    global cedula_cliente
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        buscar_pagos = self.buscar_pagos_entry.get()
        # Verificar si el campo de entrada está vacío
        if not buscar_pagos:
            messagebox.showerror("Error", "Por favor, ingrese el número de solicitud.")
            return
        cursor = connection.cursor()
        # Verificar si el número de solicitud existe
        cursor.execute(
            "SELECT COUNT(*) FROM solicitudes WHERE id_Solicitud = %s", (buscar_pagos,)
        )
        solicitud_existe = cursor.fetchone()[0]
        if not solicitud_existe:
            messagebox.showerror("Error", "Número de solicitud inexistente.")
            return
        query = """
        SELECT dc.Nombre AS Nombre, dc.Cedula AS Documento, s.Precio AS Precio,
               p.Monto AS Abono, p.Fecha_Pago AS Fecha, s.Estado AS Estado
        FROM pagos p
        INNER JOIN datoscliente dc ON p.Cedula_Cliente = dc.Cedula
        INNER JOIN solicitudes s ON p.id_Solicitud = s.id_Solicitud
        WHERE s.id_Solicitud = %s
        ORDER BY p.id_Pago DESC
        """
        cursor.execute(query, (buscar_pagos,))
        resultados = cursor.fetchall()
        # Limpiar el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        if resultados:
            total_abonado = 0
            precio_producto = resultados[0][2]  # Precio del producto
            for fila in resultados:
                total_abonado += fila[3]
                abono_formateado = f"{fila[3]:,.0f} $"
                precio_formateado = f"{fila[2]:,.0f} $"
                fila = list(fila)
                fila[3] = abono_formateado
                fila[2] = precio_formateado
                self.tree.insert("", "end", values=fila)
            # Almacenar la cédula del primer resultado
            cedula_cliente = resultados[0][1]

            # Calcular monto restante a pagar
            monto_restante = precio_producto - total_abonado
            precio_formateado = f"{precio_producto:,.0f} $"
            monto_restante_formateado = f"{monto_restante:,.0f} $"

            # Actualizar labels
            self.label_precio_total.config(text=f"Precio total:\n{precio_formateado}")
            self.label_monto_restante.config(
                text=f"Monto restante:\n{monto_restante_formateado}"
            )
        else:
            messagebox.showinfo(
                message="No hay pagos disponibles para esta solicitud", title="Mensaje"
            )
    except mysql.connector.Error as err:
        messagebox.showerror(
            message=f"Error al obtener los pagos: {err}", title="Mensaje"
        )
    finally:
        if "connection" in locals():
            connection.close()


def Agregar_Pago(self):
    global cedula_cliente
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor()
        # Obtener los datos del nuevo pago
        id_solicitud = self.buscar_pagos_entry.get()
        nuevo_pago_str = self.pago_entry.get()
        fecha_pago = self.fecha_pago_entry.get()
        aceptar = self.tipo_elegir.get()
        fecha_entrega = self.fecha_entrega_entry.get() if aceptar == "1" else None

        # Verificar si el campo de entrada está vacío
        if not id_solicitud or not nuevo_pago_str or not fecha_pago:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Intentar convertir el nuevo pago a Decimal y validar que sea mayor que 999
        try:
            nuevo_pago = Decimal(nuevo_pago_str)
            if nuevo_pago < 1000:
                raise InvalidOperation
        except InvalidOperation:
            messagebox.showerror(
                "Error", "Monto de pago inválido. Debe ser mayor a 4 Dígitos."
            )
            return

        # Obtener la cédula del cliente
        cursor.execute(
            "SELECT Cedula FROM datoscliente WHERE Cedula = %s", (cedula_cliente,)
        )
        cedula_existe = cursor.fetchone()
        if not cedula_existe:
            messagebox.showerror("Error", "Cédula del cliente no existe.")
            return

        # Obtener la fecha de solicitud y el precio
        cursor.execute(
            "SELECT Fecha_Solicitud, Precio, Estado FROM solicitudes WHERE id_Solicitud = %s",
            (id_solicitud,),
        )
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", "Número de solicitud inexistente.")
            return
        fecha_solicitud, precio_solicitud, estado_solicitud = resultado

        # Convertir las fechas a objetos datetime para la comparación
        try:
            fecha_pago_dt = datetime.strptime(fecha_pago, "%Y/%m/%d").date()
        except ValueError:
            messagebox.showerror(
                "Error", "Formato de fecha incorrecto. Use 'YYYY/MM/DD'."
            )
            return
        if fecha_pago_dt < fecha_solicitud:
            messagebox.showerror(
                "Error",
                "La fecha de pago no puede ser menor que la fecha de solicitud.",
            )
            return

        # Obtener la suma de los pagos existentes para la solicitud
        cursor.execute(
            "SELECT SUM(Monto) FROM pagos WHERE id_Solicitud = %s", (id_solicitud,)
        )
        suma_pagos = cursor.fetchone()[0] or Decimal(0)

        # Calcular el monto total después del nuevo pago
        monto_total = suma_pagos + nuevo_pago
        if monto_total > precio_solicitud:
            messagebox.showerror(
                "Error",
                f"El pago excede el monto restante de {precio_solicitud - suma_pagos:.0f} $.",
            )
            return

        # Insertar el nuevo pago
        cursor.execute(
            "INSERT INTO pagos (id_Solicitud, Cedula_Cliente, Monto, Fecha_Pago) VALUES (%s, %s, %s, %s)",
            (id_solicitud, cedula_cliente, nuevo_pago, fecha_pago),
        )
        connection.commit()

        # Actualizar el estado de la solicitud si el monto total de los pagos alcanza el precio de la solicitud
        if monto_total >= precio_solicitud:
            cursor.execute(
                "UPDATE solicitudes SET Estado = 'Pagado' WHERE id_Solicitud = %s",
                (id_solicitud,),
            )
            connection.commit()
            if aceptar == "1":
                try:
                    fecha_entrega_dt = datetime.strptime(
                        fecha_entrega, "%Y/%m/%d"
                    ).date()
                except ValueError:
                    messagebox.showerror(
                        "Error",
                        "Formato de fecha incorrecto para la fecha de entrega. Use 'YYYY/MM/DD'.",
                    )
                    return
                if fecha_entrega_dt < fecha_solicitud:
                    messagebox.showerror(
                        "Error",
                        "La fecha de entrega no puede ser menor que la fecha de solicitud.",
                    )
                    return
                cursor.execute(
                    "UPDATE solicitudes SET Fecha_Entrega = %s, Estado = 'Entregado' WHERE id_Solicitud = %s",
                    (fecha_entrega, id_solicitud),
                )
                connection.commit()
            messagebox.showinfo(
                "Éxito",
                "El pago se ha registrado y la solicitud está completamente pagada.",
            )
            descargar_datos(self, id_solicitud)
        else:
            messagebox.showinfo("Éxito", "El pago se ha registrado.")

        # Limpiar los campos de entrada
        limpiar_campos(self)
    except mysql.connector.Error as err:
        messagebox.showerror(
            message=f"Error al registrar el pago: {err}", title="Mensaje"
        )
    finally:
        if "connection" in locals():
            connection.close()


def descargar_datos(self, id_solicitud):
    numero_solicitud = id_solicitud
    datos_solicitud = obtener_datos_solicitud(numero_solicitud)
    if datos_solicitud is not None:
        guardar_datos_en_excel(datos_solicitud)


def limpiar_campos(self):
    self.pago_entry.delete(0, END)
    self.fecha_pago_entry.delete(0, END)
    self.fecha_entrega_entry.delete(0, END)
