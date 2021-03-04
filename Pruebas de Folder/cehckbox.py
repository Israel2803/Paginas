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

        self.chbut1=Checkbutton(self.ven,text="Python", variable=self.var1, command=self.x1, onvalue=1, offvalue=0, font=("Caveat Brush", 14, "bold"),bg="skyblue",fg="darkslategrey",justify="center", activebackground="gray")
        self.chbut1.place(x=300,y=50)


        self.ven.mainloop()
app=Aplicacion()