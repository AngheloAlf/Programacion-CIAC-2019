def listaPaises(animales):
    lista=[]
    for _,_,_,correo in animales:
        tld=correo.split('.')[-1]
        lista.append( paises[tld] )
    return lista
def animalMasJoven(animales):
    mayor_fecha=(0,0,0)
    jovencito=''
    for nombre,_,fecha,_ in animales:
        if fecha>mayor_fecha:
            mayor_fecha=fecha
            jovencito=nombre
    return jovencito
def obtenerCumpleaneros(animales,mes):
    lista=[]
    indice_mes=meses.index(mes)+1
    for _,_,(_,numero,_),correo in animales:
        if indice_mes==numero and correo not in lista:
            lista.append(correo)
    return lista          
def depositar(animal,monto,archivo):
    arch=open(archivo)
    temp=open('temporal.txt','w')
    for linea in arch:
        if animal in linea:
            datos=linea.strip().split(':')
            temp.write('{0}:{1}\n'.format(animal,int(datos[1])+monto))
        else:
            temp.write(linea)
    arch.close(), temp.close()
    arch=open(archivo,'w')
    temp=open('temporal.txt')
    for linea in temp:
        arch.write(linea)
    arch.close(), temp.close()
    print('Deposito realizado con exito!')
    return None
def sacarDinero(animal,monto,archivo):
    arch=open(archivo)
    temp=open('temporal.txt','w')
    condicion=False
    for linea in arch:
        if animal in linea:
            datos=linea.strip().split(':')
            if int(datos[1]) >=monto:
                temp.write('{0}:{1}\n'.format(animal,int(datos[1])-monto))
                condicion=True
            else:
                print('No se puede realizar giro')
                temp.write(linea)
        else:
            temp.write(linea)
    arch.close(), temp.close()
    arch=open(archivo,'w')
    temp=open('temporal.txt')
    for linea in temp:
        arch.write(linea)
    arch.close(), temp.close()
    if condicion:
        print('Giro realizado con exito!')
    return None
