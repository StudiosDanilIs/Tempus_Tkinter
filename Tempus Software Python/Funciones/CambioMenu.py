from tkinter import *
import tkinter as tk
import util.PhotoImagenes as utl

def resaltar1(self, event):
    if not self.presionado:
        logo_cambio1 = utl.leer_imagen(utl.resource_path("imagenes/usuario.png"), size=(57, 42))
        self.boton_opcion1.config(image=logo_cambio1, bg="#ffffff")
        self.boton_opcion1.image = logo_cambio1
        
def resaltar2(self, event):        
    if not self.presionado:
        logo_cambio2 = utl.leer_imagen(utl.resource_path("imagenes/solicitud_azul.png"), size=(57, 42))
        self.boton_opcion2.config(image=logo_cambio2, bg="#ffffff")
        self.boton_opcion2.image = logo_cambio2 
            
def resaltar3(self, event):
    if not self.presionado:
        logo_cambio3 = utl.leer_imagen(utl.resource_path("imagenes/clientes_azul.png"), size=(57, 42))
        self.boton_opcion3.config(image=logo_cambio3, bg="#ffffff")
        self.boton_opcion3.image = logo_cambio3
        
def resaltar4(self, event):        
    if not self.presionado:
        logo_cambio4 = utl.leer_imagen(utl.resource_path("imagenes/pagos_azul.png"), size=(57, 42))
        self.boton_opcion4.config(image=logo_cambio4, bg="#ffffff")
        self.boton_opcion4.image = logo_cambio4
        
def resaltar5(self, event):
    if not self.presionado:
        logo_cambio5 = utl.leer_imagen(utl.resource_path("imagenes/historial_azul.png"), size=(57, 42))
        self.boton_opcion5.config(image=logo_cambio5, bg="#ffffff")
        self.boton_opcion5.image = logo_cambio5
        
def resaltar6(self, event):        
    if not self.presionado:
        logo_cambio6 = utl.leer_imagen(utl.resource_path("imagenes/salir_azul.png"), size=(57, 42))
        self.boton_opcion6.config(image=logo_cambio6, bg="#ffffff")
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