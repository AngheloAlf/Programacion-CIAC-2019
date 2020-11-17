def impuesto(monto, tipo):
    if tipo=='empresa':
        factor=0.27
    else:
        if monto<664592:
            factor=0
        elif monto<1476871:
            factor=0.04
        elif monto<2461451:
            factor=0.08
        elif monto<3446031:
            factor=0.135
        elif monto<4430611:
            factor=0.23
        elif monto<5907481:
            factor=0.304
        else:
            factor=0.35
    return monto*factor

total=0
tipo=input('Ingrese tipo de entidad: ')
while tipo!='':
    renta=int(input('Ingrese renta liquida: '))
    suma=impuesto(renta,tipo)
    total+=suma
    tipo=input('Ingrese tipo de entidad: ')
print('El total recaudado fue',total)
    
