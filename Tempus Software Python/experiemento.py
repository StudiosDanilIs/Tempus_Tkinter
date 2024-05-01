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
        self.tempus_logo = PhotoImage(file="imagenes/tempus.png")
        self.after(100, lambda: self.iconphoto(False, self.tempus_logo))


        # Aquí puedes agregar más widgets a tu aplicación
        # ...
        
        
        
# Crear y ejecutar la aplicación
app = Tempus_Progrma()
app.mainloop()