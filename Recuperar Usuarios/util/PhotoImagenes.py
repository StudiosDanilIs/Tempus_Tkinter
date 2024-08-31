import sys
import os
from PIL import ImageTk, Image


# Código de la función para leer imágenes
def leer_imagen(path, size):
    """Lee una imagen y la redimensiona, manejando errores de ruta"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Ajusta esta parte para reflejar tu estructura de carpetas
    image_path = os.path.join(script_dir, "..", "imagenes", path)

    try:
        return ImageTk.PhotoImage(Image.open(image_path).resize(size, Image.ADAPTIVE))
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen '{path}'. Verifica la ruta.")
        return None


def resource_path(relative_path):
    """Obtiene la ruta absoluta a un recurso, funciona tanto en desarrollo como en PyInstaller."""
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
