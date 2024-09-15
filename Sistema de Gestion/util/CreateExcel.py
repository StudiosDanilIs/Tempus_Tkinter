import pandas as pd
from sqlalchemy import create_engine
from openpyxl import load_workbook
import tkinter as tk
from tkinter import messagebox

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
        engine = create_engine('mysql+mysqlconnector://root:210605@localhost:3306/registro')

        # Ejecutar la consulta SQL
        with engine.connect() as conn:
            consulta = f"""
            SELECT dc.Nombre, dc.Apellido, dc.Documento, dc.Cedula, dc.Telefono, dc.Direccion,
                   s.id_Solicitud, s.Fecha_Solicitud, s.Tipo_Solicitud, s.Descripcion, s.Garantia,
                   s.Precio, s.Estado, s.Fecha_Entrega
            FROM datoscliente dc
            JOIN solicitudes s ON dc.Cedula = s.Cedula_Cliente
            WHERE s.id_Solicitud = {numero_solicitud}
            """
            datos = pd.read_sql(consulta, conn)
            return datos

    except Exception as e:
        mostrar_error("Error", f"Ocurrió un error: {e}")
        return None

    except Exception as e:
        mostrar_error("Error", f"Ocurrió un error: {e}")
        return None

def guardar_datos_en_excel(datos):
    try:
        # Cargar el archivo Excel existente
        archivo_excel = "util/Documento.xlsx"
        libro = load_workbook(archivo_excel, data_only=True)

        # Seleccionar la primera hoja (si solo hay una hoja)
        hoja = libro.active

        # Asignar los datos a posiciones específicas
        if not datos.empty:
            row = datos.iloc[0]
            hoja['C6'] = f"{row['Nombre']} {row['Apellido']}"
            hoja['C7'] = f"{row['Documento']} {row['Cedula']}"
            hoja['E6'] = row['Telefono']
            hoja['E7'] = row['Direccion']
            hoja['B9'] = row['id_Solicitud']
            hoja['C9'] = row['Fecha_Solicitud']
            hoja['D9'] = row['Tipo_Solicitud']
            hoja['E9'] = row['Descripcion']
            hoja['F9'] = f"{row['Garantia']} dias"
            hoja['G9'] = row['Precio']
            hoja['B11'] = row['Estado']
            hoja['C11'] = row['Fecha_Entrega']

            # Guardar una copia del archivo Excel
            copia_archivo_excel = f"Solicitud N°{row['id_Solicitud']}.xlsx"
            libro.save(copia_archivo_excel)
            mostrar_mensaje("Éxito", f"Archivo guardado exitosamente como {copia_archivo_excel}")
        else:
            mostrar_error("Error", "No se encontraron datos para la solicitud especificada.")

    except FileNotFoundError:
        mostrar_error("Error", f"El archivo {archivo_excel} no se encontró.")

    except Exception as e:
        mostrar_error("Error", f"Ocurrió un error: {e}")
