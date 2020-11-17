def get_pos(palabra, clave):
    if clave not in palabra:
        return -1
    else:
        posicion=0
        while posicion<len(palabra):
            if palabra[posicion:posicion+len(clave)]==clave:
                return posicion
            posicion+=1

def get_palabra(palabra,clave):
    posicion=get_pos(palabra,clave)
    if posicion!=-1:
        return palabra[:posicion]+palabra[posicion+len(clave):]
    return -1


clave=input('Ingrese clave: ')
palabra=input('Ingrese palabra: ')
mensaje=''
while palabra!='out':
    parte=get_palabra(palabra,clave)
    if parte!=-1:
        mensaje+=parte+' ' #Se agrega un espacio para separar
    palabra=input('Ingrese palabra: ')
print('El mensaje oculto es',mensaje)
