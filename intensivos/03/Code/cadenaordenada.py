def esta_ordenado(cadena):
    i=0
    while i<len(cadena)-1:
        if cadena[i]>cadena[i+1]:
            return False
        i+=1
    return True
cadena=input('Ingrese cadena de letras: ')
while cadena!='0':
    if esta_ordenado(cadena):
        print('El string',cadena,'esta ordenado alfabeticamente')
    else:
        print('El string',cadena,'esta desordenado :(')
    cadena=input('Ingrese cadena de letras: ')
