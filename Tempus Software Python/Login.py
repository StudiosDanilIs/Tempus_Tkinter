import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.font import BOLD
from prueba.gato import VentanaPrincipal

base_datos = "SQLite\Registro.db"

class CreateLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry('480x670')
        self.root.resizable(0, 0)
        self.root.title("Login - Tempus Software")
        

        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.root, bg='#222222')
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)


        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\logotipo.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#222222')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.pack(side="top", fill=tk.X, pady=30)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", anchor="w", bg="#222222", fg="#F8F8FF",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.pack(fill=tk.X, padx=25, pady=8)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#222222", fg="#F8F8FF",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.pack(fill=tk.X, padx=30, pady=0)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0)
        self.username_line.pack(fill=tk.X, padx=30, pady=1)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", anchor="w", bg="#222222", fg="#F8F8FF",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.pack(fill=tk.X, padx=25, pady=8)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#222222", fg="#F8F8FF",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.pack(fill=tk.X, padx=30, pady=0)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#4169E1", highlightthickness=0)
        self.password_line.pack(fill=tk.X, padx=30, pady=1)
        
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#222222')
        self.lgn_button_label.image = photo
        self.lgn_button_label.pack(side="top", fill=tk.X, pady=40)
        self.login = Button(self.lgn_button_label, text='Iniciar Sesion', font=("yu gothic ui", 13, "bold"), width=10, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=lambda: self.verificar(root))
        self.login.pack(pady=5)
        self.login.bind("<Return>", (lambda event: self.verificar()))
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Recuperar Acceso",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#4169E1"
                                    , borderwidth=0, background="#222222", cursor="hand2",command=lambda: self.ventana_modificar())
        self.forgot_button.place(x=170, y=515)

        # ========================================================================
        # ============================Info Tempus=================================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Tempus Software -Beta-",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#4169E1"
                                    , borderwidth=0, background="#222222", cursor="hand2")
        self.forgot_button.place(x=265, y=620)


    def verificar(self, root):
        self.root = root
        connection = sqlite3.connect(base_datos)
        cursor = connection.cursor()

        usuario = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute(
            "SELECT * FROM Usuarios WHERE Usuario = ? AND Clave = ?", (usuario, password)
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
            
            


    def ventana_modificar(self):
        self.subventana = tk.Toplevel()
        self.subventana.title("Subventana")
        self.subventana.geometry("300x200")

        # Agrega opciones o contenido a la subventana
        etiqueta = tk.Label(self.subventana, text="¡Bienvenido a la subventana!")
        etiqueta.pack()


def Mostrar():
    root = Tk()
    logo = PhotoImage(file='images\\logotipo.png')
    root.iconphoto(True, logo)
    CreateLogin(root)
    root.mainloop()


if __name__ == '__main__':
    Mostrar()