
from tkinter import *
from tkinter import messagebox as caja

class Aplicacion:
    def __init__(self):
        self.ven=Tk()
        self.ven.title("Objeto ListBox")
        self.ven.geometry("500x500+400+200")
        self.ven.resizable(0,0)
        self.ven.config(bg="plum1")
        self.ven.iconbitmap("C:/Users/INGENIERIA TECNICA/Downloads/python.ico")
        self.dato=StringVar()
        
        self.lista1=Listbox(self.ven, selectmode="EXTENDED", font=("arial", 14), bg="ivory3")
        self.lista1.place(x=50, y=100)

        self.label1=Label(self.ven, text="Insertar item: ")
        self.label1.config(font=("arial", 14),bg="plum1")
        self.label1.place(x=40, y=50)

        self.entry=Entry(self.ven, width=20, textvariable=self.dato,
                        state=NORMAL, justify=CENTER,
                        font=("arial", 14))
        self.entry.place(x=200, y=50)

        self.btn1=Button(self.ven, text="Ingresar Item",
                        command=self.ingreso,
                        font=("arial", 14),
                        width=15, bg="steelblue")
        self.btn1.place(x=300, y=100)

        self.btn2=Button(self.ven, text="Eliminar Item",
                        command=self.e_1,
                        font=("arial", 14),
                        width=15, bg="salmon")
        self.btn2.place(x=300, y=150)

        self.btn3=Button(self.ven, text="Eliminar Varios",
                        command=self.e_varios,
                        font=("arial", 14),
                        width=15, bg="salmon")
        self.btn3.place(x=300, y=200)

        self.btn4=Button(self.ven, text="Eliminar Todos",
                        command=self.e_todos,
                        font=("arial", 14),
                        width=15, bg="salmon")
        self.btn4.place(x=300, y=250)

        self.btn5=Button(self.ven, text="Ordenar Todos",
                        #command=self.ordenar,
                        font=("arial", 14),
                        width=15, bg="palegreen")
        self.btn5.place(x=300, y=300)

        self.label2=Label(self.ven, text="Cantidad de elementos")
        self.label2.config(font=("arial", 14),bg="plum1")
        self.label2.place(x=40, y=350)

        self.ven.mainloop()
        
    def ingreso(self):
        if self.dato.get()!="":
            self.lista1.insert(END, self.dato.get())
            self.dato.set("")
        else:
            caja.showerror("Título", "No ha ingresado ninguna cadena")
    
    def e_1(self):
        if len(self.lista1.curselection())!=0:
            self.lista1.delete(self.lista1.curselection()[0])
        else:
            caja.showerror("Título", "Debe seleccionar un elemento")
        self.label2.config(text=self.lista1.size())

    def e_varios(self):
        if len(self.lista1.curselection())!=0:
            tupla=self.lista1.curselection() #posicion de los elementos
            tupla2=tupla[::-1] #invertir tupla
        for x in(tupla2):
            self.lista1.delete(x)
        else:
            caja.showerror("Título", "Debe seleccionar los elementos")
        self.label2.config(text=self.lista1.size())
    def e_todos(self):
        self.lista1.delete(0,END)
        self.label2.config(text=self.lista1.size())
    #def ordenar(self):
        
app=Aplicacion()
