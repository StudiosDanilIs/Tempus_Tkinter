import customtkinter as ctk
from tkinter import messagebox
import requests

class GitHubDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Downloader")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")

        # Estilo
        ctk.set_appearance_mode("dark")  # Modo oscuro
        ctk.set_default_color_theme("blue")  # Tema de color

        # Etiqueta
        self.label = ctk.CTkLabel(root, text="Descargar aplicación desde GitHub", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Opciones de descarga
        self.option_var = ctk.StringVar(value="Seleccione una opción")
        self.option_menu = ctk.CTkOptionMenu(root, variable=self.option_var, values=["Opción 1", "Opción 2"])
        self.option_menu.pack(pady=10)

        # Botón de descarga
        self.download_button = ctk.CTkButton(root, text="Descargar", command=self.download_file)
        self.download_button.pack(pady=20)

    def download_file(self):
        option = self.option_var.get()
        if option == "Opción 1":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus_Tkinter/main/gato.exe"
            local_filename = "archivo1.exe"
        elif option == "Opción 2":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus_Tkinter/main/perro.exe"
            local_filename = "archivo2.exe"
        else:
            messagebox.showerror("Error", "Por favor, seleccione una opción válida.")
            return

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica si hubo algún error en la solicitud

            with open(local_filename, 'wb') as file:
                file.write(response.content)

            messagebox.showinfo("Éxito", f"Aplicación descargada como {local_filename}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo descargar la aplicación: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = GitHubDownloader(root)
    root.mainloop()
