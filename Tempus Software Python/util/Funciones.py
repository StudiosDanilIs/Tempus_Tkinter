from tkinter import *
import tkinter as tk
from time import strftime
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def actualizar_reloj(self):
    if hasattr(self, 'label_reloj') and self.label_reloj.winfo_exists():
        hora_actual = strftime("%I:%M:%S")  # Formato de 12 horas con AM/PM
        dia_actual = datetime.now().strftime("%A")
        self.label_reloj.config(text=hora_actual)
        self.label_dia.config(text=dia_actual.capitalize())
        self.root2.after(1000, lambda: actualizar_reloj(self))  # Llamada correcta a la función
    else:
        pass