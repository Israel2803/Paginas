import tkinter as tk

class Aplicacion:
    def __init__(self):
        
        self.ventana1=tk.Tk()
        self.ventana1.geometry("500x400")
        self.ventana1.config(bg="steelblue")
        self.ventana1.iconbitmap("python.ico")
        
        #Definición de Variables
        self.seleccion1=tk.IntVar()  ## 1 y 0
        self.seleccion3=tk.IntVar()
        self.seleccion4=tk.IntVar()
        
        self.check1=tk.Checkbutton(self.ventana1,text="Chrome", variable=self.seleccion1, command=self.cambiartitulo,
                                   font=("calibri",24),offvalue=0, onvalue=1,
                                   bg="steelblue")
        self.check1.place(x=50, y=50)
        
        
        self.check2=tk.Checkbutton(self.ventana1,text="FireFox", variable=self.seleccion2, command=self.cambiartitulo,
                                   font=("calibri",24),
                                   bg="steelblue")
        self.check2.place(x=300, y=50)
        
        
        
        self.check3=tk.Checkbutton(self.ventana1,text="Edge", variable=self.seleccion3, command=self.cambiartitulo,
                                   font=("calibri",24),
                                   bg="steelblue")
        self.check3.place(x=50, y=200)
        
        
        self.check4=tk.Checkbutton(self.ventana1,text="Opera", variable=self.seleccion4, command=self.cambiartitulo,
                                   font=("calibri",24),
                                   bg="steelblue")
        self.check4.place(x=300, y=200)
        
        
        
        self.ventana1.mainloop()
        
        
    #Desarrollo del Procedimiento
    def cambiartitulo(self):
        cadena=""
        if self.seleccion1.get()==1:   #Obtener un valor del objeto variable  ( 1 // 0)
            cadena+="Chrome - "
        if self.seleccion2.get()==1:
            cadena+="Firefox - "
        if self.seleccion3.get()==1:
            cadena+="Edge - "
        if self.seleccion4.get()==1:
            cadena+="Opera"
        self.ventana1.title(cadena)
app=Aplicacion()












