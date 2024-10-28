import tkinter as tk
from tkinter import *
import webbrowser
from tkinter.font import BOLD
import util.PhotoImagenes as utl

def InformacionTempus(self):
    if not self.subventana_abierta:
        miniVentana = tk.Toplevel()
        miniVentana.title("Detalles de la Versión")
        miniVentana.geometry("685x400")
        miniVentana.resizable(0, 0)
        miniVentana.configure(bg="#f0f0f0")
        miniVentana.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

        # Creamos un frame principal para organizar los elementos de la ventana
        main_frame = Frame(miniVentana, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título de la aplicación
        title_label = tk.Label(
            main_frame,
            text="Tempus Software",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 24, "bold"),
        )
        title_label.pack(pady=10)

        # Descripción con un separador visual
        description_label = tk.Label(
            main_frame,
            text="Tempus app es un software diseñado con el objetivo de mejorar la eficiencia y la productividad en el trabajo. Aunque no tiene fines de lucro, su enfoque es proporcionar soluciones prácticas y herramientas útiles para facilitar las tareas diarias.",
            font=("Arial", 12),
            wraplength=640,
            bg="#f0f0f0",
            fg="#232323",
        )
        description_label.pack(pady=10)

        # Sección de desarrollador con un estilo más organizado
        team_label = tk.Label(
            main_frame,
            text="Desarrollador y Herramientas",
            bg="#f0f0f0",
            fg="#1778FB",
            font=("Montserrat", 17),
        )
        team_label.pack(pady=15)

        def crear_perfil(name, role, image_file, command=None):
            profile_frame = Frame(main_frame, bg="#f0f0f0")
            profile_frame.pack(side=tk.LEFT, padx=18, pady=10)
            # Cargar la imagen utilizando la función leer_imagen del módulo utl
            image = utl.leer_imagen(f"{image_file}", size=(70, 70))
            # Crear label para la imagen y el texto
            image_label = tk.Label(profile_frame, image=image, bg="#f0f0f0")
            image_label.image = image
            image_label.pack()
            text_label = tk.Label(
                profile_frame,
                text=f"{name}\n{role}",
                font=("Arial", 12),
                bg="#f0f0f0",
                fg="#232323",
                cursor="hand2",
            )
            text_label.pack()
            if command:
                text_label.bind("<Button-1>", command)

        # Agregar perfil del desarrollador
        crear_perfil("Desarrollador", "@StudiosDaniels", "programador.png", lambda event: abrir_perfil_github())
        crear_perfil("Lenguaje usado", "Python 3.12", "python.png")
        crear_perfil("Base de datos", "MySQL", "mysql.png")
        crear_perfil("Entorno Trabajo", "GitHub", "github.png")

        # permite que la subventana se abra solo si no está abierta
        self.subventana_abierta = True

        def cerrar_sesion(self):
            self.subventana_abierta = False
            miniVentana.destroy()

        def abrir_perfil_github():
            # Abre el perfil de GitHub en el navegador
            perfil_github = "https://github.com/StudiosDanilIs"  # Enlace al perfil de GitHub
            webbrowser.open(perfil_github)
