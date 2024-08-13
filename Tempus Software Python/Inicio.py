import tkinter as tk
from tkinter import *
import util.PhotoImagenes as utl
import tkinter.messagebox as messagebox
from util.Funciones import actualizar_reloj


class App:
    def __init__(self, root):
        self.root2 = root
        self.root2.geometry("1100x635")
        self.root2.title("Inicio - Area de Cuentas")
        self.label_info = Frame(root, bg="#f0f0f0")
        self.label_info.pack(fill=BOTH, expand=True)

        self.nombre_cuenta = "Administrador"

        # Etiqueta de bienvenida
        self.imagen_perfil = utl.leer_imagen(
            utl.resource_path("imagenes/2.png"), size=(40, 40)
        )
        self.imagen_perfil_boton = Label(
            self.label_info,
            image=self.imagen_perfil,
            width=50,
            bg="#f0f0f0",
            activebackground="#f0f0f0",
            bd=0,
            cursor="hand2",
            fg="white",
        )
        self.imagen_perfil_boton.place(x=150, y=10)

        self.bienvenida_label = Label(
            self.label_info,
            text=f"{self.nombre_cuenta}\nBienvenido de vuelta!",
            bg="#f0f0f0",
            fg="#1E90FF",
            font=("Avenir", 15),
            anchor="w",
            justify="left",
        )
        self.bienvenida_label.place(x=200, y=5)



        # Frame para mostrar la información dinámica
        self.info_frame = Frame(self.label_info, bg="#f0f0f0")
        self.info_frame.place(x=70, y=150, width=500, height=700)

        # Botones para cambiar la información
        self.imagen_agregar = utl.leer_imagen(
            utl.resource_path("imagenes/editar.png"), size=(58, 58)
        )
        self.imagen_agregar_boton = Button(
            self.label_info,
            image=self.imagen_agregar,
            width=115,
            height=115,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.mostrar_informacion("Modificar Cuenta"),
        )
        self.imagen_agregar_boton.place(x=0, y=0)

        self.imagen_eliminar = utl.leer_imagen(
            utl.resource_path("imagenes/agregar.png"), size=(58, 58)
        )
        self.imagen_eliminar_boton = Button(
            self.label_info,
            image=self.imagen_eliminar,
            width=115,
            height=115,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.mostrar_informacion("Agregar Cuenta"),
        )
        self.imagen_eliminar_boton.place(x=0, y=117)

        self.imagen_modificar = utl.leer_imagen(
            utl.resource_path("imagenes/borrar.png"), size=(58, 58)
        )
        self.imagen_modificar_boton = Button(
            self.label_info,
            image=self.imagen_modificar,
            width=115,
            height=115,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            cursor="hand2",
            fg="white",
            command=lambda: self.mostrar_informacion("Eliminar Cuenta"),
        )
        self.imagen_modificar_boton.place(x=0, y=234)
        
        
        self.espacio_blanco = Label(
            self.label_info,
            width=15,
            height=40,
            bg="#FFFFFF",
            activebackground="#FFFFFF",
            bd=0,
            fg="white",
        )
        self.espacio_blanco.place(x=0, y=351, width=117)


        # Muestra un CALENDARIO en la ventana principal
        self.label_dia = tk.Label(
            self.label_info,
            font=("Avenir", 18),
            anchor="w",
            justify="left",
            bg="#f0f0f0",
            fg="#1E90FF",
        )
        self.label_dia.place(x=705, y=120)

        # Muestra un RELOJ DIGITAL en la ventana principal
        self.label_reloj = tk.Label(
            self.label_info, width=20, font=("Avenir", 25), bg="#f0f0f0", fg="#1E90FF"
        )
        self.label_reloj.place(x=600, y=300)
        actualizar_reloj(self)

        self.mostrar_informacion("Inicio Sistema")

    def mostrar_informacion(self, opcion):
        # Limpiar el contenido del frame de información
        for widget in self.info_frame.winfo_children():
            widget.destroy()
            
        
        if opcion == "Modificar Cuenta":
            label = Label(
                self.info_frame,
                text="Modificar Usuario",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Montserrat", 17, "bold"),
            )
            label.place(x=130, y=10)

            self.password_label = Label(
                self.info_frame,
                text="Usuario",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=60)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=90)
            
            self.password_label = Label(
                self.info_frame,
                text="Contraseña",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=130)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=160)
            
            self.password_label = Label(
                self.info_frame,
                text="Nuevo Usuario",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=200)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=230)
            
            
            self.password_label = Label(
                self.info_frame,
                text="Nueva Contraseña",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=270)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=300)
            
            self.password_label = Label(
                self.info_frame,
                text="Clave Unica",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=340)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=370)
            
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Modificar Datos",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
            )
            self.guardar_clientes_button.place(x=142, y=420)


        elif opcion == "Agregar Cuenta":
            label = Label(
                self.info_frame,
                text="Agregar Usuario",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Montserrat", 17, "bold"),
            )
            label.place(x=130, y=10)

            self.password_label = Label(
                self.info_frame,
                text="Nombre",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=60)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=90)
            
            self.password_label = Label(
                self.info_frame,
                text="Cedula",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=130)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=160)
            
            self.password_label = Label(
                self.info_frame,
                text="Usuario",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=200)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=230)
            
            
            self.password_label = Label(
                self.info_frame,
                text="Contraseña",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=270)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=300)
            
            self.password_label = Label(
                self.info_frame,
                text="Clave Unica",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=340)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=370)
            
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Guardar Datos",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
            )
            self.guardar_clientes_button.place(x=142, y=420)
            

        elif opcion == "Eliminar Cuenta" and self.nombre_cuenta == "Administrador":
            label = Label(
                self.info_frame,
                text="Eliminar Usuario",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Montserrat", 17, "bold"),
            )
            label.place(x=130, y=10)

            self.password_label = Label(
                self.info_frame,
                text="Cedula",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=60)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=90)
            
            self.password_label = Label(
                self.info_frame,
                text="Clave Unica",
                anchor="w",
                justify="left",
                bg="#f0f0f0",
                fg="#1E90FF",
                font=("Poppins", 13, "bold"),
            )
            self.password_label.place(x=70, y=130)

            self.password_entry = Entry(
                self.info_frame,
                highlightthickness=2,
                highlightbackground="#1778FB",
                relief=tk.FLAT,
                fg="#0046A4",
                background="#f0f0f0",
                font=("Poppins", 12, "bold"),
                insertbackground="#1E90FF",
                width=25,
            )
            self.password_entry.place(x=140, y=160)
            
            self.guardar_clientes_button = tk.Button(
                self.info_frame,
                text="Eliminar Datos",
                font=("Poppins", 13, "bold"),
                width=22,
                bd=0,
                bg="#1E90FF",
                cursor="hand2",
                activebackground="#1778FB",
                fg="white",
            )
            self.guardar_clientes_button.place(x=142, y=210)


        elif opcion == "Inicio Sistema":
            self.title_label = Label(
                self.info_frame,
                text="Interfaz",
                anchor="w",
                bg="#f0f0f0",
                fg="#1778FB",
                font=("Montserrat", 30),
            )
            self.title_label.place(x=80, y=10)

            self.title2_label = Label(
                self.info_frame,
                text="para opciones\nde Usuario",
                anchor="w",
                justify=LEFT,
                bg="#f0f0f0",
                fg="#1778FB",
                font=("Montserrat", 36, "bold"),
            )
            self.title2_label.place(x=80, y=57)

root = Tk()
app = App(root)
root.mainloop()
