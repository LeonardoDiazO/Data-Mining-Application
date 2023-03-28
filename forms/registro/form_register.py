from forms.registro.form_designer import formRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.modelos import Auth_User
from tkinter import messagebox
import util.enconding_decoding as end_dec
import tkinter as tK

class FormRegister (formRegisterDesigner):
    def __init__(self) -> None:
        self.auth_user_repository = AuthUserRepository()
        super().__init__()
        
    def register(self):
        if(self.isConfirPassword()):
            user = Auth_User()
            user.username= self.usuario.get()
            user_db:Auth_User= self.auth_user_repository.getUserByUserName(self.usuario.get())
            if not(self.isUserRegister(user_db)):
                user.password = end_dec.encrypter(self.password.get())
                self.auth_user_repository.insertUser(user)
                messagebox.showinfo(message="Se registro el usuario", title= "Mensaje")
                self.ventana.destroy()
    
    def isConfirPassword(self):
        status: bool = True
        if (self.password.get() != self.confirmation.get()):
            status=False
            messagebox.showerror(message="La contraseña no coinciden por favor verificar el registro", title="Mensaje")
            self.password.delete(0,tK.END)
            self.confirmation.delete(0, tK.END)
        return status
    def isUserRegister(self,user:Auth_User):
        status: bool = False
        if (user != None):
            status=True
            messagebox.showerror(message="El usuario ya existe", title="Mensaje")
        return status