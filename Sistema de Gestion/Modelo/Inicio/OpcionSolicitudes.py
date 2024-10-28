from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox
from decimal import Decimal, InvalidOperation
from util.CreateExcel import obtener_datos_solicitud, guardar_datos_en_excel
from Visual.Inicio.VentanaCliente import VentanaEmergente


def Agregar_Solicitud(self):
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
    
    # Datos a ingresar en la base de datos
    cedula = self.cedula_agregar.get()
    descripcion = self.descripcion_agregar.get("1.0", "end-1c")
    precio = self.precio_agregar.get()
    garantia = self.garantia_agregar.get()
    fecha_solicitud = self.fecha_solicitud_agregar.get()
    abono = self.abono_entry.get()
    fecha_abono = self.fecha_abono_entry.get()
    tipo_solicitud = self.tipo_solicitud.get()
    aceptar = self.tipo_elegir.get()
    
    # Validación de ceros por delante en precio, garantía y abono
    if precio.startswith('0') or abono.startswith('0') or garantia.startswith('0'):
        messagebox.showerror("Error", "No se permiten ceros por delante en precio, garantía o abono.")
        return

    # Validación de abono y fecha de entrega
    if aceptar == "1":
        if not abono or float(abono) != float(precio):
            messagebox.showerror(
                "Error",
                "El abono debe ser igual al precio para registrar la fecha de entrega",
            )
            return
        else:
            fecha_entrega = self.fecha_entrega_entry.get()
            if not fecha_entrega or fecha_entrega < fecha_solicitud:
                messagebox.showerror(
                    "Error",
                    "La fecha de entrega no puede ser menor que la fecha de solicitud",
                )
                return
    else:
        fecha_entrega = None

    if len(cedula) < 6 or len(descripcion) < 20 or len(precio) < 4 or len(garantia) < 1:
        messagebox.showerror("Error", "Faltan datos, intenta nuevamente")
        return
    
    # Validaciones adicionales
    if abono and fecha_abono:
        if float(abono) > float(precio):
            messagebox.showerror("Error", "El abono no puede ser mayor que el precio")
            return
        if fecha_abono < fecha_solicitud:
            messagebox.showerror(
                "Error",
                "La fecha de abono no puede ser menor que la fecha de solicitud",
            )
            return
    
    try:
        # Verifica si la cédula ingresada pertenece a algún cliente registrado
        cursor.execute("SELECT * FROM datoscliente WHERE Cedula = %s", (cedula,))
        result = cursor.fetchone()
        if result is None:
            messagebox.showerror(
                "Error", "La cédula no corresponde a un cliente existente"
            )
            VentanaEmergente(self)
            return
        
        # Inserta la solicitud según el tipo
        estado_inicial = "En proceso"
        if aceptar == "1" and float(abono) == float(precio):
            estado_inicial = "Entregado"
        cursor.execute(
            "INSERT INTO solicitudes (Cedula_Cliente, Tipo_Solicitud, Fecha_Solicitud, Descripcion, Garantia, Precio, Fecha_Entrega, Estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (cedula, tipo_solicitud, fecha_solicitud, descripcion, garantia, precio, fecha_entrega, estado_inicial),
        )
        solicitud_id = cursor.lastrowid
        
        # Inserta el abono si se proporcionó
        if abono and fecha_abono:
            cursor.execute(
                "INSERT INTO pagos (id_Solicitud, Cedula_Cliente, Monto, Fecha_Pago) VALUES (%s, %s, %s, %s)",
                (solicitud_id, cedula, abono, fecha_abono),
            )
            if float(abono) == float(precio):
                estado_final = "Pagado"
                if aceptar == "1":
                    estado_final = "Entregado"
                cursor.execute(
                    "UPDATE solicitudes SET Estado = %s WHERE id_Solicitud = %s",
                    (estado_final, solicitud_id),
                )
        
        connection.commit()
        messagebox.showinfo(
            message=f"Solicitud registrada exitosamente. Número de solicitud: {solicitud_id}",
            title="Solicitud",
        )
        limpiar_campos(self)
        descargar_datos(self, solicitud_id)
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


