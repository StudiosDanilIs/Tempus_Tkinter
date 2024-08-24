import tkinter as tk
from tkinter import messagebox
import requests

class GitHubDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Downloader")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Descargar aplicación desde GitHub")
        self.label.pack(pady=10)

        self.download_button = tk.Button(root, text="Descargar", command=self.download_file)
        self.download_button.pack(pady=20)

    def download_file(self):
        url = "https://github.com/StudiosDanilIs/Tempus_Tkinter/releases/download/v1.0/tu_aplicacion.exe"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica si hubo algún error en la solicitud

            with open(local_filename, 'wb') as file:
                file.write(response.content)

            messagebox.showinfo("Éxito", f"Aplicación descargada como {local_filename}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo descargar la aplicación: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitHubDownloader(root)
    root.mainloop()
