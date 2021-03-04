high=int(input("Ingresar la altura de la persona(cm): "))
if high<150:
    print("persona de altura baja")
else:
    if high<=170:
        print("Persona de altura media")
    else:
        if high<=195:
            print("Persona de altura alta")
        else:
            print("No exagere con la altura")

if high<150:
    print("persona de altura baja")
else:
    if high>150 and high<=170:
        print("Persona de altura media")
    else:
        if high>170 and high<=195:
            print("Persona de altura alta")
        else:
            print("No exagere con la altura")