# Permite buscar un pedido por el id
def Buscar_Solicitud(self):
    global id_encontrado
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

    id_solicitud = self.buscar_id_entry.get()
    # Verifica que los campos no estén vacíos
    if len(id_solicitud) < 1:
        messagebox.showerror("Error", "Faltan datos, intenta nuevamente")
        return

    try:
        cursor.execute(
            "SELECT Cedula_Cliente, Descripcion, Precio, Garantia, Fecha_Solicitud, Fecha_Entrega FROM solicitudes WHERE id_Solicitud = %s",
            (id_solicitud,),
        )
        resultado = cursor.fetchone()
        if resultado:
            # Muestra los datos del pedido en los campos correspondientes
            self.cedula_agregar.delete(0, END)
            self.cedula_agregar.insert(0, resultado[0])
            self.descripcion_agregar.delete("1.0", END)
            self.descripcion_agregar.insert("1.0", resultado[1])
            self.precio_agregar.delete(0, END)
            self.precio_agregar.insert(0, resultado[2])
            self.garantia_agregar.delete(0, END)
            self.garantia_agregar.insert(0, resultado[3])

            # Convierte la fecha a cadena de texto y actualiza el DateEntry
            if resultado[4]:
                fecha_solicitud = resultado[4].strftime("%Y/%m/%d")
                self.fecha_solicitud_agregar.set_date(fecha_solicitud)
            else:
                self.fecha_solicitud_agregar.set_date("")

            # Convierte la fecha de entrega a cadena de texto y actualiza el DateEntry
            if resultado[5]:
                fecha_entrega = resultado[5].strftime("%Y/%m/%d")
                self.fecha_entrega_entry.set_date(fecha_entrega)
            else:
                self.fecha_entrega_entry.set_date(None)  # Usa None en lugar de ""

            # Borra el contenido del campo de búsqueda
            self.buscar_id_entry.delete(0, END)
            id_encontrado = id_solicitud

            # Buscar abono y fecha de abono
            cursor.execute(
                "SELECT Monto, Fecha_Pago FROM pagos WHERE id_Solicitud = %s ORDER BY Fecha_Pago ASC LIMIT 1",
                (id_solicitud,),
            )
            pago_resultado = cursor.fetchone()
            if pago_resultado:
                self.abono_entry.delete(0, END)
                self.abono_entry.insert(0, pago_resultado[0])
                if pago_resultado[1]:
                    fecha_abono = pago_resultado[1].strftime("%Y/%m/%d")
                    self.fecha_abono_entry.set_date(fecha_abono)
                else:
                    self.fecha_abono_entry.set_date("")
            else:
                self.abono_entry.delete(0, END)
                self.fecha_abono_entry.set_date("")

            # Cambiar el estado a modificando
            self.modificando = True
            self.guardar_pedido_button.config(state="disabled")
            self.modificar_solicitud_button.config(state="normal")
        else:
            messagebox.showerror(
                message="Esa solicitud no existe, intenta otra vez",
                title="Error de Búsqueda",
            )
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


