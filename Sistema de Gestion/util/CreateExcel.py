import os
import pandas as pd
from sqlalchemy import create_engine
from openpyxl import load_workbook
import tkinter as tk
from tkinter import messagebox
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def mostrar_mensaje(titulo, mensaje):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo(titulo, mensaje)
    root.destroy()

def mostrar_error(titulo, mensaje):
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showerror(titulo, mensaje)
    root.destroy()

def obtener_datos_solicitud(numero_solicitud):
    try:
        # Crear el motor de base de datos SQLAlchemy
        engine = create_engine(
            "mysql+mysqlconnector://u0ioaiitne1nh02w:svvGffwj1FHbLpuwy3UL@bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com:3306/bimtfzdinglabpw1yzd0"
        )
        # Ejecutar la consulta SQL
        with engine.connect() as conn:
            consulta = f"""
            SELECT dc.Nombre, dc.Apellido, dc.Documento, dc.Cedula, dc.Telefono, dc.Direccion,
                   s.id_Solicitud, s.Fecha_Solicitud, s.Tipo_Solicitud, s.Descripcion, s.Garantia,
                   s.Precio, s.Estado, s.Fecha_Entrega,
                   p.Monto AS Abono, p.Fecha_Pago AS Fecha_Abono
            FROM datoscliente dc
            JOIN solicitudes s ON dc.Cedula = s.Cedula_Cliente
            LEFT JOIN pagos p ON s.id_Solicitud = p.id_Solicitud
            WHERE s.id_Solicitud = {numero_solicitud}
            ORDER BY p.Fecha_Pago ASC
            """
            datos = pd.read_sql(consulta, conn)
            return datos
    except Exception as e:
        mostrar_error("Error", f"Ocurrió un error: {e}")
        return None

def guardar_datos_en_excel(datos):
    try:
        # Cargar el archivo Excel existente
        archivo_excel = resource_path("util/Documento.xlsx")
        libro = load_workbook(archivo_excel, data_only=True)
        # Seleccionar la primera hoja (si solo hay una hoja)
        hoja = libro.active
        # Asignar los datos a posiciones específicas
        if not datos.empty:
            row = datos.iloc[0]
            hoja["C6"] = f"{row['Nombre']} {row['Apellido']}"
            hoja["C7"] = f"{row['Documento']} {row['Cedula']}"
            hoja["E6"] = row["Telefono"]
            hoja["E7"] = row["Direccion"]
            hoja["B10"] = row["id_Solicitud"]
            hoja["C10"] = row["Fecha_Solicitud"]
            hoja["D10"] = row["Tipo_Solicitud"]
            hoja["E10"] = row["Descripcion"]
            hoja["F10"] = row["Estado"]
            hoja["G10"] = row["Fecha_Entrega"]
            hoja["B12"] = f"{row['Garantia']} dias"
            hoja["C12"] = row["Precio"]
            # Escribir los pagos en las celdas correspondientes
            for i, pago in datos.iterrows():
                fila = 12 + i
                hoja[f"D{fila}"] = pago["Abono"]
                hoja[f"E{fila}"] = pago["Fecha_Abono"]
            # Guardar una copia del archivo Excel
            copia_archivo_excel = f"Solicitud N°{row['id_Solicitud']}.xlsx"
            if os.path.exists(copia_archivo_excel):
                os.remove(copia_archivo_excel)  # Eliminar el archivo existente
            libro.save(copia_archivo_excel)
            mostrar_mensaje(
                "Éxito", f"Archivo guardado exitosamente como {copia_archivo_excel}"
            )
        else:
            mostrar_error(
                "Error", "No se encontraron datos para la solicitud especificada."
            )
    except FileNotFoundError:
        mostrar_error("Error", f"El archivo {archivo_excel} no se encontró.")
    except Exception as e:
        mostrar_error("Error", f"Ocurrió un error: {e}")
