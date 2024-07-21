from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl
import tkinter as tk
from tkinter import Frame
import tkinter.messagebox as messagebox
import Funciones.CambioMenu as status

class VentanaPrincipal:
    def __init__(self, nombre_rol, **kwargs):
        self.root2 = tk.Tk()
        self.root2.title("Inicio - Tempus Software")
        self.root2.geometry("1100x635")
        self.root2.resizable(0, 0)
        self.rol_programa = nombre_rol
        self.presionado = False

        # Crear el frame del menú lateral
        self.menu_lateral = tk.Frame(self.root2, bg="gray", width=200)
        self.menu_lateral.pack(side="left", fill="y")
        self.menu_lateral.grid_rowconfigure(6, minsize=20)

        # Crear botones para las opciones
        self.logo1 = utl.leer_imagen(utl.resource_path("imagenes/usuario.png"), size=(41, 45))
        self.boton_opcion1 = self.crear_boton("Inicio", self.mostrar_opcion1, image=self.logo1)
        self.boton_opcion1.image = self.logo1
        self.boton_opcion1.place(relx=0.5, rely=0.36, anchor=tk.CENTER)  
        self.boton_opcion1.bind("<Enter>", lambda event: status.resaltar1(self, event))
        self.boton_opcion1.bind("<Leave>", lambda event: status.restaurar1(self, event))      
        
        self.logo2 = utl.leer_imagen(
            utl.resource_path("imagenes/solicitudes.png"), size=(59, 61)
        )
        self.boton_opcion2 = self.crear_boton("Solicitudes", self.mostrar_opcion2, image=self.logo2)
        self.boton_opcion2.image = self.logo2
        self.boton_opcion2.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion2.bind("<Enter>", lambda event: status.resaltar2(self, event))
        self.boton_opcion2.bind("<Leave>", lambda event: status.restaurar2(self, event))  

        self.logo3 = utl.leer_imagen(utl.resource_path("imagenes/clientes.png"), size=(44, 59))
        self.boton_opcion3 = self.crear_boton("Clientes", self.mostrar_opcion3, image=self.logo3)
        self.boton_opcion3.image = self.logo3
        self.boton_opcion3.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion3.bind("<Enter>", lambda event: status.resaltar3(self, event))
        self.boton_opcion3.bind("<Leave>", lambda event: status.restaurar3(self, event))  

        self.logo4 = utl.leer_imagen(utl.resource_path("imagenes/pagos.png"), size=(44, 64))
        self.boton_opcion4 = self.crear_boton("Pagos", self.mostrar_opcion4, image=self.logo4)
        self.boton_opcion4.image = self.logo4
        self.boton_opcion4.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion4.bind("<Enter>", lambda event: status.resaltar4(self, event))
        self.boton_opcion4.bind("<Leave>", lambda event: status.restaurar4(self, event))  

        self.logo5 = utl.leer_imagen(utl.resource_path("imagenes/historial.png"), size=(44, 60))
        self.boton_opcion5 = self.crear_boton("Historial", self.mostrar_opcion5, image=self.logo5)
        self.boton_opcion5.image = self.logo5
        self.boton_opcion5.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion5.bind("<Enter>", lambda event: status.resaltar5(self, event))
        self.boton_opcion5.bind("<Leave>", lambda event: status.restaurar5(self, event))  


        self.logo6 = utl.leer_imagen(utl.resource_path("imagenes/salir.png"), size=(57, 59))
        self.boton_opcion6 = self.crear_boton("Salir", self.mostrar_opcion6, image=self.logo6)
        self.boton_opcion6.image = self.logo6
        self.boton_opcion6.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        self.boton_opcion6.bind("<Enter>", lambda event: status.resaltar6(self, event))
        self.boton_opcion6.bind("<Leave>", lambda event: status.restaurar6(self, event))  

        # Empaquetar los botones
        self.boton_opcion1.pack(fill="x")
        self.boton_opcion2.pack(fill="x")
        self.boton_opcion3.pack(fill="x")
        self.boton_opcion4.pack(fill="x")
        self.boton_opcion5.pack(fill="x")
        self.boton_opcion6.pack(fill="x")

        # Crear el frame para el contenido principal
        self.label_info = tk.Frame(self.root2, bg="white")
        self.label_info.pack(fill="both", expand=True)

        self.mostrar_opcion1()

    def crear_boton(self, texto, comando, **kwargs):
        boton = tk.Button(
            self.menu_lateral,
            text=texto,
            borderwidth=0,
            command=comando,
            bg="#1778FB",
            highlightthickness=2,
            activebackground="#FFFFFF",
            height=102,
            width=150,
            **kwargs
        )
        return boton

    def mostrar_opcion1(self):
        self.limpiar_contenido()
        logo = utl.leer_imagen(utl.resource_path("imagenes/logo.png"), size=(200, 200))
        self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
        self.logo_inicio_label.image = logo
        self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

        # Etiqueta de bienvenida
        self.username_label = Label(
            self.label_info,
            text="Welcome to\n Tempus Software.",
            anchor="center",
            bg="#FFFFFF",
            fg="#000000",
            font=("Hipstelvetica", 20),
        )
        self.username_label.place(relx=0.5, rely=0.60, anchor=CENTER)

        # Etiqueta de Eslogan
        self.eslogan_label = Label(
            self.label_info,
            text="Tu aliado tecnológico: eficiencia y confianza al\n alcance de tu mano.",
            bg="#FFFFFF",
            fg="#000000",
            font=("Avenir", 13),
        )
        self.eslogan_label.place(relx=0.5, rely=0.70, anchor=CENTER)

        # Etiqueta de permisos
        self.rol_label = Button(
            self.label_info,
            text=f"Nivel de Permisos: {self.rol_programa}",
            font=("Avenir", 14),
            width=30,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
        )
        self.rol_label.place(relx=0.5, rely=0.80, anchor=CENTER)

    def mostrar_opcion2(self):
        self.limpiar_contenido()
        logo = utl.leer_imagen(utl.resource_path("imagenes/logo.png"), size=(200, 200))
        self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
        self.logo_inicio_label.image = logo
        self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

    def mostrar_opcion3(self):
        self.limpiar_contenido()
        logo = utl.leer_imagen(utl.resource_path("imagenes/salir_azul.png"), size=(200, 200))
        self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
        self.logo_inicio_label.image = logo
        self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

    def mostrar_opcion4(self):
        self.limpiar_contenido()
        logo = utl.leer_imagen(utl.resource_path("imagenes/clientes_azul.png"), size=(200, 200))
        self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
        self.logo_inicio_label.image = logo
        self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

    def mostrar_opcion5(self):
        self.limpiar_contenido()
        logo = utl.leer_imagen(utl.resource_path("imagenes/historial_azul.png"), size=(200, 200))
        self.logo_inicio_label = tk.Label(self.label_info, image=logo, bg="#FFFFFF")
        self.logo_inicio_label.image = logo
        self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

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