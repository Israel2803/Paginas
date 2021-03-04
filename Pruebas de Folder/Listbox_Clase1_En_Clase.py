"""
Listbox en Python
"""
from tkinter import *
from tkinter import messagebox as caja

class Aplicacion:
    def __init__(self):
        self.ven=Tk()
        self.ven.title("Objeto Listbox")
        self.ven.geometry("500x500")
        
        #Creación del objeto Listbox
        self.lista1=Listbox(self.ven, selectmode=MULTIPLE)
        self.lista1.place(x=100, y=100)
        
        #Agregar elementos al Listbox
        self.lista1.insert(0,"Python")
        self.lista1.insert(1,"Visual Basic")
        self.lista1.insert(2,"C++")
        self.lista1.insert(3,"Java")
        self.lista1.insert(4,"C#")
        self.lista1.insert(5,"C")
        
        #Crear Label para la impresión 
        self.label1=Label(self.ven,text="Respuesta")
        self.label1.place(x=100,y=300)
        
        #Crear Botón
        self.boton1=Button(self.ven, text="Seleccionar",
                           command=self.Proceboton)
        self.boton1.place(x=300,y=100) 
        
        self.ven.mainloop()
        
    def Proceboton(self):
        var=self.lista1.curselection()
        print(var)
        if len(self.lista1.curselection())!=0:
            self.label1.config(text=self.lista1.get(self.lista1.curselection()[0]))
        else:
            caja.showerror("Título", "No ha seleccionado ningún elemento")
     
app=Aplicacion()

