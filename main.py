from tkinter import Tk
from modulo_visual import Aplicacion
from modulo_db import Database
from modulo_cripto import obtener_clave

def main():
    root=Tk()
    #root.title("Almacenamientos de usuarios y contraseñas")
    app=Aplicacion(root)
    root.mainloop()

if __name__=="__main__":
    db = Database("mi_base_datos.db")
    db.crear_tabla()
    main()
    db.cerrar_conexion()