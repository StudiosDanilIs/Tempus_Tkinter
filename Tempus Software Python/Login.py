import tkinter as tk
import sqlite3
from tkinter import ttk, PhotoImage, messagebox
from tkinter.font import BOLD
from prueba.gato import VentanaPrincipal

base_datos = "SQLite\Registro.db"


class CreateLogin:

    def verificar(self, root):
        self.root = root
        connection = sqlite3.connect(base_datos)
        cursor = connection.cursor()

        usu = self.usuario.get()
        password = self.password.get()

        cursor.execute(
            "SELECT * FROM Usuarios WHERE Usuario = ? AND Clave = ?", (usu, password)
        )
        resultado = cursor.fetchone()

        if resultado:
            self.root.destroy()
            VentanaPrincipal()
        else:
            messagebox.showerror(
                message="La contraseña no es correcta", title="Mensaje"
            )

            connection.close()

    def __init__(self, root):
        self.root = root
        ruta_icono = "imagenes\logotipo.ico"
        self.root.geometry("470x570")
        self.root.title("Login - Tempus Software")
        self.root.iconbitmap(ruta_icono)
        self.root.protocol("WM_DELETE_WINDOW", self.Close_Windows)

        # Crear un Contendor para la Imagen del Login
        self.logo_image = PhotoImage(file="imagenes\logotipo.png")

        frame_form = tk.Frame(
            self.root, bd=0, relief=tk.SOLID, bg="#F0F8FF", background="#F0F8FF"
        )
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg="#CBD5E8"
        )
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(
            frame_form_top,
            image=self.logo_image,
            background="#CBD5E8",
        )
        title.pack(pady=7, expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(
            frame_form,
            height=50,
            bd=0,
            relief=tk.SOLID,
            bg="#CBD5E8",
        )
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(
            frame_form_fill,
            text="Usuario",
            font=("Comic Sans MS", 14),
            fg="#4E4E4E",
            bg="#fcfcfc",
            anchor="w",
            background="#CBD5E8",
            pady=10,
        )
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=0)
        self.usuario = ttk.Entry(frame_form_fill, font=("arial", 14))
        self.usuario.pack(fill=tk.X, padx=50, pady=10)

        etiqueta_password = tk.Label(
            frame_form_fill,
            text="Contraseña",
            font=("Comic Sans MS", 14),
            fg="#4E4E4E",
            bg="#4E4E4E",
            anchor="w",
            background="#CBD5E8",
        )
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=("Times", 14))
        self.password.pack(fill=tk.X, padx=50, pady=10)
        self.password.config(show="*")

        recuperar = tk.Button(
            frame_form_fill,
            text="Recuperar Acceso",
            cursor="plus",
            font=("Comic Sans MS", 15),
            bg="#3F8BBA",
            bd=0,
            fg="#F5F5F5",
            command=lambda: self.ventana_modificar(),
        )
        recuperar.place(x=220, y=200)

        inicio = tk.Button(
            frame_form_fill,
            text="Iniciar Sesión",
            cursor="plus",
            font=("Comic Sans MS", 15),
            bg="#3F8BBA",
            bd=0,
            fg="#F5F5F5",
            command=lambda: self.verificar(root),
        )
        inicio.place(x=65, y=200)
        inicio.bind("<Return>", (lambda event: self.verificar()))
        # end frame_form_fill
        self.root.mainloop()

    # Para saber si se cerrará la ventana o no
    def Close_Windows(self):
        if messagebox.askokcancel("Close", "¿Desea cerrar la aplicación?"):
            self.root.destroy()

    def ventana_modificar(self):
        self.subventana = tk.Toplevel(root)
        self.subventana.title("Subventana")
        self.subventana.geometry("300x200")

        # Agrega opciones o contenido a la subventana
        etiqueta = tk.Label(self.subventana, text="¡Bienvenido a la subventana!")
        etiqueta.pack()


# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CreateLogin(root)
    root.mainloop()
