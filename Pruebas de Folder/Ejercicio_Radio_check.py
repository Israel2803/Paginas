"""
Radiobuttons 
Checkbuttons
Button
Label
"""

from tkinter import*
from tkinter import messagebox as caja

class Aplicacion:
    def __init__(self):
        self.ven=Tk()
        self.ven.title("Botones de Verificación")
        self.ven.geometry("550x550")
        
        #Definición de ObjetoVariable Radiobutton
        self.rbo1=IntVar()
        self.rbo1.set(0)        

        #Definición de ObjetoVariable Checkbutton
        self.cbo1=IntVar() #1 y 0
                
        
        #marcos
        self.frame=LabelFrame(self.ven,text="Lenguajes de Programación")
        self.frame.config(bg="lightblue",
                          font=("arial",14))
        self.frame.config(width=400,height=190)  
        self.frame.place(x=70,y=50)  
        
      
        #radiobutton
        self.rb1=Radiobutton(self.frame,text="Python",variable=self.rbo1,
                        value=1,
                        font=("arial",14),
                        bg="lightblue")
        self.rb1.place(x=40,y=30)
        
        self.rb2=Radiobutton(self.frame,text="Visual Basic",variable=self.rbo1,
                        value=2,
                        font=("arial",14),
                        bg="lightblue")
        self.rb2.place(x=210,y=30)
        
        self.rb3=Radiobutton(self.frame,text="Java",variable=self.rbo1,
                        value=3,
                        font=("arial",14),
                        bg="lightblue")
        self.rb3.place(x=40,y=100)
        
        self.rb4=Radiobutton(self.frame,text="C++",variable=self.rbo1,
                        value=4,
                        font=("arial",14),
                        bg="lightblue")
        self.rb4.place(x=210,y=100)
        
        
        #checkbutton
        self.cb1=Checkbutton(self.ven,text="Aceptar los términos",
                        variable=self.cbo1, onvalue=1, offvalue=0,
                        font=("arial",14)).place(x=65,y=250)
        
        
        #buttons
        self.btn1=Button(self.ven,text="Aceptar", command=self.operaciones,
                    font=("arial",14),
                    width=10).place(x=350,y=300)
        
        #Etiquetas
        self.lbl1=Label(self.ven,text="respuesta...")
        self.lbl1.config(font=("comic sams ms", 15, "bold"))
        
        self.lbl1.place(x=60, y=400)
        
        
        self.ven.mainloop()

    def operaciones(self):
        self.cade=""
        if self.cbo1.get()==1:
            
            if self.rbo1.get()==1:
                cade="Ha seleccionado Python"
            
            elif self.rbo1.get()==2:
                cade="Ha seleccionado Visual Basic"
            elif self.rbo1.get()==3:
                cade="Ha seleccionado Java"
            elif self.rbo1.get()==4:
                cade="Ha seleccionado C++"
            else:
                cade="No ha seleccionado ningún lenguaje"
            self.lbl1.config(text=cade)
            print(cade)
        else:
            caja.showerror("Título", "No ha aceptado los términos")
       
       
            
app=Aplicacion() 

