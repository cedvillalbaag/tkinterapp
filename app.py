#CONSTRUIR INTERFAZ

#Importar librerías
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

####################################################
#Crear ventanas de aplicación

#Ventana root
root = Tk()
root.title("Database App")
root.iconbitmap("icon.ico")
root.geometry("400x400")






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

#Crear función para insertar a DB
def submit():
    #Connect database
    conn = sqlite3.connect("db1.db")
    #create cursor
    c = conn.cursor()

    #Insertar a tabla
    c.execute("INSERT INTO  adresses VALUES (:f_name, :l_name, :address, :city, :state, :zip)", 
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zip':zip.get(),

    }
    )

    #Commit changes
    conn.commit()

    #Cerrar conexion base datos
    conn.close()


    #Limpiar contenido de inputs
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip.delete(0,END)
    return


#Crear funcion consulta
def query():
    '''c.execute("SELECT *, FROM adresses
    ")'''
    return

'''
    #Commit changes
    conn.commit()

    #Cerrar conexion base datos
    conn.close()'''

############################################################

#Enviar cambios realizados a la base de datos
conn.commit()

#Cerrar la conexión
conn.close()


############################################################
#Ventana Root - Crear textbox input

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zip = Entry(root, width=30)
zip.grid(row=5, column=1)


#Ventana Root - Crear etiquetas
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0 )


l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0 )

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0 )

city_label = Label(root, text="City")
city_label.grid(row=3, column=0 )

state_label = Label(root, text="State")
state_label.grid(row=4, column=0 )

zip_label = Label(root, text="Zip")
zip_label.grid(row=5, column=0 )

# Ventana Root - Crear botones
#Boton Enviar
submit_btn = Button(root, text="Add record to Database", command=submit) 
submit_btn.grid(row=6, column=0, columnspan = 2, pady = 10, padx= 10, ipadx = 100)


#Boton Imprimir en Ventana - Query Boton
query_btn = Button(root, text="Show Records", command=query) 
query_btn.grid(row=11, column=0, columnspan = 2, pady = 10, padx= 10, ipadx = 100)


#####################################################
root.mainloop()
