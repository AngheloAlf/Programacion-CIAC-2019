def listado_alumnos(nombre_archivo):
    lista=[]
    archivo=open(nombre_archivo)
    for linea in archivo:
        nombre=linea.strip().split('#')[0]
        lista.append(nombre)
    archivo.close()
    return lista

def aprueba_por_notas(nombre_archivo):
    diccionario={}
    archivo=open(nombre_archivo)
    for linea in archivo:
        nombre=linea.split('#')[0]
        notas=linea.strip().split('#')[1].split(':')
        notas=list(map(int,notas))
        promedio=float(sum(notas))/len(notas)
        diccionario[nombre]=(promedio>=55)
    archivo.close()
    return diccionario

def aprueba_por_asistencia(nombre_archivo):
    diccionario={}
    archivo=open(nombre_archivo)
    for linea in archivo:
        nombre=linea.split('#')[0]
        asistencia=linea.strip().split('#')[1].split(':')
        porcentaje=(asistencia.count('1')*100)/7
        diccionario[nombre]=porcentaje>=75
    archivo.close()
    return diccionario

def resumen(archivo_notas,archivo_asistencia):
    final=open('Final.txt','w')
    diccionario_notas=aprueba_por_notas(archivo_notas)
    diccionario_asistencia=aprueba_por_asistencia(archivo_asistencia)
    for nombre in listado_alumnos(archivo_notas):
        if diccionario_notas[nombre] and diccionario_asistencia[nombre]:
            final.write(nombre+'#APROBADO\n')
        elif diccionario_notas[nombre] or diccionario_asistencia[nombre]:
            final.write(nombre+'#EXAMEN GLOBAL\n')
        else:
            final.write(nombre+'#REPROBADO\n')
    final.close()
    return None
