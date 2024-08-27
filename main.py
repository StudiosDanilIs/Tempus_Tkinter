import customtkinter as ctk
from tkinter import messagebox
import requests

class GitHubDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Downloader")
        self.root.geometry("400x300")
        self.root.configure(bg="#1778FB")

        # Estilo
        ctk.set_appearance_mode("dark")  # Modo oscuro
        ctk.set_default_color_theme("blue")  # Tema de color

        # Etiqueta
        self.label = ctk.CTkLabel(root, text="Descargar Aplicacion para Tempus", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Opciones de descarga
        self.option_var = ctk.StringVar(value="Opciones a Descargar")
        self.option_menu = ctk.CTkOptionMenu(root, variable=self.option_var, values=["Tempus Gestión", "Tempus Reset"], fg_color="#1778FB", text_color="#000000")
        self.option_menu.pack(pady=10)

        # Botón de descarga
        self.download_button = ctk.CTkButton(root, text="Descargar", command=self.download_file, fg_color="#1778FB", text_color="#000000")
        self.download_button.pack(pady=20)
        
    def download_file(self):
        option = self.option_var.get()
        if option == "Tempus Gestión":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus-App/main/Gestion.exe"
            local_filename = "Sistema de Gestión.exe"
        elif option == "Tempus Reset":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus-App/main/Recuperar.exe"
            local_filename = "Recuperar Usuarios.exe"
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
