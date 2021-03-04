num1=int(input("Ingrese un primer numero:"))
num2=int(input("Ingrese un segundo numero:"))
num3=int(input("Ingrese un tercer numero:"))
sum1=num1+num2
sum2=num1+num3
sum3=num2+num3
if sum1==num3:
    print("Iguales")
elif sum2==num2:
    print("Iguales")
elif sum3==num1:
    print("Iguales")
else:
    print("Distintos")