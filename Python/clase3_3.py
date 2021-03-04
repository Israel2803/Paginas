
num1=num2=contar=0
num1=int(input("Ingresar num uno: "))
num2=int(input("Ingresar num dos: "))
if num1<num2:
    while num1<=num2:
        if num1%2==0:
            print(num1," ")
            num1=num1+1
else:
    print("Los números esta desordenados")
