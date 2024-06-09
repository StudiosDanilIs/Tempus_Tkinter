import tkinter as tk
from tkinter import *
from tkinter.font import BOLD


def InformacionTempus(self):
    miniVentana = tk.Toplevel()
    miniVentana.title("Tempus - Info")
    miniVentana.geometry("600x340")
    miniVentana.resizable(0, 0)

    # Frame para la información de los desarrolladores
    self.lgn_frame = Frame(miniVentana, bg="#E6F0F3")
    self.lgn_frame.pack(fill=tk.BOTH)

    # Título de la aplicación
    title_label = tk.Label(
        self.lgn_frame,
        text=" Tempus Software",
        justify=LEFT,
        anchor="w",
        font=("Helvetica", 20, "bold"),
        bg="#1E90FF",
        fg="#E6F0F3",
        height=2,
    )
    title_label.pack(fill=tk.BOTH, pady=14, padx=18)

    # Descripción de la aplicación
    description_text = """Tempus App es un Software diseñado con el objetivo de mejorar la eficiencia y la productividad en el trabajo. Aunque no tiene fines de lucro, su enfoque es proporcionar soluciones prácticas y herramientas útiles para facilitar las tareas diarias."""
    description_label = tk.Label(
        self.lgn_frame,
        text=description_text,
        justify=LEFT,
        font=("arial", 12),
        wraplength=530,
        bg="#E6F0F3",
        fg="#333333",
        height=5,
    )
    description_label.pack(fill=tk.BOTH, pady=6, padx=18)

    # Información del equipo de desarrollo
    team_label = tk.Label(
        self.lgn_frame,
        text=" Equipo de Desarrollo",
        justify=LEFT,
        anchor="w",
        font=("Helvetica", 14, "bold"),
        bg="#E6F0F3",
        fg="#1E90FF",
    )
    team_label.pack(fill=tk.BOTH, padx=19, pady=(2, 30))

    # perfil de Alvíarez
    profile1_label = tk.Label(
        self.lgn_frame,
        text="Daniel Alvíarez\nBackend - Frontend - DBA",
        font=("arial", 9, "bold"),
        justify=CENTER,
        anchor="nw",
        bg="#E6F0F3",
        fg="#333333",
    )
    profile1_label.pack(fill=tk.BOTH, side=LEFT, padx=(10, 8), pady=15)

    # perfil de Zambrano
    profile1_label = tk.Label(
        self.lgn_frame,
        text="Einner Zambrano\nBackend",
        font=("arial", 9, "bold"),
        justify=CENTER,
        anchor="nw",
        bg="#E6F0F3",
        fg="#333333",
    )
    profile1_label.pack(fill=tk.BOTH, side=LEFT, padx=(8, 8), pady=15)

    # perfil de Grimaldo
    profile1_label = tk.Label(
        self.lgn_frame,
        text="Daniel Grimaldo\nBackend",
        font=("arial", 9, "bold"),
        justify=CENTER,
        anchor="nw",
        bg="#E6F0F3",
        fg="#333333",
    )
    profile1_label.pack(fill=tk.BOTH, side=LEFT, padx=(8, 8), pady=15)

    # perfil de Ramirez
    profile1_label = tk.Label(
        self.lgn_frame,
        text="Victor Ramirez\nBackend - Diseñador Gráfico",
        font=("arial", 9, "bold"),
        justify=CENTER,
        anchor="nw",
        bg="#E6F0F3",
        fg="#333333",
    )
    profile1_label.pack(fill=tk.BOTH, side=LEFT, padx=(8, 10), pady=15)
