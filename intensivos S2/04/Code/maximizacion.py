maximo=-float('inf')
persona=input('Ingrese nombre del donador: ')
while persona!='':
    monto=int(input('Ingrese donacion: '))
    if monto>maximo:
        maximo=monto
        mejor=persona
    persona=input('Ingrese nombre del donador (enter para salir): ')
print('La donacion mas alta fue de',maximo,'realizada por',mejor)
