cont_miguel=0
cont_anghelo=0
print('1. Ingresar venta')
print('2. Mejor vendedor')
print('3. Resumen diario')
print('4. Salir')
print('')
op=input('Ingrese opcion: ')
while op!='4':
    if op=='1':
        vendedor=input('Ingrese nombre vendedor [Miguel/Anghelo]: ')
        venta=int(input('Ingrese monto vendido: '))
        if vendedor=='Miguel':
            cont_miguel+=venta
        elif vendedor=='Anghelo':
            cont_anghelo+=venta
    elif op=='2':
        if cont_miguel>cont_anghelo:
            print('El mejor vendedor es Miguel, que ha vendido $'+str(cont_miguel))
        else:
            print('El mejor vendedor es Anghelo, que ha vendido $'+str(cont_anghelo))
    elif op=='3':
        print('Hoy se han vendido $'+str(cont_miguel+cont_anghelo))
        print('Buenas noches!')
        cont_miguel=0
        cont_anghelo=0
    op=input('Ingrese opcion: ')
        
