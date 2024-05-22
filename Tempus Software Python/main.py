# Incorporación de Librerias y Demas
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
        # Configurar la ventana
        self.geometry("1100x580")
        self.title("Tempus Software")
        # Cargar y establecer el logo de la ventana
        self.ruta_icono = "imagenes/logotipo.ico"
    # Integre esta seccion luego de ver que no se ejecutaba correctamente, me dio muchos errores y con esto se solucionan
        try:
            self.icon = PhotoImage(file=self.ruta_icono)
            self.tk.call('wm', 'iconphoto', self._w, self.icon)
        except tk.TclError:
            print("Error: No se pudo cargar el icono")

        # Aquí puedes agregar más widgets a tu aplicación
        # ...
        
# Crear y ejecutar la aplicación
app = Tempus_Progrma()
app.mainloop()