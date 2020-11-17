def tuplinador(lista_strings):
    lista_auxiliar = []
    for i in lista_strings:
        lista_auxiliar.append(int(i))
    return tuple(lista_auxiliar)

def diccioninador(archivo):
    arch = open(archivo)
    dicc = dict()
    for linea in arch:
        datos = linea.strip().split("#")
        nombre = datos[0]
        if nombre not in dicc:
            dicc[nombre] = dict()
        ramo = datos[1]
        notas = datos[2].split(";")
        tupla = tuplinador(notas)
        dicc[nombre][ramo] = tupla
    arch.close()
    return dicc

def stringifinador(tupla_enteros):
    lista_auxiliar = []
    for i in tupla_enteros:
        lista_auxiliar.append(str(i))
    return lista_auxiliar

def archivinador(archivo, diccionario):
    arch = open(archivo, "w")
    plantilla = "{0}#{1}#{2}\n"
    for nombre, datos in diccionario.items():
        for ramo, notas in datos.items():
            notas = stringifinador(notas)
            notas = ";".join(notas)
            escribir = plantilla.format(nombre, ramo, notas)
            arch.write(escribir)
    arch.close()
    return

def agregar_alumno_inador(archivo, nombre, ramos):
    dicc = diccioninador(archivo)
    if nombre not in dicc:
        dicc[nombre] = dict()
    for sigla, notas in ramos.items():
        dicc[nombre][sigla] = notas
    archivinador(archivo, dicc)
