import tkinter as tk
from tkinter import ttk

def mostrar_opcion3(self):
    self.limpiar_contenido()

    titel_label = tk.Label(
        self.label_info,
        text="Informacion del Cliente",
        fg="#1778FB",
        bg="#E6F0F3",
        font=("Poppins", 17, "bold"),
    )
    titel_label.place(x=10, y=10)

    # cedula opcion de recuperación
    self.cedula_label = tk.Label(
        self.label_info,
        text="Nombre",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("Poppins", 13, "bold"),
    )
    self.cedula_label.place(x=10, y=55)

    # entrada de cedula
    self.cedula_entry = tk.Entry(
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.cedula_entry.place(x=10, y=85)
    

    # usurario opcion de recuperación
    self.apellido_label = tk.Label(
        self.label_info,
        text="Apellido",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("Poppins", 13, "bold"),
    )
    self.apellido_label.place(x=10, y=125)

    # entrada de usuario y  validación de tabulador
    self.apellido_entry = tk.Entry(  # Cambié el nombre de la variable
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.apellido_entry.place(x=10, y=155)

    # clave opcion de recuperación
    self.cedula_label2 = tk.Label(  # Cambié el nombre de la variable
        self.label_info,
        text="Cedula",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("Poppins", 13, "bold"),
    )
    self.cedula_label2.place(x=10, y=195)

    # Crear un estilo para el Combobox con borde de color
    self.combo = ttk.Combobox(
        self.label_info,
        state="readonly",
        width=2,
        values=["V", "J", "P", "E"],
    )
    self.combo.place(x=10, y=225)
    self.combo.set("V")  # Establece un valor predeterminado (puedes cambiarlo según tus necesidades)
    self.combo.config(justify="center", foreground="#0046A4", font=("Poppins", 12, "bold"))


    self.cedula_entry2 = tk.Entry(  # Cambié el nombre de la variable
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=22,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.cedula_entry2.place(x=64, y=225)

    # usurario opcion de recuperación
    self.telefono_label = tk.Label(  # Cambié el nombre de la variable
        self.label_info,
        text="Telefono",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("Poppins", 13, "bold"),
    )
    self.telefono_label.place(x=10, y=265)

    # entrada de usuario y  validación de tabulador
    self.telefono_entry = tk.Entry(  # Cambié el nombre de la variable
        self.label_info,
        highlightthickness=2,
        highlightbackground="#1778FB",
        relief=tk.FLAT,
        width=28,
        fg="#0046A4",
        font=("Poppins", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.telefono_entry.place(x=10, y=295)

    # usurario opcion de recuperación
    self.direccion_label = tk.Label(  # Cambié el nombre de la variable
        self.label_info,
        text="Direccion",
        fg="#1E90FF",
        bg="#E6F0F3",
        font=("Poppins", 13, "bold"),
    )
    self.direccion_label.place(x=10, y=335)

    # entrada de usuario y  validación de tabulador
    self.direccion_text = tk.Text(
        self.label_info,
        height=2,
        width=28,
        font=("Poppins", 12, "bold"),
        fg="#0046A4",
        insertbackground="#1778FB",
        highlightthickness=2,
        highlightbackground="#1E90FF",
        relief=tk.FLAT,
    )
    self.direccion_text.place(x=10, y=365)

    # botón de guardar datos
    guardar_button1 = tk.Button(  # Cambié el nombre de la variable
        self.label_info,
        text="Añadir Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
    )
    guardar_button1.place(x=35, y=445)

    # botón de guardar datos
    guardar_button2 = tk.Button(  # Cambié el nombre de la variable
        self.label_info,
        text="Modificar Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
    )
    guardar_button2.place(x=35, y=505)

    # botón de guardar datos
    guardar_button3 = tk.Button(  # Cambié el nombre de la variable
        self.label_info,
        text="Eliminar Cliente",
        font=("Poppins", 13, "bold"),
        width=20,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#1778FB",
        fg="white",
    )
    guardar_button3.place(x=35, y=565)