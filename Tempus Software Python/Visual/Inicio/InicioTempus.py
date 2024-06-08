from PIL import ImageTk, Image as imim
import tkinter as tk
from tkinter import *


class VentanaPrincipal:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.title("Inicio - Tempus Software")
        self.root2.geometry("1200x700")
        self.root2.resizable(0, 0)
        
        
        self.lgn_frame = Frame(self.root2, bg="#E6F0F3")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)


        self.sign_in_image = imim.open("images\\logotipo.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg="#E6F0F3", anchor="center")
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)      
        


        # Menú principal
        self.menu_tempus = tk.Menu(self.root2, tearoff=0)
        self.root2.config(menu=self.menu_tempus)

        # Menú de solicitud
        self.opcion_solicitud = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(
            label="Crear Solicitud", menu=self.opcion_solicitud
        )
        opciones = [
            "Solicitud de Pedido",
            "Solicitud de Venta",
            "Solicitud de Reparación",
        ]
        for opcion in opciones:
            self.opcion_solicitud.add_command(label=opcion)

        # Menú de clientes
        self.opcion_clientes = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Clientes", menu=self.opcion_clientes)
        opciones_clientes = ["Agregar Clientes", "Ver Clientes"]
        for opcion_cliente in opciones_clientes:
            self.opcion_clientes.add_command(label=opcion_cliente)

        # Menú de Historial
        self.opcion_historial = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Historial", menu=self.opcion_historial)
        opciones_historial = ["Ver Pedidos", "Ver Ventas", "Ver Reparaciones"]
        for opcion_historial in opciones_historial:
            self.opcion_historial.add_command(label=opcion_historial)

        # Menú de Herramientas
        self.opcion_herramienta = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Herramientas", menu=self.opcion_herramienta)
        opciones_herramienta = ["Ver Perfil", "Salir Sistema"]
        for opcion_herramienta in opciones_herramienta:
            self.opcion_herramienta.add_command(label=opcion_herramienta)
            

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.root2.mainloop()
