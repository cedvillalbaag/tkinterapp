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
#OPERACIONES EN DATABASE

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



#Crear función de actualizar registro
def edit():
    #Crear ventana edición
    #Ventana edición
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap("icon.ico")
    editor.geometry("400x400")


    #Connect database
    conn = sqlite3.connect("db1.db")
    #create cursor
    c = conn.cursor()

    
    #Instruccion SQL
    record_id = delete_box.get()

    c.execute("SELECT * FROM adresses WHERE oid = "+ record_id)
    records = c.fetchall()

    


    #Ventana Editor - Crear textbox input

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady = (20,0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zip_editor = Entry(editor, width=30)
    zip_editor.grid(row=5, column=1)

    #Ventana Editor - Crear etiquetas
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, padx = 10, pady = (20,0) )


    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0 )

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0 )

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0 )

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0 )

    zip_label_editor = Label(editor, text="Zip")
    zip_label_editor.grid(row=5, column=0 )


    #Loop thru result
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_editor.insert(0, record[5])


    #Create a Save Button to save edited record
    edit_btn = Button(editor, text="Save Record", command=edit) 
    edit_btn.grid(row=6, column=0, columnspan = 2, pady = 10, padx= 10, ipadx=145)

    #Commit changes
    conn.commit()

    #Cerrar conexion base datos
    conn.close()



#Create function to delete a record
def delete():
    #Connect database
    conn = sqlite3.connect("db1.db")
    #create cursor
    c = conn.cursor()

    #Instruccion SQL
    #c.execute("DELETE FROM adresses WHERE oid= PLACEHOLDER")
    c.execute("DELETE FROM adresses WHERE oid = " + delete_box.get())
    
    
    
    #Borrar campo
    delete_box.delete(0,END)

    #Commit changes
    conn.commit()

    #Cerrar conexion base datos
    conn.close()






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
    #Connect database
    conn = sqlite3.connect("db1.db")
    #create cursor
    c = conn.cursor()

    #Instruccion SQL
    c.execute("SELECT *, oid FROM adresses")
    records = c.fetchall()  #fetchone / fetchmany(50)
    #print(records)

    #Loop thru result
    print_records=""
    for record in records:
        print_records += str(record[1]) + " " + str(record[2]) + " " + str(record[3]) +  " " + str(record[6]) +"\n"
       # print_records += str(record[0]) + " " + str(record[1]) +  " " + str(record[3]) + " " + str(record[4] + "\n"

    query_label = Label(root, text= print_records)
    query_label.grid(row=8, column= 0, columnspan=2)
    return


    #Commit changes
    conn.commit()

    #Cerrar conexion base datos
    conn.close()






############################################################

#Enviar cambios realizados a la base de datos
conn.commit()

#Cerrar la conexión
conn.close()


############################################################
#Ventana Root - Crear textbox input

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady = (20,0))

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

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady= 5)







#Ventana Root - Crear etiquetas
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx = 10, pady = (20,0) )


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

delete_label = Label(root, text= "Select ID", pady = 5)
delete_label.grid(row=9, column=0)

# Ventana Root - Crear botones
#Boton Enviar
submit_btn = Button(root, text="Add record to Database", command=submit) 
submit_btn.grid(row=6, column=0, columnspan = 2, pady = (20,5), padx= 10, ipadx=100)


#Boton Query
query_btn = Button(root, text="Show Records", command=query) 
query_btn.grid(row=7, column=0, columnspan = 2, pady = 10, padx= 10, ipadx= 125)

#Boton Delete
delete_btn = Button(root, text="Delete Record", command=delete) 
delete_btn.grid(row=10, column=0, columnspan = 2, pady = 10, padx= 10, ipadx=125)

#Boton Edit
edit_btn = Button(root, text="Edit Record", command=edit) 
edit_btn.grid(row=11, column=0, columnspan = 2, pady = 10, padx= 10, ipadx=131)


#####################################################
root.mainloop()
