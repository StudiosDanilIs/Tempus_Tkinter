import locale
import tkinter as tk
from datetime import datetime

# Forzar el locale al inicio y configurar la fuente
locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")

# Agrega un ReLoJ a la interfaz gráfica de usuario (GUI) de Tkinter
def actualizar_reloj(self):
    if hasattr(self, "label_reloj") and self.label_reloj.winfo_exists():
        hora_actual = datetime.now().strftime("%I:%M %p")
        dia_actual = datetime.now().strftime("%A").capitalize()
        self.label_reloj.config(text=hora_actual)
        self.label_dia.config(text=dia_actual.capitalize())
        self.root2.after(1000, lambda: actualizar_reloj(self))
    else:
        pass
