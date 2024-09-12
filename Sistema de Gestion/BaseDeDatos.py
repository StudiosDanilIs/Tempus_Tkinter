import mysql.connector
import tkinter as tk
from tkinter import ttk

# Configura los detalles de tu base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "210605",
    "database": "registro"
}

# Función para conectar a la base de datos y ejecutar una consulta
def ejecutar_consulta(consulta, valores):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(consulta, valores)
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return resultados
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Historial de Solicitudes")

# Crear un campo de entrada para la cédula
cedula_var = tk.StringVar()
cedula_entry = tk.Entry(ventana, textvariable=cedula_var)
cedula_entry.pack()

# Crear un botón para buscar
buscar_btn = tk.Button(ventana, text="Buscar", command=lambda: buscar_solicitudes())
buscar_btn.pack()

# Crear un Treeview para mostrar los resultados
treeview = ttk.Treeview(ventana, columns=("Tipo", "Fecha", "Descripción", "Precio", "Cliente", "Cédula"), show='headings')
treeview.heading("Tipo", text="Tipo")
treeview.heading("Fecha", text="Fecha")
treeview.heading("Descripción", text="Descripción")
treeview.heading("Precio", text="Precio")
treeview.heading("Cliente", text="Cliente")
treeview.heading("Cédula", text="Cédula")

# Ajustar el ancho de cada columna (ajusta los valores según tus necesidades)
treeview.column("Tipo", width=80, anchor="center")
treeview.column("Fecha", width=100, anchor="center")
treeview.column("Descripción", width=250, anchor="w")
treeview.column("Precio", width=80, anchor="center")
treeview.column("Cliente", width=150, anchor="w")
treeview.column("Cédula", width=100, anchor="center")

treeview.pack()

# Función para buscar las solicitudes
def buscar_solicitudes():
    cedula = cedula_var.get()
    consulta = """
    SELECT s.Tipo_Solicitud AS Tipo, s.Fecha_Solicitud AS Fecha, s.Descripcion, s.Precio, 
           CONCAT(dc.Nombre, ' ', dc.Apellido) AS Cliente, dc.Cedula
    FROM solicitudes s
    INNER JOIN datoscliente dc ON s.Cedula_Cliente = dc.Cedula
    WHERE dc.Cedula = %s
    ORDER BY s.Fecha_Solicitud DESC
    """
    valores = (cedula,)
    resultados = ejecutar_consulta(consulta, valores)

    # Limpiar el Treeview antes de agregar nuevos datos
    for i in treeview.get_children():
        treeview.delete(i)

    if resultados:
        for row in resultados:
            treeview.insert("", tk.END, values=row)
    else:
        print("No se encontraron solicitudes para el cliente:", cedula)

ventana.mainloop()
