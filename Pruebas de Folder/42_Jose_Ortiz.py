from tkinter import *
from tkinter import messagebox as caja

class Aplicacion:
    def __init__(self):
        self.ven=Tk()
        self.ven.title("Navegador Web")
        self.ven.geometry("600x400+300+200")
        self.ven.resizable(0,0)
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        """
        self.lista=Listbox(self.ven,selectmode=MULTIPLE)
        self.lista.place(x=100, y=100)

        self.lista.insert(0,"Python")
        self.lista.insert(1,"Visual")
        self.lista.insert(2,"C++")
        self.lista.insert(3,"Java")
        self.lista.insert(4,"C#")
        self.lista.insert(5,"C")

        self.label1=Label(self.ven, text="respuesta")
        self.label1.place(x=100, y=300)

        self.boton1=Button(self.ven, text="Seleccionar", command=self.boton)
        self.boton1.place(x=300, y=100)

        def boton(self):
            if len(self.lista.curselection())!==0:
                self.label1.config(text=self.lista.get(self.lista.curselection()[0]))
            else:
                caja.showerror("T","No selecciono el ultimo elemento")

        """

        self.chebut1=Checkbutton(self.ven,text="Chrome", variable=self.var1, command=self.Cambiar, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chebut1.place(x=50,y=50)

        self.chebut2=Checkbutton(self.ven,text="FireFox", variable=self.var2, command=self.Cambiar, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chebut2.place(x=200,y=50)

        self.chebut3=Checkbutton(self.ven,text="Opera", variable=self.var3, command=self.Cambiar, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chebut3.place(x=50,y=200)

        self.chebut4=Checkbutton(self.ven,text="MicrosoftEdge", variable=self.var4, command=self.Cambiar, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chebut4.place(x=200,y=200)
        
        self.ven.mainloop()
    def Cambiar(self):
        cadena=""
        if self.var1.get()==1:
            cadena=cadena+"Chrome "
        if self.var2.get()==1:
            cadena=cadena+"FireFox "
        if self.var3.get()==1:
            cadena=cadena+"Opera "
        if self.var4.get()==1:
            cadena=cadena+"MicrosoftEdge "
        
        self.ven.title(cadena)
        
        
app=Aplicacion()