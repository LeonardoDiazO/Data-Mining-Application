import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import formLoginDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.modelos import Auth_User
import util.enconding_decoding as end_dec

#Clase heredada que es de FormLoginDesigner
class FormLogin(formLoginDesigner):
    
    def __init__(self) -> None:
        self.auth_user_repository = AuthUserRepository()
        super().__init__()
    
    #Inicializacion 
    # def __init__(self) -> None:
    #     self.auth_repository = AuthUserRepository()
    #     super().__init__
    
    #Metodo Validacion de la contraseña y password
    def verificar(self):
        user_db: Auth_User = self.auth_user_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)
        
    
    #Metodo para verificar si es usuario
    def isUser(self,user:Auth_User):
        status:bool = True
        if(user == None):
            status = False
            messagebox.showerror(
            message="El ususario no existe por favor resitrarse", title="Mensaje")
        return status


    #Metodo para verificar si es la contraseña
    def isPassword(self,password:str,user:Auth_User):
        b_password = end_dec.descrypt(user.password)
        if(password == b_password):
            self.ventana.destroy
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")
           
     