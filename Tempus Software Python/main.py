# Incorporacion de Librerias y Demas
import customtkinter
import tkinter
from customtkinter import CTk,CTkEntry
from tkinter import PhotoImage


# Configurar la ventana
customtkinter.set_appearance_mode("system")
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_default_color_theme("blue")



class Tempus_Progrma(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configurar la ventana
        self.geometry(f"{1100}x{580}")
        self.title("Tempus Software")
        # Cargar y establecer el logo de la ventana
        self.ruta_icono = "imagenes/logotipo.ico"
        self.iconbitmap(self.ruta_icono)


        # Aquí puedes agregar más widgets a tu aplicación
        # ...
        
        

# Crear y ejecutar la aplicación
app = Tempus_Progrma()
app.mainloop()