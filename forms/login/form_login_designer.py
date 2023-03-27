import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl


class formLoginDesigner:
    
    
    def verificar(self):
        pass
    
    def userRegister(self):
        pass
    
    
    
    def __init__(self) -> None:
        self.ventana= tk.Tk()
        self.ventana.title('INICIO DE SESSION')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#ABEBC6')
        self.ventana.resizable(width=0,height=0)
        utl.centrar_ventana(self.ventana,800,500)
        

        
        logo =utl.leer_imagen("./imagenes/logotransparente.png",(200,200))
        
        # framer_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#7DCEA0')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH )
        label = tk.Label(frame_logo, image=logo,bg='#7DCEA0')
        label.place(x=0,y=0,relwidth=1,relheight=1)
        
         # framer_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES,fill=tk.BOTH)
        # frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height=50, bd=0,relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title= tk.Label(frame_form_top, text="Inicio de sesion", font=('Times',30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #frame_form_top
        
        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height=50,bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES,fill=tk.BOTH)
        
        # #etiqueta_usuario
        etiqueta_usuario = tk.Label(frame_form_fill, text="USUARIO", font=('Times',14),fg="#666a88",bg='#fcfcfc',anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill,font=('Times',14))
        self.usuario.pack(fill=tk.X,padx=20,pady=10)
        
        
        # #etiqueta_password
        etiqueta_password = tk.Label(frame_form_fill, text="PASSWORD", font=('Times',14),fg="#666a88",bg='#fcfcfc',anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill,font=('Times',14))
        self.password.pack(fill=tk.X,padx=20,pady=10)
        self.password.config(show="*")
        
        
        #boton de inicio
        inicio=tk.Button(frame_form_fill,text="Iniciar Sesion", font=('Times',15,BOLD),bg='#7DCEA0',bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        inicio.bind("<Return>",(lambda event:self.verificar()))
        
        #boton de registro
        inicio=tk.Button(frame_form_fill,text="Registro de usuario", font=('Times',15,BOLD),bg='#ABEBC6',bd=0,fg="#1D8348",command=self.userRegister)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        inicio.bind("<Return>",(lambda event:self.userRegister()))
        
        
        self.ventana.mainloop()