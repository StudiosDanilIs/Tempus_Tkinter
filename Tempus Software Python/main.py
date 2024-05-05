# Incorporacion de Librerias y Demas
import customtkinter
from customtkinter import CTk,CTkEntry
from tkinter import PhotoImage


# Configurar la ventana
customtkinter.set_appearance_mode("system")
customtkinter.deactivate_automatic_dpi_awareness()



class Tempus_Progrma(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configurar la ventana
        self.geometry("800x600")
        self.title("Tempus Software")
        # Cargar y establecer el logo de la ventana
        self.ruta_icono = "imagenes/tempus.ico"
        self.iconbitmap(self.ruta_icono)


        # Aquí puedes agregar más widgets a tu aplicación
        # ...
        
        

# Crear y ejecutar la aplicación
app = Tempus_Progrma()
app.mainloop()