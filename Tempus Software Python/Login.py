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
                                    , borderwidth=0, background="#222222", cursor="hand2", command=self.ventana_modificar)
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
            messagebox.showinfo(
                message="Bienvenido a Tempus Software", title="Mensaje"
            )
            self.root.destroy()
            VentanaPrincipal()
        else:
            messagebox.showerror(
                message="Los Datos son Invalidos", title="Mensaje"
            )

            connection.close()
            
            


    def ventana_modificar(self):
        self.subventana = tk.Toplevel()
        self.subventana.title("Subventana")
        self.subventana.geometry("400x400")
        self.subventana.resizable(0, 0)

        self.titel_label = Label(self.subventana, text="Recuperar Acceso", anchor="s", fg="#4169E1",
                                    font=("yu gothic ui", 13, "bold"))
        self.titel_label.pack(fill=tk.X, padx=50, pady=8)
        
        
        self.cedula_label = Label(self.subventana, text="Ingresa Cedula", anchor="w", fg="#222222",
                                    font=("yu gothic ui", 13, "bold"))
        self.cedula_label.pack(fill=tk.X, padx=25, pady=8)

        self.cedula_entry = Entry(self.subventana, highlightthickness=0, relief=FLAT, fg="#222222",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.cedula_entry.pack(fill=tk.X, padx=30, pady=0)

        self.cedula_line = Canvas(self.subventana, width=300, height=2.0, bg="#4169E1", highlightthickness=0)
        self.cedula_line.pack(fill=tk.X, padx=30, pady=1)
        
        
        
        self.buscar_datos = Button(self.subventana, text="Buscar Datos",
                                font=("yu gothic ui", 13, "bold underline"), relief=FLAT,
                                activebackground="#4169E1", borderwidth=0, cursor="hand2",
                                command=self.Buscar)
        
        self.buscar_datos.pack(fill=tk.X, padx=30, pady=20)
        

    def Buscar(self):
        connection = sqlite3.connect(base_datos)
        cursor = connection.cursor()

        cedula = self.cedula_entry.get()

        cursor.execute(
            "SELECT Cedula FROM Usuarios WHERE Cedula = ?", (cedula,)
        )
        resultado_busqueda = cursor.fetchone()

        if resultado_busqueda:
            messagebox.showinfo(
                message="Datos Identificados Correctamente", title="Mensaje"
            )
            self.subventana.destroy()
            self.abrir_subventana_nuevos_datos(cedula)  # Pasamos la cédula como argumento
        else:
            messagebox.showerror(
                message="Datos No Encontrados. Verifique Nuevamente", title="Mensaje"
            )

        connection.close()

    def abrir_subventana_nuevos_datos(self, cedula):
        nueva_subventana = tk.Toplevel()
        nueva_subventana.title("Ingresar Nuevos Datos")
        nueva_subventana.geometry("400x300")
        nueva_subventana.resizable(0, 0)

        self.nuevo_usuario_label = Label(nueva_subventana, text="Nuevo Usuario", anchor="w", fg="#222222",
                                    font=("yu gothic ui", 13, "bold"))
        self.nuevo_usuario_label.pack(fill=tk.X, padx=25, pady=8)

        self.nuevo_usuario_entry = Entry(nueva_subventana, highlightthickness=0, relief=FLAT, fg="#222222",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.nuevo_usuario_entry.pack(fill=tk.X, padx=30, pady=0)

        self.nuevo_usuario_line = Canvas(nueva_subventana, width=300, height=2.0, bg="#4169E1", highlightthickness=0)
        self.nuevo_usuario_line.pack(fill=tk.X, padx=30, pady=1)
        
        
        
        self.nueva_clave_label = Label(nueva_subventana, text="Nueva Calve", anchor="w", fg="#222222",
                                    font=("yu gothic ui", 13, "bold"))
        self.nueva_clave_label.pack(fill=tk.X, padx=25, pady=8)

        self.nueva_clave_entry = Entry(nueva_subventana, highlightthickness=0, relief=FLAT, fg="#222222",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.nueva_clave_entry.pack(fill=tk.X, padx=30, pady=0)

        self.nueva_clave_line = Canvas(nueva_subventana, width=300, height=2.0, bg="#4169E1", highlightthickness=0)
        self.nueva_clave_line.pack(fill=tk.X, padx=30, pady=1)
        
        
        
        guardar_button = Button(nueva_subventana, text="Guardar",
                            command=lambda: self.actualizar_datos(cedula))
        guardar_button.pack()

    def actualizar_datos(self, cedula):
        nuevo_usuario = self.nuevo_usuario_entry.get()
        nueva_clave = self.nueva_clave_entry.get()
        
        # Validación de longitud mínima (por ejemplo, al menos 6 caracteres)
        if len(nuevo_usuario) < 6 or len(nueva_clave) < 6:
            messagebox.showerror("Error", "Los datos deben tener al menos 6 caracteres")
            return
        
        # Validación de datos en blanco
        if not nuevo_usuario or not nueva_clave:
            messagebox.showerror("Error", "No se permiten campos en blanco")
            return

        # Realiza la actualización en la base de datos
        connection = sqlite3.connect(base_datos)
        cursor = connection.cursor()

        try:
            cursor.execute("UPDATE Usuarios SET Usuario = ?, Clave = ? WHERE Cedula = ?",
                        (nuevo_usuario, nueva_clave, cedula))
            connection.commit()
            messagebox.showinfo("Mensaje", "Datos actualizados correctamente")
            nueva_subventana.destroy()
        except sqlite3.Error as e:
            print(f"Error al actualizar los datos: {e}")
            messagebox.showerror("Error", "No se pudieron actualizar los datos")

        connection.close()








def Mostrar():
    root = Tk()
    logo = PhotoImage(file='images\\logotipo.png')
    root.iconphoto(True, logo)
    CreateLogin(root)
    root.mainloop()


if __name__ == '__main__':
    Mostrar()