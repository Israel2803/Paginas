num=0
num=int(input("Ingrese un número de uno o dos dígitos:"))
if num<0:
    print("Número negativo")
elif num==0:
    print("Número cero")
else:
    print("Positivo")
    if num<10:
        print("Número de un dígito")
    elif num<100:
        print("Número de dos dígitos")
    else:
        print("Número mayor a 2 dígitos")
