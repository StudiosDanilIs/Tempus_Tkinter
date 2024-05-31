from PIL import ImageTk, Image as imim
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from Visual.Login.EstructuraLogin import *


class CreateLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("480x670")
        self.root.resizable(0, 0)
        self.root.title("Login - Tempus Software")

        VentanaLogin(self=self, root=root)
