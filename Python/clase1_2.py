
montocompra=montodesc=montopag=obsequio=0
docenas=int(input("Cantidad de docenas a comprar:"))
precio=int(input("Precio por docena:"))
montocompra=docenas*precio
if docenas>3:
    montodesc=montocompra*0.15
    obsequio=docenas-3
else:
    montodesc=montocompra*0.10
    obsequio=0
montopag=montocompra-montodesc
print("Monto de Compra: L.", montocompra)
print("Monto de Descuento: L.", montodesc)
print("Monto a pagar: L.", montopag)
print("Cantidad de unidades en obsequio: Uni ", obsequio)

