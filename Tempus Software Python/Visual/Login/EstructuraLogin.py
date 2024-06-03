from PIL import ImageTk, Image as imim
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from RelacionMariaDB.VerificarCuenta import verificar_sesion as Verificar
from Visual.Login.SubEstructuraLogin import SubventanaLogin as Subventana
from Visual.Login.InfoSubventana import InformacionTempus as Info


def VentanaLogin(self, root):
    # ====== Login Frame =========================
    self.lgn_frame = Frame(self.root, bg="#E6F0F3")
    self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

    # ========================================================================
    # ============ Sign In Image =============================================
    # ========================================================================
    self.sign_in_image = imim.open("images\\logotipo.png")
    photo = ImageTk.PhotoImage(self.sign_in_image)
    self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg="#E6F0F3")
    self.sign_in_image_label.image = photo
    self.sign_in_image_label.pack(side="top", fill=tk.X, pady=30)

    # ========================================================================
    # ============================username====================================
    # ========================================================================

    self.username_label = Label(
        self.lgn_frame,
        text="Usuario",
        anchor="w",
        bg="#E6F0F3",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.username_label.pack(fill=tk.X, padx=25, pady=8)

    self.username_entry = Entry(
        self.lgn_frame,
        relief=FLAT,
        bg="#E6F0F3",
        font=("yu gothic ui ", 12, "bold"),
        insertbackground="#1E90FF",
    )
    self.username_entry.pack(fill=tk.X, padx=30, pady=0)
    
    self.username_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#1E90FF", highlightthickness=0
    )
    self.username_line.pack(fill=tk.X, padx=30, pady=1)

    # ========================================================================
    # ============================password====================================
    # ========================================================================
    self.password_label = Label(
        self.lgn_frame,
        text="Contraseña",
        anchor="w",
        bg="#E6F0F3",
        fg="#1E90FF",
        font=("yu gothic ui", 13, "bold"),
    )
    self.password_label.pack(fill=tk.X, padx=25, pady=8)

    self.password_entry = Entry(
        self.lgn_frame,
        relief=FLAT,
        bg="#E6F0F3",
        font=("yu gothic ui", 12, "bold"),
        show="*",
        insertbackground="#1E90FF",
    )
    self.password_entry.pack(fill=tk.X, padx=30, pady=0)

    self.password_line = Canvas(
        self.lgn_frame, width=300, height=2.0, bg="#1E90FF", highlightthickness=0
    )
    self.password_line.pack(fill=tk.X, padx=30, pady=1)

    # ========================================================================
    # ============================login button================================
    # ========================================================================
    self.login = Button(
        self.lgn_frame,
        text="Iniciar Sesion",
        font=("yu gothic ui", 13, "bold"),
        width=42,
        bd=0,
        bg="#1E90FF",
        cursor="hand2",
        activebackground="#3047ff",
        fg="white",
        command=lambda: Verificar(self=self, root=root),
    )
    self.login.pack(pady=35)
    self.login.bind("<Return>", (lambda event: Verificar()))
    # ========================================================================
    # ============================Forgot password=============================
    # ========================================================================
    self.forgot_button = Button(
        self.lgn_frame,
        text="Recuperar Acceso",
        font=("yu gothic ui", 13, "bold"),
        fg="#1E90FF",
        relief=FLAT,
        activebackground="#4169E1",
        borderwidth=0,
        background="#E6F0F3",
        cursor="hand2",
        command=lambda: Subventana(self=self),
    )

    self.forgot_button.pack(pady=2)

    # ========================================================================
    # ============================Info Tempus=================================
    # ========================================================================
    self.forgot_button = Button(
        self.lgn_frame,
        text="Version Beta 1",
        font=("yu gothic ui", 13, "bold"),
        fg="#1E90FF",
        relief=FLAT,
        activebackground="#4169E1",
        borderwidth=0,
        background="#E6F0F3",
        cursor="hand2",
        command=lambda: Info(self=self),
    )
    self.forgot_button.pack(pady=2)
