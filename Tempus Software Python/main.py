import tkinter as tk
from Visual.Login.EstructuraLogin import CreateLogin

if __name__ == "__main__":
    root = tk.Tk()
    logo = "images\\logotipo.ico"
    root.iconbitmap(True, logo)

    CreateLogin(root)
    root.mainloop()