# Permite eliminar un pedido de la base de datos
def Eliminar_Solicitud(self):
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

    solicitud_numero = self.eliminar_solicitud_entry.get()

    try:
        cursor.execute(
            "SELECT COUNT(*) FROM solicitudes WHERE id_Solicitud = %s",
            (solicitud_numero,),
        )
        count = cursor.fetchone()[0]
        if count == 0:
            messagebox.showerror(
                message="Esa solicitud no existe, intenta otra vez",
                title="Error de Búsqueda",
            )
            return

        # Confirmación antes de eliminar
        confirmacion = messagebox.askyesno(
            title="Confirmación de eliminación",
            message="¿Estás seguro de que quieres eliminar esta solicitud y todos los pagos asociados?",
        )
        if not confirmacion:
            return

        # Eliminar pagos asociados
        cursor.execute("DELETE FROM pagos WHERE id_Solicitud = %s", (solicitud_numero,))

        # Eliminar la solicitud
        cursor.execute(
            "DELETE FROM solicitudes WHERE id_Solicitud = %s", (solicitud_numero,)
        )
        connection.commit()

        messagebox.showinfo(
            message="Solicitud y pagos asociados eliminados correctamente",
            title="Eliminación de solicitud",
        )
        self.eliminar_solicitud_entry.delete(0, END)

    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def Modificar_Solicitud(self):
    global id_encontrado
    # Verificar si id_encontrado está ingresado
    if not id_encontrado:
        messagebox.showerror(
            "Error", "No se ha seleccionado ninguna solicitud para modificar"
        )
        return

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

    # Datos a actualizar en la base de datos
    nueva_descripcion = self.descripcion_agregar.get("1.0", "end-1c")
    nuevo_precio = self.precio_agregar.get()
    nueva_garantia = self.garantia_agregar.get()
    nueva_fecha_solicitud = self.fecha_solicitud_agregar.get()
    # Datos de abono
    nuevo_abono = self.abono_entry.get()
    nueva_fecha_abono = self.fecha_abono_entry.get()
    # Datos de entrega
    nueva_fecha_entrega = self.fecha_entrega_entry.get()

    # Confirmación antes de modificar
    confirmacion = messagebox.askyesno(
        title="Confirmación de modificación",
        message="¿Estás seguro de que quieres modificar esta solicitud?",
    )
    if not confirmacion:
        return

    try:
        # Verifica si el pedido existe
        cursor.execute(
            "SELECT Precio, Fecha_Solicitud, Fecha_Entrega FROM solicitudes WHERE id_Solicitud = %s",
            (id_encontrado,),
        )
        solicitud_actual = cursor.fetchone()
        if solicitud_actual is None:
            messagebox.showerror(
                message="Esa solicitud no existe, ingresa otra",
                title="Error de Búsqueda",
            )
            return

        fecha_actual = solicitud_actual[1]
        # Validaciones adicionales
        if nueva_fecha_solicitud < fecha_actual.strftime("%Y-%m-%d"):
            messagebox.showerror(
                "Error",
                "La nueva fecha de solicitud no puede ser menor que la fecha actual",
            )
            return
        if nueva_fecha_entrega and nueva_fecha_entrega < nueva_fecha_solicitud:
            messagebox.showerror(
                "Error",
                "La fecha de entrega no puede ser menor que la fecha de solicitud",
            )
            return
        if nuevo_abono and float(nuevo_abono) > float(nuevo_precio):
            messagebox.showerror("Error", "El abono no puede ser mayor que el precio")
            return
        if nueva_fecha_abono and nueva_fecha_abono < nueva_fecha_solicitud:
            messagebox.showerror(
                "Error",
                "La fecha de abono no puede ser menor que la fecha de solicitud",
            )
            return

        # Si el pedido existe y las validaciones pasan, procede a actualizar los datos
        cursor.execute(
            "UPDATE solicitudes SET Descripcion = %s, Precio = %s, Garantia = %s, Fecha_Solicitud = %s, Fecha_Entrega = %s WHERE id_Solicitud = %s",
            (
                nueva_descripcion,
                nuevo_precio,
                nueva_garantia,
                nueva_fecha_solicitud,
                nueva_fecha_entrega if nueva_fecha_entrega else None,
                id_encontrado,
            ),
        )

        # Verifica si ya existe un abono para la solicitud
        cursor.execute(
            "SELECT id_Pago FROM pagos WHERE id_Solicitud = %s ORDER BY Fecha_Pago ASC LIMIT 1",
            (id_encontrado,),
        )
        pago_existente = cursor.fetchone()
        if nuevo_abono and nueva_fecha_abono:
            if pago_existente:
                # Actualiza el primer abono realizado
                cursor.execute(
                    "UPDATE pagos SET Monto = %s, Fecha_Pago = %s WHERE id_Pago = %s",
                    (nuevo_abono, nueva_fecha_abono, pago_existente[0]),
                )
            else:
                # Inserta un nuevo abono
                cursor.execute(
                    "INSERT INTO pagos (id_Solicitud, Cedula_Cliente, Monto, Fecha_Pago) VALUES (%s, %s, %s, %s)",
                    (
                        id_encontrado,
                        self.cedula_agregar.get(),
                        nuevo_abono,
                        nueva_fecha_abono,
                    ),
                )
            if float(nuevo_abono) == float(nuevo_precio):
                estado_final = "Pagado"
                if nueva_fecha_entrega:
                    estado_final = "Entregado"
                cursor.execute(
                    "UPDATE solicitudes SET Estado = %s WHERE id_Solicitud = %s",
                    (estado_final, id_encontrado),
                )

        connection.commit()
        messagebox.showinfo(
            message="Datos de la solicitud actualizados correctamente",
            title="Modificación de solicitud",
        )
        limpiar_campos(self)
        # Habilitar el botón de agregar y restablecer el estado
        self.guardar_pedido_button.config(state="normal")
        self.modificar_solicitud_button.config(state="disabled")
        self.modificando = False
    except mysql.connector.Error as err:
        messagebox.showerror(message=f"Error en la consulta: {err}", title="Mensaje")
    finally:
        connection.close()


def descargar_datos(self, solicitud_id):
    numero_solicitud = solicitud_id
    datos_solicitud = obtener_datos_solicitud(numero_solicitud)
    if datos_solicitud is not None:
        guardar_datos_en_excel(datos_solicitud)


def limpiar_campos(self):
    self.cedula_agregar.delete(0, END)
    self.descripcion_agregar.delete(1.0, END)
    self.precio_agregar.delete(0, END)
    self.garantia_agregar.delete(0, END)
    self.fecha_solicitud_agregar.delete(0, END)
    self.abono_entry.delete(0, END)
    self.fecha_abono_entry.delete(0, END)
    self.fecha_entrega_entry.delete(0, END)
