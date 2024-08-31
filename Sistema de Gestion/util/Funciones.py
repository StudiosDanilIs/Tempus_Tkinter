import locale
import tkinter as tk
from datetime import datetime

# Forzar el locale al inicio y configurar la fuente
locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")

# Agrega un ReLoJ a la interfaz gráfica de usuario (GUI) de Tkinter
def actualizar_reloj(self):
    if hasattr(self, "dia_label") and self.dia_label.winfo_exists():
        fecha_actual = datetime.now().strftime("%d %B")
        anno_actual = datetime.now().strftime("%Y")
        
        dia_actual = datetime.now().strftime("%A").capitalize()
        hora_actual = datetime.now().strftime("%I:%M %p")
        
        # Convertir solo la primera letra del mes a mayúscula
        fecha_actual_resultado = fecha_actual[:3] + fecha_actual[3:].title()
        
        self.fecha_label.config(text=fecha_actual_resultado)
        self.anno_label.config(text=anno_actual.capitalize())
        
        self.dia_label.config(text=dia_actual)
        self.hora_label.config(text=hora_actual)
        self.root2.after(1000, lambda: actualizar_reloj(self))
    else:
        pass
