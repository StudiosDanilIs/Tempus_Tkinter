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