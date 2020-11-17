def digito_verificador(rut):
    cont=0
    suma=0
    while rut>0:
        unidad=rut%10
        suma+=unidad*(2+(cont%6))
        rut=rut//10
        cont=cont+1
    d=suma%11
    d=11-d
    if d==10:
        return 'k'
    elif d==11:
        return '0'
    return str(d)

def estado_cuenta(meta, actual):
    if meta>actual:
        return('Faltan $'+str(meta-actual)+' Vamos chilenos!!')
    else:
        return('Logramos la meta, que venga la modelo!!')

maximo=-float('inf')
mayor_donador=''
meta=int(input('Cual sera la meta de esta TePyTon?: '))
total=0
dias=int(input('Ingrese la cantidad de dias de la TePyTon: '))
dia_actual=1
print('')
print('Opcion 1. Ingresar nueva donacion')
print('Opcion 2. Estado de cuentas') 
print('Opcion 3. Mayor donacion')
print('Opcion 4. Avanzar al siguiente dia')
while dia_actual<=dias:
    print('DIA',dia_actual)
    print('Meta:',meta)
    print('Llevamos:',total)

    mayor_donador_del_dia = ''
    maximo_del_dia = 0
    operacion=input('Ingrese operacion: ')
    
    while operacion!='4':
        if operacion=='1':
            rut=input('Ingrese rut (sin digito verificador): ')
            dv=input('Ingrese digito verificador: ')
            if digito_verificador(int(rut))==dv:
                donacion=int(input('Ingrese donacion: $'))
                total+=donacion
                if donacion>maximo_del_dia:
                    maximo_del_dia=donacion
                    mayor_donador_del_dia=rut+'-'+dv
                if donacion>maximo:
                    maximo=donacion
                    mayor_donador=rut+'-'+dv
            else:
                print('Rut invalido')
        elif operacion=='2':
            print(estado_cuenta(meta,total))
        elif operacion=='3':
            if mayor_donador == '':
                print('Aun nadie ha demostrado ser caritativo en este pais')
            elif mayor_donador_del_dia == '':
                mensaje_mostrar = 'No se han registrado donaciones el dia de hoy'
                mensaje_mostrar += 'pero felicitamos a '+mayor_donador+''
                print('No se han registrado donaciones el dia de hoy, pero felicitamos a ',mayor_donador,'pro su generoso aporte de ',maximo,' el otro dia')
            else:
                print('Felicitamos al RUT',mayor_donador_del_dia,'por su generosa donacion de ',maximo_del_dia,'y al rut',mayor_donador,'ha realizado un generoso aporte maximo de',maximo)
        elif operacion=='4':
            dia_actual+=1
        else:
            print('Opcion invalida')
        operacion=input('Ingrese operacion: ')
