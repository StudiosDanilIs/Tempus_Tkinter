import customtkinter as ctk
from tkinter import messagebox
import requests
import webbrowser

class GitHubDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Descargar Software")
        self.root.geometry("450x350")
        self.root.configure(bg="#1778FB")
        self.root.resizable(0, 0)

        # Estilo
        ctk.set_appearance_mode("light")  # Modo oscuro
        ctk.set_default_color_theme("blue")  # Tema de color

        # Etiqueta
        self.label = ctk.CTkLabel(
            root,
            text="Aplicaciones",
            font=("Montserrat", 38, "bold"),
            text_color="#1778FB",
        )
        self.label.pack(pady=(20, 0))
        
        self.label = ctk.CTkLabel(
            root,
            text="de Tempus",
            font=("Montserrat", 34),
            text_color="#1778FB",
        )
        self.label.pack(pady=(0, 10))

        # Opciones de descarga
        self.option_var = ctk.StringVar(value="Software a Descargar")
        self.option_menu = ctk.CTkOptionMenu(
            root,
            variable=self.option_var,
            values=["Sistema de Gestión", "Recuperar Usuarios"],
            fg_color="#1778FB",
            text_color="#FFFFFF",
            font=("Helvetica", 15),
            button_color="#1778FB",
            height=34,
            dropdown_font=("Helvetica", 13),
            dropdown_text_color="#000000",
            state="readonly",
        )
        self.option_menu.pack(pady=(30, 15))

        # Botón de descarga
        self.download_button = ctk.CTkButton(
            root,
            text="Descargar",
            command=self.download_file,
            fg_color="#1778FB",
            text_color="#FFFFFF",
            height=32,
            font=("Helvetica", 15),
            border_spacing=8,
            hover_color="#4E96FF",
        )
        self.download_button.pack(pady=(20,10))
        
        self.label22 = ctk.CTkButton(
            root,
            text="©DanielIs",
            font=("Montserrat", 21, "bold"),
            fg_color="#ECECEC",
            text_color="#1778FB",
            text_color_disabled="#4E96FF",
            height=32,
            border_spacing=8,
            hover_color="#ECECEC",
            command=lambda: self.abrir_perfil_github(),
        )
        self.label22.pack(side="bottom", anchor="e", pady=(0, 0))
        
        self.label22 = ctk.CTkLabel(
            root,
            text="Version 1.0",
            font=("Montserrat", 20, "bold"),
            text_color="#1778FB",
        )
        self.label22.place(x=15, y=315)

    def download_file(self):
        option = self.option_var.get()
        if option == "Sistema de Gestión":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus_Tkinter/main/Programas/Gestion.rar"
            local_filename = "Sistema de Gestión.rar"
        elif option == "Recuperar Usuarios":
            url = "https://raw.githubusercontent.com/StudiosDanilIs/Tempus_Tkinter/main/Programas/Recuperar.rar"
            local_filename = "Recuperar Usuarios.rar"
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

    def abrir_perfil_github(self):
        # Abre el perfil de Instagram en el navegador
        perfil_github = "https://github.com/StudiosDanilIs"  # Reemplaza con el perfil deseado
        webbrowser.open(perfil_github)
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = GitHubDownloader(root)
    root.mainloop()
