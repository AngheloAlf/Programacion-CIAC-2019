def mapear(funcion,lista):
    nuevo=[]
    for elemento in lista:
        agregar=funcion(elemento)
        nuevo.append(agregar)
    return nuevo
