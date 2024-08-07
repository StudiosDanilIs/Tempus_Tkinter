import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import util.PhotoImagenes as utl

def InformacionTempus(self):
    if not self.subventana_abierta:
        miniVentana = tk.Toplevel()
        miniVentana.title("Detalles de la Version")
        miniVentana.geometry("780x400")
        miniVentana.resizable(0, 0)
        miniVentana.configure(bg="#FFFFFF")  # Color de fondo general más claro
        miniVentana.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(self))

        # Frame principal con un poco de padding
        main_frame = Frame(miniVentana, bg="#FFFFFF", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título de la aplicación (con un estilo más moderno)
        title_label = tk.Label(
            main_frame,
            text="Tempus Software",
            font=("Helvetica", 24, "bold"),
            bg="#FFFFFF",
            fg="#1E90FF"
        )
        title_label.pack(pady=10)

        # Descripción con un separador visual
        description_label = tk.Label(
            main_frame,
            text="Tempus App es un Software diseñado con el objetivo de mejorar la eficiencia y la productividad en el trabajo. Aunque no tiene fines de lucro, su enfoque es proporcionar soluciones prácticas y herramientas útiles para facilitar las tareas diarias.",
            font=("Arial", 12),
            wraplength=700,
            bg="#FFFFFF",
            fg="#000000"
        )
        description_label.pack(pady=10)
        
        separator = tk.Frame(main_frame, height=2, bg="#666666")
        separator.pack(fill=tk.X, pady=10)

        # Sección de equipo de desarrollo con un estilo más organizado
        team_label = tk.Label(
            main_frame,
            text="Equipo de Desarrollo",
            font=("Helvetica", 16, "bold"),
            bg="#FFFFFF",
            fg="#1E90FF"
        )
        team_label.pack(pady=10)


        def crear_perfil(name, role, image_file):
            profile_frame = Frame(main_frame, bg="#FFFFFF")
            profile_frame.pack(side=tk.LEFT, padx=18, pady=10)

            # Cargar la imagen utilizando la función leer_imagen del módulo utl
            image = utl.leer_imagen(utl.resource_path(f"imagenes/{image_file}"), (70, 70))

            # Crear label para la imagen y el texto
            image_label = tk.Label(profile_frame, image=image, bg="#FFFFFF")
            image_label.image = image
            image_label.pack()
            text_label = tk.Label(profile_frame, text=f"{name}\n{role}", font=("Arial", 12), bg="#FFFFFF", fg="#000000")
            text_label.pack()

                

        # Agregar perfiles de equipo
        crear_perfil("Daniel Hernandez", "Backend - Frontend - DBA", "user.png")
        crear_perfil("Victor Ramirez", "Frontend - Diseñador", "user.png")
        crear_perfil("Einner Zambrano", "Colaborador", "user.png")
        crear_perfil("Daniel Grimaldo", "Colaborador", "user.png")

        self.subventana_abierta = True
        
        def cerrar_sesion(self):
            self.subventana_abierta = False
            miniVentana.destroy()