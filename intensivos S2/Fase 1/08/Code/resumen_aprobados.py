def listado_alumnos(nombre_archivo):
    lista_nombres = []

    arch = open(nombre_archivo)
    for linea in arch:
        nombre, datos = linea.strip().split("#")
        lista_nombres.append(nombre)

    arch.close()
    return lista_nombres

def aprueba_por_notas(nombre_archivo):
    aprobacion = {}

    arch = open(nombre_archivo)
    for linea in arch:
        nombre, datos = linea.strip().split("#")
        
        lista_notas = datos.split(":")
        suma = 0
        cantidad = 0
        for nota in lista_notas:
            suma += int(nota)
            cantidad += 1

        promedio = suma/cantidad
        if promedio >= 55:
            aprobacion[nombre] = True
        else:
            aprobacion[nombre] = False

    arch.close()
    return aprobacion

def aprueba_por_asistencia(nombre_archivo):
    aprobacion = {}

    arch = open(nombre_archivo)
    for linea in arch:
        nombre, datos = linea.strip().split("#")
        
        lista_asistencia = datos.split(":")
        suma = 0
        cantidad = 0
        for asis in lista_asistencia:
            suma += int(asis)
            cantidad += 1

        promedio = 100*suma/cantidad
        if promedio > 75:
            aprobacion[nombre] = True
        else:
            aprobacion[nombre] = False

    arch.close()
    return aprobacion

def resumen(archivo_notas, archivo_asistencia):
    personas = listado_alumnos(archivo_notas)
    aprobaciones_por_notas = aprueba_por_notas(archivo_notas)
    aprobaciones_por_asistencia = aprueba_por_asistencia(archivo_asistencia)

    formato = "{0}#{1}\n"

    arch = open("Final.txt", "w")
    for nombre in personas:
        aprueba_notas = aprobaciones_por_notas[nombre]
        aprueba_asistencia = aprobaciones_por_asistencia[nombre]

        if aprueba_notas and aprueba_asistencia:
            para_escribir = formato.format(nombre, "APROBADO")
        elif not aprueba_notas and not aprueba_asistencia:
            para_escribir = formato.format(nombre, "REPROBADO")
        else:
            para_escribir = formato.format(nombre, "EXAMEN GLOBAL")

        arch.write(para_escribir)
    arch.close()

    return
