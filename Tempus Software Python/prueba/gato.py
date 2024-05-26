import tkinter as tk
from tkinter import PhotoImage
from tkinter.font import BOLD

class VentanaPrincipal:
    
                                      
    def __init__(self):        
        self.root = tk.Tk()                             
        self.root.title('Master panel')
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()                                    
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.config(bg='#fcfcfc')
        self.root.resizable(width=0, height=0)            
        
        logo = PhotoImage(file="imagenes\logotipo.png")
                        
        label = tk.Label( self.root, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.root.mainloop()
        