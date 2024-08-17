import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Crear la ventana principal con ThemedTk
root = ThemedTk(theme="arc")
root.geometry("600x400")

# Crear un objeto Style
style = ttk.Style()

# Configurar el estilo del Treeview
style.configure("Treeview",
    background="#DCEBFF",
    fieldbackground="#DCEBFF",
    foreground="#1778FB"
)

# Configurar el estilo de los encabezados del Treeview
style.configure("Treeview.Heading",
    background="#DCEBFF",
    foreground="#0046A4",
    font=("Arial", 12, "bold"),
    relief="raised",
    borderwidth=2,
    anchor="center"
)

# Configurar el estilo del Scrollbar
style.configure("Vertical.TScrollbar",
    troughcolor="#1778FB",
    background="#1778FB",
    relief="flat",
    borderwidth=1,
    width=12,
    highlightcolor="#1778FB",
    highlightbackground="#1778FB",
    highlightthickness=1
)

# Crear el marco de información
info_frame = ttk.Frame(root)
info_frame.place(x=50, y=50, width=500, height=300)

# Crear un Canvas
canvas = tk.Canvas(info_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Crear un Frame dentro del Canvas
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Añadir el Frame al Canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Crear el Treeview dentro del Frame
tree = ttk.Treeview(scrollable_frame, columns=("ID", "Nombre", "Apellido", "Cedula", "Telefono"),
                    show="headings", style="Treeview")

# Configurar los encabezados de las columnas
tree.heading("ID", text="#")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")
tree.heading("Cedula", text="Cédula")
tree.heading("Telefono", text="Teléfono")

# Configurar la fuente para los encabezados y las filas
tree.tag_configure("heading", font=("Arial", 12, "bold"))
tree.tag_configure("row", font=("Arial", 11))

# Configurar el ancho de las columnas y la alineación
for col in tree["columns"]:
    tree.column(col, minwidth=100, width=114, anchor="center")

# Crear la barra de desplazamiento
scrollbar = ttk.Scrollbar(
    info_frame,
    orient="vertical",
    command=canvas.yview,
    style="Vertical.TScrollbar",
)
canvas.configure(yscrollcommand=scrollbar.set)

# Colocar el Treeview y la barra de desplazamiento en el marco
tree.pack(fill="both", expand=True)
scrollbar.grid(row=0, column=1, sticky="ns")

# Configurar el marco de información    
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_columnconfigure(1, weight=0)

# Iniciar el bucle principal de la aplicación
root.mainloop()
