import tkinter as tk 
from tkinter import messagebox
from modulo_cripto import obtener_clave
from modulo_db import Database
import random
import string
from cryptography.fernet import Fernet

class Aplicacion:
    def __init__(self,master):
        self.root=master
        self.root.title("Almacenamientos de usuarios y contraseñas")
        self.root.geometry("400x300")
        self.db=Database("mi_base_datos.db")
        self.clave_encriptacion = obtener_clave()
        #self.cipher_suite = Fernet(self.clave_encriptacion)
    #etiquetas y cajas de textos
        lbl_id=tk.Label(self.root,text="ID:")
        lbl_id.grid(row=0,column=0)
        self.entry_id=tk.Entry(self.root)
        self.entry_id.grid(row=0,column=1)

        lbl_url=tk.Label(self.root,text="URL:")
        lbl_url.grid(row=1,column=0)
        self.entry_url=tk.Entry(self.root)
        self.entry_url.grid(row=1,column=1)

        lbl_usuario=tk.Label(self.root,text="Usuario:")
        lbl_usuario.grid(row=2,column=0)
        self.entry_usuario=tk.Entry(self.root)
        self.entry_usuario.grid(row=2,column=1)

        lbl_clave=tk.Label(self.root,text="Clave:")
        lbl_clave.grid(row=3,column=0)
        self.entry_clave=tk.Entry(self.root)
        self.entry_clave.grid(row=3,column=1)

        lbl_nota=tk.Label(self.root,text="Nota:")
        lbl_nota.grid(row=4,column=0)
        self.entry_nota=tk.Entry(self.root)
        self.entry_nota.grid(row=4,column=1)
    #botones
        btn_grabar=tk.Button(self.root,text="Grabar",command=self.grabar_registro)
        btn_grabar.grid(row=5,column=0)
        btn_actualizar=tk.Button(self.root,text="Actualizar",command=self.actualizar_registro)   
        btn_actualizar.grid(row=5,column=1)
        btn_borrar=tk.Button(self.root,text="Borrar",command=self.borrar_registro)
        btn_borrar.grid(row=6,column=0)
        btn_buscar=tk.Button(self.root,text="Buscar",command=self.buscar_por_id)
        btn_buscar.grid(row=6,column=1)
        btn_generar=tk.Button(self.root,text="Generar Contraseña",command=self.generar_contraseña)
        btn_generar.grid(row=7,column=0,columnspan=2)

    def grabar_registro(self):
        url=self.entry_url.get()
        usuario=self.entry_usuario.get()
        clave=self.entry_clave.get()
        nota=self.entry_nota.get()
        if url and usuario and clave:
            self.db.insertar_registro(url,usuario,clave,nota)
            messagebox.showinfo("Éxito","Registro guardado correctamente")
            self.limpiar_campos()
        else :
            messagebox.showwarning("Error","Por favor complete todos los campos obligatorios")
    def actualizar_registro(self):
        id=self.entry_id.get()
        url=self.entry_url.get()
        usuario=self.entry_usuario.get()
        clave=self.entry_clave.get()
        nota=self.entry_nota.get()
        if id and url and usuario and clave:
            self.db.actualizar_registro(id,url,usuario,clave,nota)
            messagebox.showinfo("Éxito","Registro actualizado correctamente")
        else :
            messagebox.showerror("Error","Por favor complete todos los campos obligatorios")
    def borrar_registro(self):
        id=self.entry_id.get()
        if id: 
            self.db.borrar_registro(id)
            messagebox.showinfo("Éxito","Registro borrado correctamente")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error","Por favor ingrese un ID válido")
    def buscar_por_id(self):
        id=self.entry_id.get()
        if id:
            resultado=self.db.buscar_registro(id)
            if resultado:
                self.limpiar_campos()
                self.entry_url.insert(0,resultado[1])
                self.entry_usuario.insert(0,resultado[2])
                clave_desencriptada =self.db.desencriptar(resultado[3])
                self.entry_clave.insert(0,clave_desencriptada)
                self.entry_nota.insert(0,resultado[4])
            else:
                messagebox.showerror("Error","Registro no encontrado")
        else:
            messagebox.showerror("Error","Por favor ingrese un ID válido")

    def limpiar_campos(self):
        #self.entry_id.delete(0,tk.END)
        self.entry_url.delete(0,tk.END)
        self.entry_usuario.delete(0,tk.END)
        self.entry_clave.delete(0,tk.END)
        self.entry_nota.delete(0,tk.END)
    
    def generar_contraseña(self):
        longitud=12
        caracteres=string.ascii_letters + string.digits + string.punctuation
        contraseña=''.join(random.choice(caracteres)for i in range(longitud))
        self.entry_clave.delete(0,tk.END)
        self.entry_clave.insert(0,contraseña)
    
