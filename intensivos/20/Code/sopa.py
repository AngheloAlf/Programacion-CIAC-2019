def encontrar_extremos(linea,palabra):
    largo=len(palabra)
    for i in range(len(linea)):
        if linea[i:i+largo]==palabra:
            return i,i+largo-1
    return None

def encontrar_palabra(palabra,sopa):
    L=[]
    #se busca horizontalmente
    for i_fila in range(len(sopa)):
        extremos=encontrar_extremos(sopa[i_fila],palabra)
        if extremos!= None:
            ini,fin=extremos
            for j in range(ini,fin+1):
                L.append((i_fila,j))
            return L
    #se busca verticalmente
    for i_columna in range(len(sopa[0])):
        linea=''
        for i_fila in range(len(sopa)):
            linea+=sopa[i_fila][i_columna]
        extremos=encontrar_extremos(linea,palabra)
        if extremos!=None:
            ini,fin=extremos
            for i in range(ini,fin+1):
                L.append((i,i_columna))
            return L
    return None

diccionario={}
lista=[]
for palabra in palabras:
    coordenadas=encontrar_palabra(palabra,sopa)
    if coordenadas:
        diccionario[palabra]=coordenadas
        lista.append((palabra,coordenadas))

def dibujar(palabra,sopa):
    blank='-'
    sopa_vacia=[]
    for i in range(len(sopa)):
        linea=''
        for j in range(len(sopa[0])):
            if (i,j) in diccionario[palabra]:
                linea+=palabra[diccionario[palabra].index((i,j))]
            else:
                linea+=blank
        sopa_vacia.append(linea)
    for i in sopa_vacia:
        print(i)
    return None