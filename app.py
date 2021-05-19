#CONSTRUIR INTERFAZ

#Importar librerías
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

####################################################
#Crear ventanas de aplicación

#ventana root
root = Tk()
root.title("Database App")
root.iconbitmap("icon.ico")
root.geometry("1000x600")



#Root - Crear textbox input
f_name = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=0, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=0, padx=30)

city = Entry(root, width=30)
city.grid(row=3, column=0, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=0, padx=20)

zip = Entry(root, width=30)
zip.grid(row=5, column=0, padx=20)

#Root - Crear etiquetas



#####################################################
#DATABASE

#Crear base de datos y conectarse (se corre solo una vez)
conn = sqlite3.connect("db1.db")

#Crear un cursor
c = conn.cursor()


#CREAR TABLA

'''
c.execute("""CREATE TABLE adresses (first_name text, 
last_name text,
adress text,
city text,
state text,
zip text ) """)
'''








#Enviar cambios realizados a la base de datos
conn.commit()

#Cerrar la conexión
conn.close()

#####################################################
root.mainloop()
