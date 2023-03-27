import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import formLoginDesigner

#Clase heredada que es de FormLoginDesigner
class FormLogin(formLoginDesigner):
    
    #Metodo Validacion de la contraseña y password
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password== "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="la contraseña no es correcta", title="Mensaje")
    
    
    
    def __init__(self) -> None:
        super().__init__()