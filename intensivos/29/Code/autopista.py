def ruta_autopista(archivo_autopista, patente):
    lista=[]
    arch=open(archivo_autopista)
    for linea in arch:
        datos=linea.strip().split(',')
        if datos[0]==patente:
            lista.append((datos[1],datos[2]))
    arch.close()
    return lista

def rutas(lista_nombres, patente):
    lista=[]
    for archivo in lista_nombres:
        lista=lista+ruta_autopista(archivo,patente)
    lista2=[]
    for pat,hor in lista:
        lista2.append((hor,pat))
    lista2.sort()
    lista=[]
    for hor,pat in lista2:
        lista.append((pat,hor))
    return lista

def lista_patentes(lista_nombres):
    lista=[]
    for nombre in lista_nombres:
        arch=open(nombre)
        for linea in arch:
            datos=linea.strip().split(',')
            if datos[0] not in lista:
                lista.append(datos[0])
        arch.close()
    return lista

def escribir_rutas(lista_nombres):
    lista=lista_patentes(lista_nombres)
    for patente in lista:
        lista_rutas=rutas(lista_nombres,patente)
        archivo=open(patente+'.txt','w')
        for pat, hora in lista_rutas:
            archivo.write('{0};{1}\n'.format(pat,hora))
        archivo.close()
    return None
