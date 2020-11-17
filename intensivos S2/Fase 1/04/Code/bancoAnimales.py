def listaPaises(animales):
    lista = []
    for cientifico, comun, fecha, correo in animales:
        tld = correo.split('.')[-1]
        lista.append(paises[tld])
    return lista

def animalMasJoven(animales):
    mayor_fecha = (0,0,0)
    jovencito = ''
    for cientifico, comun, fecha, correo in animales:
        if fecha > mayor_fecha:
            mayor_fecha = fecha
            jovencito = cientifico
    return jovencito

def obtenerCumpleaneros(animales, mes):
    lista = list()
    indice_mes = meses.index(mes) + 1
    for cientifico, comun, fecha, correo in animales:
        anno, mes_animal, dia_animal = fecha
        if indice_mes == mes_animal:
            if correo not in lista:
                lista.append(correo)
    return lista

def depositar(animal, monto, archivo):
    formato = '{0}:{1}\n'

    arch = open(archivo)
    temp = open('temporal.txt','w')
    for linea in arch:
        if animal in linea:
            datos = linea.strip().split(':')
            nombre, dinero = datos
            dinero = int(dinero)
            para_escribir = formato.format(animal, dinero + monto)
            temp.write(para_escribir)
        else:
            temp.write(linea)
    arch.close()
    temp.close()

    arch=open(archivo, 'w')
    temp=open('temporal.txt')
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()

    return 'Deposito realizado con exito!'

def sacarDinero(animal, monto, archivo):
    formato = '{0}:{1}\n'
    condicion = False

    arch = open(archivo)
    temp = open('temporal.txt','w')
    for linea in arch:
        if animal in linea:
            datos = linea.strip().split(':')
            nombre, dinero = datos
            dinero = int(dinero)
            if dinero >= monto:
                para_escribir = formato.format(animal, dinero - monto)
                temp.write(para_escribir)
                condicion=True
            else:
                temp.write(linea)
        else:
            temp.write(linea)
    arch.close()
    temp.close()

    arch=open(archivo,'w')
    temp=open('temporal.txt')
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()

    if condicion:
        return 'Giro realizado con exito!'
    return 'No se puede realizar giro'
