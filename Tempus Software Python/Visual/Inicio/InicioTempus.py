from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl
from tkinter import Frame
import tkinter.messagebox as messagebox
import util.CambioMenu as status

from Visual.Inicio.Menu.Inicio import mostrar_opcion1
from Visual.Inicio.Menu.Solicitudes import mostrar_opcion2
from Visual.Inicio.Menu.Clientes import mostrar_opcion3
from Visual.Inicio.Menu.Pagos import mostrar_opcion4
from Visual.Inicio.Menu.Historial import mostrar_opcion5

class VentanaPrincipal:
    def __init__(self, nombre_rol, **kwargs):
        self.root2 = tk.Tk()
        self.root2.geometry("1100x635")
        self.root2.resizable(0, 0)
        self.root2.protocol("WM_DELETE_WINDOW", self.cerrar_sesion)
        self.rol_programa = nombre_rol
        self.presionado = False

        # Crear el frame del menú lateral
        self.menu_lateral = tk.Frame(self.root2, bg="gray", width=200)
        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.grid_rowconfigure(6, minsize=20)
        
        
        # Crear botones para las opciones
        self.logo1 = utl.leer_imagen(utl.resource_path("imagenes/menu/home.png"), size=(44, 61))
        self.logo_inicial = utl.leer_imagen(utl.resource_path("imagenes/menu/home2.png"), size=(44, 61))
        self.boton_opcion1 = self.crear_boton(image=self.logo1, command=lambda: mostrar_opcion1(self))
        self.boton_opcion1.place(relx=0.5, rely=0.36, anchor=tk.CENTER)  
        self.boton_opcion1.bind("<Button>", lambda event: status.resaltar1(self, event))
        self.boton_opcion1.config(bg='#FFFFFF', image=self.logo_inicial)
        
        self.logo2 = utl.leer_imagen(utl.resource_path("imagenes/menu/solicitudes.png"), size=(59, 61))
        self.boton_opcion2 = self.crear_boton(image=self.logo2, command=lambda: mostrar_opcion2(self))
        self.boton_opcion2.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion2.bind("<Button>", lambda event: status.resaltar2(self, event))

        self.logo3 = utl.leer_imagen(utl.resource_path("imagenes/menu/clientes.png"), size=(44, 59))
        self.boton_opcion3 = self.crear_boton(image=self.logo3, command=lambda: mostrar_opcion3(self))
        self.boton_opcion3.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion3.bind("<Button>", lambda event: status.resaltar3(self, event))

        self.logo4 = utl.leer_imagen(utl.resource_path("imagenes/menu/pagos.png"), size=(44, 64))
        self.boton_opcion4 = self.crear_boton(image=self.logo4, command=lambda: mostrar_opcion4(self))
        self.boton_opcion4.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion4.bind("<Button>", lambda event: status.resaltar4(self, event))

        self.logo5 = utl.leer_imagen(utl.resource_path("imagenes/menu/historial.png"), size=(44, 60))
        self.boton_opcion5 = self.crear_boton(image=self.logo5, command=lambda: mostrar_opcion5(self))
        self.boton_opcion5.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion5.bind("<Button>", lambda event: status.resaltar5(self, event))

        self.logo6 = utl.leer_imagen(utl.resource_path("imagenes/menu/salir.png"), size=(57, 59))
        self.boton_opcion6 = self.crear_boton(image=self.logo6, command=lambda: self.mostrar_opcion6())
        self.boton_opcion6.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion6.bind("<Button>", lambda event: status.resaltar6(self, event))

        # Empaquetar los botones
        self.boton_opcion1.pack(fill="x")
        self.boton_opcion2.pack(fill="x")
        self.boton_opcion3.pack(fill="x")
        self.boton_opcion4.pack(fill="x")
        self.boton_opcion5.pack(fill="x")
        self.boton_opcion6.pack(fill="x")

        # Crear el frame para el contenido principal                
        self.label_info = tk.Frame(self.root2, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#FFFFFF')
        self.label_info.pack(side="left",expand=tk.YES,fill=tk.BOTH)

        mostrar_opcion1(self)
    

    def crear_boton(self, image=None, command=None, **kwargs):
        boton = tk.Button(self.menu_lateral, image=image, command=command,
                        borderwidth=0, highlightthickness=2, bg="#1778FB",
                        activebackground="#FFFFFF", height=102, width=150,
                        **kwargs)  # Pass remaining arguments using **kwargs
        return boton


    def mostrar_opcion6(self):
        self.cerrar_sesion()



    # Función para cerrar la ventana
    def cerrar_sesion(self):
        respuesta = messagebox.askokcancel(
            "Cerrar Programa", "¿Desea Salir del Sistema?"
        )
        if respuesta:
            self.root2.destroy()

    def limpiar_contenido(self):
        # Elimina cualquier widget o contenido previo
        for widget in self.label_info.winfo_children():
            widget.destroy()
            
    # Función para cerrar la ventana
    def Close_Windows(self):
        if messagebox.askokcancel("Close", "¿Desea Cerrar la Aplicación?"):
            self.root2.destroy()               

# Crear una instancia de la ventana principal
if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.root2.mainloop()
    VentanaPrincipal()