def info_temas(arch_temas):
    info={}
    arch=open(arch_temas)
    for linea in arch:
        datos=linea.strip().split(';')
        tema=datos[0].replace('(','').replace(')','')
        palabras=datos[1].split(',')
        info[tema]=palabras
    arch.close()
    return info

def cantidad(oracion,diccionario):
    dicc={}
    for tema,palabras in diccionario.items():
        for palabra in palabras:
            if palabra in oracion:
                if tema not in dicc:
                    dicc[tema]=0
                dicc[tema]+=1
    maximo=-float('inf')
    for tema,cant in dicc.items():
        if cant>maximo:
            maximo=cant
            dominante=tema
    return dominante       

def clasificacion(arch_temas, arch_oraciones):
    info=info_temas(arch_temas)
    nuevo=open('temas_oraciones.txt','w')
    oraciones=open(arch_oraciones)
    for linea in oraciones:
        datos=linea.strip().split(':')
        numero=datos[0]
        oracion=datos[1]
        nuevo.write('{0}:{1}\n'.format(numero,cantidad(oracion,info)))
    oraciones.close()
    nuevo.close()
    return None
