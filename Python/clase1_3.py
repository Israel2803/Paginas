
nota1=int(input("Nota 1: "))
nota2=int(input("Nota 2: "))
nota3=int(input("Nota 3: "))
prom=(nota1+nota2+nota3)/3
if prom>7:
    print("Alumno ha sido promovido")
elif prom>=4:
    print("Alumno con nota regular")
else:
    print("Alumno ha reprobado")
