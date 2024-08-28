import tkinter as tk
from tkinter import *
from tkinter import Frame
import util.CambioMenu as status
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from Visual.Inicio.Menu.Inicio import mostrar_opcion1
from Visual.Inicio.Menu.Solicitudes import mostrar_opcion2
from Visual.Inicio.Menu.Clientes import mostrar_opcion3
from Visual.Inicio.Menu.Pagos import mostrar_opcion4
from Visual.Inicio.Menu.Historial import mostrar_opcion5


class VentanaPrincipal:
    def __init__(self, nombre, nombre_rol, **kwargs):
        self.root2 = tk.Tk()
        self.root2.resizable(0, 0)
        self.root2.geometry("1100x635")
        self.root2.protocol("WM_DELETE_WINDOW", self.cerrar_sesion)
        self.presionado = False
        self.nombre_cuenta = nombre
        self.rol_programa = nombre_rol

        # Crear el frame del menú lateral
        self.menu_lateral = tk.Frame(self.root2, width=200)
        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.grid_rowconfigure(6, minsize=20)

        # Boton 1 Inicio del Sistema
        self.logo1 = utl.leer_imagen("menu/home.png", size=(44, 61))
        self.boton_opcion1 = self.crear_boton(
            image=self.logo1, command=lambda: mostrar_opcion1(self)
        )
        self.boton_opcion1.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion1.bind("<Enter>", lambda event: status.resaltar1(self, event))
        self.boton_opcion1.bind("<Leave>", lambda event: status.restaurar1(self, event))

        # Boton 2 Solicitudes
        self.logo2 = utl.leer_imagen("menu/solicitudes.png", size=(59, 61))
        self.boton_opcion2 = self.crear_boton(
            image=self.logo2, command=lambda: mostrar_opcion2(self)
        )
        self.boton_opcion2.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion2.bind("<Enter>", lambda event: status.resaltar2(self, event))
        self.boton_opcion2.bind("<Leave>", lambda event: status.restaurar2(self, event))

        # Boton 3 Clientes
        self.logo3 = utl.leer_imagen("menu/clientes.png", size=(44, 59))
        self.boton_opcion3 = self.crear_boton(
            image=self.logo3, command=lambda: mostrar_opcion3(self)
        )
        self.boton_opcion3.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion3.bind("<Enter>", lambda event: status.resaltar3(self, event))
        self.boton_opcion3.bind("<Leave>", lambda event: status.restaurar3(self, event))

        # Boton 4 Pagos
        self.logo4 = utl.leer_imagen("menu/pagos.png", size=(44, 64))
        self.boton_opcion4 = self.crear_boton(
            image=self.logo4, command=lambda: mostrar_opcion4(self)
        )
        self.boton_opcion4.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion4.bind("<Enter>", lambda event: status.resaltar4(self, event))
        self.boton_opcion4.bind("<Leave>", lambda event: status.restaurar4(self, event))

        # Boton 5 Historial
        self.logo5 = utl.leer_imagen("menu/historial.png", size=(44, 60))
        self.boton_opcion5 = self.crear_boton(
            image=self.logo5, command=lambda: mostrar_opcion5(self)
        )
        self.boton_opcion5.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion5.bind("<Enter>", lambda event: status.resaltar5(self, event))
        self.boton_opcion5.bind("<Leave>", lambda event: status.restaurar5(self, event))

        # Boton 6 Salir
        self.logo6 = utl.leer_imagen("menu/salir.png", size=(57, 59))
        self.boton_opcion6 = self.crear_boton(
            image=self.logo6, command=lambda: self.cerrar_sesion()
        )
        self.boton_opcion6.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion6.bind("<Enter>", lambda event: status.resaltar6(self, event))
        self.boton_opcion6.bind("<Leave>", lambda event: status.restaurar6(self, event))

        # Empaquetar los botones en el frame de opciones
        self.boton_opcion1.pack(fill="x")
        self.boton_opcion2.pack(fill="x")
        self.boton_opcion3.pack(fill="x")
        self.boton_opcion4.pack(fill="x")
        self.boton_opcion5.pack(fill="x")
        self.boton_opcion6.pack(fill="x")

        # Creación del Frame para las opciones
        self.label_info = tk.Frame(
            self.root2, bd=0, width=300, relief=tk.SOLID, padx=0, pady=0, bg="#f0f0f0"
        )
        self.label_info.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        # Mostramos la opción 1 por defecto
        mostrar_opcion1(self)

    #Funcion para crear botones
    def crear_boton(self, image=None, command=None, **kwargs):
        boton = tk.Button(
            self.menu_lateral,
            image=image,
            command=command,
            borderwidth=0,
            highlightthickness=2,
            bg="#1778FB",
            activebackground="#f0f0f0",
            height=102,
            width=150,
            **kwargs
        )
        return boton

    # Función para cerrar la ventana
    def cerrar_sesion(self):
        respuesta = messagebox.askokcancel(
            "Cerrar Programa", "¿Seguro, Quieres Salir del Programa?"
        )
        if respuesta:
            self.root2.destroy()

    # Función para limpiar el contenido del frame de opciones
    def limpiar_contenido(self):
        # Elimina cualquier widget o contenido previo
        for widget in self.label_info.winfo_children():
            widget.destroy()

    def cerrar(self):
        self.root2.destroy()

# Crear una instancia de la ventana principal
if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.root2.mainloop()
    VentanaPrincipal()
