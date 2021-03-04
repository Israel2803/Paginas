minutos=int(input("Ingresar tiempo transcurrido en el estacionamiento(en min):"))
a=minutos%60
b=(a*60)-minutos
if b!=0:
    a=a+1
    cobrar=a*10
else:
    cobrar=a*10
print("Debe cobrar: ", cobrar)

