import tkinter as tk
from tkinter import PhotoImage
from tkinter import Label, Frame


class VentanaPrincipal:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.title("Inicio - Tempus Software")
        self.root2.geometry("1200x700")
        self.root2.resizable(0, 0)

        self.menu_tempus = tk.Menu(self.root2, tearoff=0)
        self.root2.config(menu=self.menu_tempus)

        self.opcion_solicitud = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Crear Solicitud", menu=self.opcion_solicitud)
        self.opcion_solicitud.add_command(label="Solicitud de Venta", command=self.crear_solicitud_venta)

        self.opcion_clientes = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Clientes", menu=self.opcion_clientes)
        self.opcion_clientes.add_command(label="Ver Clientes", command=self.ver_clientes)



    def crear_solicitud_venta(self):
        pass

    def ver_clientes(self):
        pass
    
    
    
    
    
    
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.root2.mainloop()
