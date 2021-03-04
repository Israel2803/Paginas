"""
CheckBox
El widget de botón de verificación se utiliza para mostrar una serie de opciones 
a un usuario como botones de alternancia. El usuario puede entonces seleccionar 
una o más opciones haciendo clic en el botón correspondiente a cada opción.

También puede mostrar imágenes en lugar de texto.

Sintaxis:
nombre_control = Checkbutton(root, option, ... )
"""

from tkinter import*

class Aplicacion:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Botones de Verificación (Checkbutton)")
        self.ventana.geometry("800x800+250+150")
        
        #Definir variables 
        self.var1=IntVar()#1 activado, 0 desactivado
        self.var2=IntVar()
                
        #Crear Checkbutton
        cb1=Checkbutton(self.ventana,text="Python",
                        variable=self.var1,onvalue=1,offvalue=0, command=self.x1,
                        font=("arial",20,"bold","italic","underline"),
                        bg="blue", fg="red",
                        justify=CENTER,
                        state=NORMAL) #DISABLED)
        cb1.place(x=50,y=100)
        
        
        imagCb=PhotoImage(file="sol.png") #Crear o definir el objeto imagen, dentro de la carpeta.
        cb2=Checkbutton(self.ventana,image=imagCb,
                        variable=self.var2,onvalue=1,offvalue=0,command=self.x2,
                        selectcolor="red", activebackground="yellow")
        cb2.place(x=400, y=100)
        
        self.ventana.mainloop()
        
    def x1(self):
        if self.var1.get()==1:
            print("Has elegido botón 1")
        else:
            print("No has elegido botón 1")
            
    def x2(self):
        if self.var2.get()==1:
            print("Has elegido botón de Homero")
        else:
            print("No has elegido botón de Homero")

app=Aplicacion()


                         
