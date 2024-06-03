from PIL import ImageTk, Image as imim
import tkinter as tk
from tkinter import PhotoImage


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio - Tempus Software")
        self.root.geometry("1200x700")
        self.root.resizable(0, 0)
        
        self.lgn_frame = Frame(root, bg="#E6F0F3")
        self.lgn_frame.pack(fill=tk.BOTH)

        # Información de los Desarrolladores
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