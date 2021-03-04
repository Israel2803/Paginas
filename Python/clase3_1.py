
nota=int(input("ingrese nota -1_salir: "))
total=contar=0
while nota!=-1:
    total=total+nota
    contar=contar+1
    nota=int(input("ingrese nota-1_salir: "))
promedio=total/contar
print("Promedio: ", promedio)

