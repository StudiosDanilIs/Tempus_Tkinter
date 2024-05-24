# Incorporación de Librerias y Demas (y las librerias extras como ttk y messagebox)
from tkinter import messagebox, ttk
import customtkinter
from customtkinter import CTk
import tkinter as tk
from tkinter import PhotoImage


# Configurar la ventana
customtkinter.set_appearance_mode("system")
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_default_color_theme("blue")


class Tempus_Progrma(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x580")
        self.title("Tempus Software")

        # Cargar y establecer el logo de la ventana
        self.ruta_icono = "imagenes\logotipo.ico"
        try:
            self.icon = PhotoImage(file=self.ruta_icono)
            self.tk.call('wm', 'iconphoto', self._w, self.icon)
        except tk.TclError:
            print("Error: No se pudo cargar el icono")

        # el menu es esto
        self.menu_vertical = tk.Menu(self, tearoff=0)
        self.config(menu=self.menu_vertical)

        # Opción de pedido "tecnicamente"
        self.opcion_solicitud = tk.Menu(self.menu_vertical, tearoff=0)
        self.menu_vertical.add_cascade(label="Crear Solicitud", menu=self.opcion_solicitud)
        self.opcion_solicitud.add_command(label="Solicitud de Venta", command=self.crear_solicitud_venta)

        # Opción de Clientes del menu chafo
        self.opcion_clientes = tk.Menu(self.menu_vertical, tearoff=0)
        self.menu_vertical.add_cascade(label="Clientes", menu=self.opcion_clientes)
        self.opcion_clientes.add_command(label="Ver Clientes", command=self.ver_clientes)
        self.clientes = []  # Lista Que me dio solo a mi errores XD

    def crear_solicitud_venta(self):
        def mostrar_descripcion_precio(event):
            tipo_seleccionado = tipo_venta.get()
            if tipo_seleccionado == "Revision de equipo":
                label_descripcion.config(text="Descripción del Daño y observaciones:")
                label_precio.config(text="Precio de la reparacion del daño:")
            elif tipo_seleccionado == "Pedido":
                label_descripcion.config(text="Descripción del Poducto del pedido:")
                label_precio.config(text="Precio de el pedido:")
            elif tipo_seleccionado == "Venta de Equipo":
                label_descripcion.config(text="Descripción de la Venta de Equipo:")
                label_precio.config(text="Precio de la Venta de Equipo:")

        # no es tan complejo jejeh
        ventana_solicitud_venta = tk.Toplevel(self)
        ventana_solicitud_venta.title("Solicitud de Venta")

        # todos estos son los cuadros de texto y la funcion de cada uno No tiene ciencia
        label_nombre = tk.Label(ventana_solicitud_venta, text="Nombre del Cliente:")
        label_nombre.grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(ventana_solicitud_venta)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        label_identificacion = tk.Label(ventana_solicitud_venta, text="Número de Cedula:")
        label_identificacion.grid(row=1, column=0, padx=10, pady=10)
        entry_identificacion = tk.Entry(ventana_solicitud_venta)
        entry_identificacion.grid(row=1, column=1, padx=10, pady=10)

        label_telefono = tk.Label(ventana_solicitud_venta, text="Número Telefónico:")
        label_telefono.grid(row=2, column=0, padx=10, pady=10)
        entry_telefono = tk.Entry(ventana_solicitud_venta)
        entry_telefono.grid(row=2, column=1, padx=10, pady=10)

        label_fecha = tk.Label(ventana_solicitud_venta, text="Fecha de la Solicitud:")
        label_fecha.grid(row=3, column=0, padx=10, pady=10)
        entry_fecha = tk.Entry(ventana_solicitud_venta)
        entry_fecha.grid(row=3, column=1, padx=10, pady=10)

        # estas son las opciones
        label_tipo_venta = tk.Label(ventana_solicitud_venta, text="Tipo de Venta:")
        label_tipo_venta.grid(row=4, column=0, padx=10, pady=10)
        tipo_venta = tk.StringVar()
        opciones_tipo_venta = ["Revision de equipo", "Pedido", "Venta de Equipo"]
        combo_tipo_venta = ttk.Combobox(ventana_solicitud_venta, textvariable=tipo_venta, values=opciones_tipo_venta)
        combo_tipo_venta.grid(row=4, column=1, padx=10, pady=10)
        
        combo_tipo_venta.bind("<<ComboboxSelected>>", mostrar_descripcion_precio)

        # descripciónes y precios son inventados por el usuario en este caso
        label_descripcion = tk.Label(ventana_solicitud_venta, text="Descripción:")
        label_descripcion.grid(row=5, column=0, padx=10, pady=10)
        entry_descripcion = tk.Entry(ventana_solicitud_venta)
        entry_descripcion.grid(row=5, column=1, padx=10, pady=10)

        label_precio = tk.Label(ventana_solicitud_venta, text="Precio:")
        label_precio.grid(row=6, column=0, padx=10, pady=10)
        entry_precio = tk.Entry(ventana_solicitud_venta)
        entry_precio.grid(row=6, column=1, padx=10, pady=10)

        def guardar_solicitud_venta():
            tipo_seleccionado = tipo_venta.get()
            descripcion = entry_descripcion.get()
            precio = entry_precio.get()
            nombre = entry_nombre.get()
            identificacion = entry_identificacion.get()
            telefono = entry_telefono.get()
            fecha = entry_fecha.get()
            
            # me concentre en tratar de darle esa funcion de "registrar un dato" Pero este es el ejemplo
            cliente = {
                "nombre": nombre,
                "identificacion": identificacion,
                "telefono": telefono,
                "fecha": fecha,
                "tipo_venta": tipo_seleccionado,
                "descripcion": descripcion,
                "precio": precio
            }
            
            # Agrega al cliente... solo hace eso
            self.clientes.append(cliente)
            
            # Este mensaje me dio "un error en la linea 3958" aunque no me acuerdo si ese era el numero
            messagebox.showinfo("Solicitud de Venta", "Solicitud de Venta guardada con éxito")

        boton_guardar = tk.Button(ventana_solicitud_venta, text="Guardar", command=guardar_solicitud_venta)
        boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def ver_clientes(self):
        def mostrar_informacion_cliente():
            selected_client = tree.focus()
            if selected_client:
                client_data = tree.item(selected_client)["values"]
                nombre = client_data[0]
                identificacion = client_data[1]
                telefono = client_data[2]
                fecha = client_data[3]
                tipo_venta = client_data[4]
                descripcion = client_data[5]
                precio = client_data[6]
                
                # esta parte es de la opcion del menu del cliente
                ventana_cliente = tk.Toplevel(self)
                ventana_cliente.title(f"Información de {nombre}")
                
                label_nombre = tk.Label(ventana_cliente, text=f"Nombre: {nombre}")
                label_nombre.grid(row=0, column=0, padx=10, pady=10)
                
                label_identificacion = tk.Label(ventana_cliente, text=f"Número de Identificación: {identificacion}")
                label_identificacion.grid(row=1, column=0, padx=10, pady=10)
                
                label_telefono = tk.Label(ventana_cliente, text=f"Número Telefónico: {telefono}")
                label_telefono.grid(row=2, column=0, padx=10, pady=10)
                
                label_fecha = tk.Label(ventana_cliente, text=f"Fecha: {fecha}")
                label_fecha.grid(row=3, column=0, padx=10, pady=10)
                
                label_tipo_venta = tk.Label(ventana_cliente, text=f"Tipo de Venta: {tipo_venta}")
                label_tipo_venta.grid(row=4, column=0, padx=10, pady=10)
                
                label_descripcion = tk.Label(ventana_cliente, text=f"Descripción: {descripcion}")
                label_descripcion.grid(row=5, column=0, padx=10, pady=10)
                
                label_precio = tk.Label(ventana_cliente, text=f"Precio: {precio}")
                label_precio.grid(row=6, column=0, padx=10, pady=10)

        ventana_clientes = tk.Toplevel(self)
        ventana_clientes.title("Lista de Clientes")
        
        # estas son las que almacenan los datos de los clientes "lo tome prestado"
        tree = ttk.Treeview(ventana_clientes)
        tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        tree.column("#0", width=100)
        tree.column("1", width=100)
        tree.column("2", width=100)
        tree.column("3", width=100)
        tree.column("4", width=100)
        tree.column("5", width=100)
        tree.column("6", width=100)
        tree.column("7", width=100)
        tree.heading("#0", text="ID")
        tree.heading("1", text="Nombre")
        tree.heading("2", text="Identificación")
        tree.heading("3", text="Teléfono")
        tree.heading("4", text="Fecha")
        tree.heading("5", text="Tipo de Venta")
        tree.heading("6", text="Descripción")
        tree.heading("7", text="Precio")
        tree.pack(fill="both", expand=True)
        
        # Agrega los datos "guardados" a las filas
        for i, cliente in enumerate(self.clientes):
            tree.insert("", "end", text=str(i+1), values=(
                cliente["nombre"],
                cliente["identificacion"],
                cliente["telefono"],
                cliente["fecha"],
                cliente["tipo_venta"],
                cliente["descripcion"],
                cliente["precio"]
            ))
        
        # este es un evento para mostrar la información del cliente al hacer doble clic "robado jeje"
        tree.bind("<Double-1>", lambda event: mostrar_informacion_cliente())

# Crear y ejecutar la aplicación
app = Tempus_Progrma()
app.mainloop()
# recalco que investigue varias paginas y foros donde me guie y admito haber copiado y pegado algunas cosas mas
# sonara cochino pero una inteligencia artificial acomodo muchas cosas que quedaban feas o innecesarias