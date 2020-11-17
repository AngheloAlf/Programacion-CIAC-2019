def total_producto(nom_producto, archivo):
    total=0
    arch=open(archivo)
    for linea in arch:
        datos=linea.strip().split(',')
        if nom_producto==datos[1]:
            total+=int(datos[2])
    arch.close()
    return total

def lista_productos(archivo):
    lista=[]
    arch=open(archivo)
    for linea in arch:
        datos=linea.strip().split(',')
        if datos[1] not in lista:
            lista.append(datos[1])
    arch.close()
    return lista

def generar_resumen(informe, fecha_inicio, fecha_final):
    resumen=open('resumen.txt','w')
    lista=lista_productos(informe)
    for producto in lista:
        cantidad=0
        lista2=[]
        arch=open(informe)
        for linea in arch:
            datos=linea.strip().split(',')
            fecha=list(map(int,datos[-1].split('/')))[::-1]
            fecha_i=list(map(int,fecha_inicio.split('/')))[::-1]
            fecha_f=list(map(int,fecha_final.split('/')))[::-1]
            if fecha_i<=fecha<=fecha_f and datos[1]==producto:
                cantidad+=int(datos[2])
                if datos[0] not in lista2:
                    lista2.append(datos[0])
        arch.close()
        if len(lista2)!=0:
            resumen.write('{0},{1},{2}\n'.format(producto,cantidad,'-'.join(lista2)))
    resumen.close()
    return None
                
                
