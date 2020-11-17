def suma_numeros(n):
    cadena=str(n)
    while len(cadena)!=1:
        suma=0
        i=0
        while i<len(cadena):
            suma+=int(cadena[i])
            i+=1
        cadena=str(suma)
    return cadena

def valor_letra(letra):
    if letra==' ':
        return 0
    return 1+((ord(letra)-65)%9)

def retroalimentacion(numero):
    if numero=='1':
        return 'Lider'
    elif numero=='2':
        return 'Amigo'
    elif numero=='3':
        return 'Comunicador'
    elif numero=='4':
        return 'Constructor'
    elif numero=='5':
        return 'Espiritu libre'
    elif numero=='6':
        return 'Responsable'
    elif numero=='7':
        return 'Perfeccionista'
    elif numero=='8':
        return 'Exitoso'
    elif numero=='9':
        return 'Filosofo'

nombre=input('Ingrese nombre: ')
while nombre!='':
    i=0
    total=0
    while i<len(nombre):
        total+=valor_letra(nombre[i])
        i+=1
    numero=suma_numeros(total)
    print(nombre,'es',retroalimentacion(numero))
    nombre=input('Ingrese nombre: ')
    
