def sospechosos(personas, publicaciones):
    arch1=open(personas)
    lista=[]
    for linea1 in arch1:
        rut,edad,calificaciones=linea1.strip().split(',')
        edad=int(edad)
        arch2=open(publicaciones)
        for linea2 in arch2:
            rut2,medio=linea2.strip().split(':')
            if rut==rut2 and edad<41 and medio!='twitter' and rut not in lista:
                lista.append(rut)
        arch2.close()
    arch1.close()
    return lista

def esta_palabra(palabra,archivo):
    arch=open(archivo)
    for linea in arch:
        if palabra in linea:
            arch.close()        
            return True
    arch.close()
    return False

def leer_mensajes(personas, publicaciones, claves):
    lista=sospechosos(personas,publicaciones)
    diccionario={}
    for sospechoso in lista:
        diccionario[sospechoso]=0
        for palabra in claves:
            if esta_palabra(palabra,sospechoso+'.txt'):
                diccionario[sospechoso]+=1
    return diccionario

def ranking(personas):
    lista=[]
    arch_per=open(personas)
    for linea in arch_per:
        datos=linea.strip().split(',')
        calificaciones=list(map(float,datos[2].split('-')))
        prom=(sum(calificaciones))/(len(calificaciones) )
        if prom > 30:
            lista.append(datos[0])
    arch_per.close()
    return lista

def peligro(personas,publicaciones,claves):
    mensajes=leer_mensajes(personas,publicaciones,claves)
    ran=ranking(personas)
    rut_mensajes=[]
    for rut,cantidad in mensajes.items():
        if cantidad>=2:
            rut_mensajes.append(rut)
    retorno=[]
    for rut in rut_mensajes:
        if rut in ran:
            retorno.append(rut)
    return retorno
