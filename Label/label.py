from tkinter import*

class Aplicacion:
    def __init__(self):
        self.ven=Tk()
        self.ven.title("Ejemplo 3 de Interfaces")
        self.ven.geometry("800x500+200+100")
        self.ven.resizable(0,0)
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.x1=IntVar()
        self.x2=IntVar()
        self.x3=IntVar()

        self.chbut1=Checkbutton(self.ven,text="Python", variable=self.var1, command=self.x1, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chbut1.place(x=300,y=50)

        self.chbut2=Checkbutton(self.ven,text="CSS", variable=self.var2, command=self.x1, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chbut2.place(x=300,y=200)
        
        self.chbut3=Checkbutton(self.ven,text="JavaScript", variable=self.var3, command=self.x1, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chbut3.place(x=300,y=350)

        self.etiqueta=Label(self.ven, text="Etiquetas")
        self.etiqueta.config(font=("Caveat Brush", 14, "bold","italic","underline"),
        width=20,height=5,
        bg="skyblue",fg="darkslategrey")
        self.etiqueta.place(x=50, y=50)

        self.etiqueta2=Label(self.ven, text="Otras Formas")
        self.etiqueta2.config(font=("Caveat Brush", 14, "bold","italic","underline"),
        width=20,height=5,
        bg="darkslategrey",fg="skyblue")
        self.etiqueta2.place(x=50, y=200)

        #imagCb=PhotoImage(file="js.png")
        #image=imagCb,
        #imaCb=PhotoImage(file="js.png", width=50, height=20)
        #self.etiqueta3=Label(self.ven,image=imaCb)
        #self.ven.place(x=50, y=350)
        
        def x1(self):
            if self.var1.get()==1:
                print("Elegiste boton 1")
            else:
                print("No elegiste boton 1")
        def x2(self):
            if self.var2.get()==1:
                print("Elegiste boton 2")
            else:
                print("No elegiste boton 2")
        def x3(self):
            if self.var3.get()==1:
                print("Elegiste boton 3")
            else:
                print("No elegiste boton 3")
                
        self.ven.mainloop()    
app=Aplicacion()