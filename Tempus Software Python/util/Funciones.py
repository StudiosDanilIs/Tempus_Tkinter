import locale
import tkinter as tk
from datetime import datetime

# Forzar el locale al inicio y configurar la fuente
locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")

# Agrega un ReLoJ a la interfaz gráfica de usuario (GUI) de Tkinter
def actualizar_reloj(self):
    if hasattr(self, "label_reloj") and self.label_reloj.winfo_exists():
        hora_actual = datetime.now().strftime("%A")
        dia_actual = datetime.now().strftime("%d %B").capitalize()
        
        hora_actual2 = datetime.now().strftime("%I:%M %p")
        dia_actual2 = datetime.now().strftime("%Y").capitalize()
        
        
        self.label_reloj.config(text=hora_actual)
        self.label_dia.config(text=dia_actual.capitalize())
        
        self.label_reloj2.config(text=hora_actual2)
        self.label_dia2.config(text=dia_actual2.capitalize())
        self.root2.after(1000, lambda: actualizar_reloj(self))
    else:
        pass
