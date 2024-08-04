from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl

def resaltar1(self, event):
    if not self.presionado:
        logo_cambio1 = utl.leer_imagen(utl.resource_path("imagenes/menu/home2.png"), size=(44, 61))
        self.boton_opcion1.config(image=logo_cambio1, bg="#FFFFFF")
        self.boton_opcion1.image = logo_cambio1
        
def resaltar2(self, event):        
    if not self.presionado:
        logo_cambio2 = utl.leer_imagen(utl.resource_path("imagenes/menu/solicitudes2.png"), size=(59, 61))
        self.boton_opcion2.config(image=logo_cambio2, bg="#FFFFFF")
        self.boton_opcion2.image = logo_cambio2 
            
def resaltar3(self, event):
    if not self.presionado:
        logo_cambio3 = utl.leer_imagen(utl.resource_path("imagenes/menu/clientes2.png"), size=(44, 59))
        self.boton_opcion3.config(image=logo_cambio3, bg="#FFFFFF")
        self.boton_opcion3.image = logo_cambio3
        
def resaltar4(self, event):        
    if not self.presionado:
        logo_cambio4 = utl.leer_imagen(utl.resource_path("imagenes/menu/pagos2.png"), size=(44, 64))
        self.boton_opcion4.config(image=logo_cambio4, bg="#FFFFFF")
        self.boton_opcion4.image = logo_cambio4
        
def resaltar5(self, event):
    if not self.presionado:
        logo_cambio5 = utl.leer_imagen(utl.resource_path("imagenes/menu/historial2.png"), size=(44, 60))
        self.boton_opcion5.config(image=logo_cambio5, bg="#FFFFFF")
        self.boton_opcion5.image = logo_cambio5
        
def resaltar6(self, event):        
    if not self.presionado:
        logo_cambio6 = utl.leer_imagen(utl.resource_path("imagenes/menu/salir2.png"), size=(57, 59))
        self.boton_opcion6.config(image=logo_cambio6, bg="#FFFFFF")
        self.boton_opcion6.image = logo_cambio6
        
        
        
def restaurar1(self, event):
    if not self.presionado:
        self.boton_opcion1.config(image=self.logo1 ,bg="#1778FB")  
            
def restaurar2(self, event):         
    if not self.presionado:
        self.boton_opcion2.config(image=self.logo2 ,bg="#1778FB")     

def restaurar3(self, event):
    if not self.presionado:
        self.boton_opcion3.config(image=self.logo3 ,bg="#1778FB")  
            
def restaurar4(self, event):         
    if not self.presionado:
        self.boton_opcion4.config(image=self.logo4 ,bg="#1778FB")                      
        
def restaurar5(self, event):
    if not self.presionado:
        self.boton_opcion5.config(image=self.logo5 ,bg="#1778FB")  
            
def restaurar6(self, event):         
    if not self.presionado:
        self.boton_opcion6.config(image=self.logo6 ,bg="#1778FB")   