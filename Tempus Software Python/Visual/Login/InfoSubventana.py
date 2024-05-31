import tkinter as tk
from tkinter import *
from tkinter.font import BOLD


def InformacionTempus(self):
    miniVentana = tk.Toplevel()
    miniVentana.title("Tempus - Info")
    miniVentana.geometry("400x500")
    miniVentana.resizable(0, 0)

    self.lgn_frame = Frame(miniVentana, bg="#FFFFFF")
    self.lgn_frame.pack(fill=tk.BOTH)

    # Información de los Desarrolladores
    info_tempus = """Tempus App es un Software diseñado con el objetivo de mejorar la eficiencia y la productividad en el trabajo. Aunque no tiene fines de lucro, su enfoque es proporcionar soluciones prácticas y herramientas útiles para facilitar las tareas diarias.
    """

    titel_label = Label(
        self.lgn_frame,
        text="Tempus Software",
        anchor="s",
        fg="#FFFFFF",
        bg="#6495ED",
        font=("Khmer UI", 20),
    )
    titel_label.pack(fill=tk.X, padx=30, pady=1)

    info_label = Label(
        self.lgn_frame,
        text=info_tempus,
        anchor="s",
        fg="#FFFFFF",
        bg="#6495ED",
        justify="left",
        font=("yu gothic ui", 13),
        wraplength=320,  # Ancho máximo del texto antes de envolverlo
    )
    info_label.pack(fill=tk.X, padx=30, pady=1)

    info_desarrolladores = """
    @Daniel Alvíarez - Desarrollador BackEnd / DBA / FrontEnd.
    @Einner Zambrano - Desarrollador FrontEnd.
    @Daniel Grimaldo - Desarrollador FrontEnd.
    @Victor Ramirez - Desarrollador FrontEnd / Diseñador Gráfico.
    2024 UPTAIET
    """

    titel_label = Label(
        self.lgn_frame,
        text="Desarrolladores",
        anchor="s",
        fg="#FFFFFF",
        bg="#90EE90",
        font=("Khmer UI", 18, "bold"),
    )
    titel_label.pack(fill=tk.X, padx=30, pady=2)

    info_label = Label(
        self.lgn_frame,
        text=info_desarrolladores,
        anchor="w",
        fg="#FFFFFF",
        bg="#90EE90",
        font=("yu gothic ui", 13),
        justify="left",
        wraplength=320,  # Ancho máximo del texto antes de envolverlo
    )
    info_label.pack(fill=tk.X, padx=30, pady=1)
