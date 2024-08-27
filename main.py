import customtkinter as ctk
from tkinter import messagebox
import requests

class GitHubDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Descargar Software")
        self.root.geometry("400x300")
        self.root.configure(bg="#1778FB")

        # Estilo
        ctk.set_appearance_mode("light")  # Modo oscuro
        ctk.set_default_color_theme("blue")  # Tema de color

        # Etiqueta
        self.label = ctk.CTkLabel(
            root,
            text="Aplicaciones",
            font=("Montserrat", 32, "bold"),
            text_color="#1778FB",
        )
        self.label.pack(pady=(20, 0))
        
        self.label = ctk.CTkLabel(
            root,
            text="de Tempus",
            font=("Montserrat", 28),
            text_color="#1778FB",
        )
        self.label.pack(pady=(0, 10))

        # Opciones de descarga
        self.option_var = ctk.StringVar(value="Opciones a Descargar")
        self.option_menu = ctk.CTkOptionMenu(
            root,
            variable=self.option_var,
            values=["Sistema de Gestión", "Recuperar Usuarios"],
            fg_color="#1778FB",
            text_color="#FFFFFF",
            font=("Helvetica", 15),
            button_color="#1778FB",
            height=32,
            dropdown_font=("Helvetica", 13),
            dropdown_text_color="#000000",
            state="readonly",
        )
        self.option_menu.pack(pady=(30, 5))

        # Botón de descarga
        self.download_button = ctk.CTkButton(
            root,
            text="Descargar",
            command=self.download_file,
            fg_color="#1778FB",
            text_color="#FFFFFF",
            height=30,
            font=("Helvetica", 15),
            border_spacing=8,
            hover_color="#4E96FF",
        )
        self.download_button.pack(pady=(20,10))
        
        self.label = ctk.CTkLabel(
            root,
            text="©DanielIs   ",
            font=("Montserrat", 18, "bold"),
            text_color="#1778FB",
        )
        self.label.pack(side="bottom", anchor="e", pady=(0, 10))

    def download_file(self):
        option = self.option_var.get()
        if option == "Sistema de Gestión":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus_Tkinter/main/Programas/Gestion.rar"
            local_filename = "Sistema de Gestión.rar"
        elif option == "Recuperar Usuarios":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus_Tkinter/main/Programas/Recuperar.exe"
            local_filename = "Recuperar Usuarios.exe"
        else:
            messagebox.showerror("Error", "Por favor, seleccione una opción válida.")
            return

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica si hubo algún error en la solicitud

            with open(local_filename, "wb") as file:
                file.write(response.content)

            messagebox.showinfo("Éxito", f"Aplicación descargada como {local_filename}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo descargar la aplicación: {e}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = GitHubDownloader(root)
    root.mainloop()
