
num1=num2=op=0
inicio=True
while inicio==True:
    print("Opciones")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    op=int(input("Seleccione una de las opciones de la lista(1-5): "))
    if op==5:
        inicio=False
        print("Hasta la vista BABY")
    else:
        num1=int(input("Ingresar num uno: "))
        num2=int(input("Ingresar num dos: "))
        if op==1:
            print("Suma, el resultado es: ", num1+num2)
            print("\n")
        else:
            if op==2:
                print("Resta, el resultado es: ", num1-num2)
                print("\n")
            else:
                if op==3:
                    print("Multiplicar, el resultado es: ", num1*num2)
                    print("\n")
                else:
                    if op==4:
                        print("Dividir, el resultado es: ", num1/num2)
                        print("\n")
    