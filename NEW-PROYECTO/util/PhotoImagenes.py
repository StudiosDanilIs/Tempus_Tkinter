import os
from PIL import ImageTk, Image


# Código de la función para leer imágenes
def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))


# Código de la función para gestionar rutas absoluta y ruta relativa
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
