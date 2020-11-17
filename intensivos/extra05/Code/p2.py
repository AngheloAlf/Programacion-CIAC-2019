# Funcion auxiliar
# Retorna la tupla del orden de los programas asociados al dia correspondiente.
def orden_del_dia(dia):
    for nom_dia, shows in programas_por_dia:
        if nom_dia == dia:
            return shows
    return ()

# Funcion auxiliar
# Retorna el programa asociado al codigo entregado.
def buscar_programa(codigo):
    for datos in programas:
        # datos[1] contiene el codigo del programa
        if codigo == datos[1]:
            return datos
    return ()

def cantidad_de_programas(dia):
    shows = orden_del_dia(dia)
    return len(shows)

def nombre_primer_programa(dia):
    shows = orden_del_dia(dia)
    primer_show = shows[0]
    prog = buscar_programa(primer_show)
    return prog[0]

def pais_origen_ultimo(dia):
    shows = orden_del_dia(dia)
    ultimo_show = shows[-1]
    prog = buscar_programa(ultimo_show)
    return prog[2]

def tiempo_total(dia):
    duracion = 0
    shows = orden_del_dia(dia)
    for codigo in shows:
        prog = buscar_programa(codigo)
        duracion += prog[3]
    return duracion

def nombre_programa_largo(dia):
    duracion = 0
    nombre = ""
    shows = orden_del_dia(dia)
    for codigo in shows:
        prog = buscar_programa(codigo)
        if prog[3] > duracion:
            duracion = prog[3]
            nombre = prog[0]
    return nombre

def tiempo_programa_largo(dia):
    # Copy-paste de la funcion anterior, cambiando el valor de retorno.
    duracion = 0
    nombre = ""
    shows = orden_del_dia(dia)
    for codigo in shows:
        prog = buscar_programa(codigo)
        if prog[3] > duracion:
            duracion = prog[3]
            nombre = prog[0]
    return duracion

def idioma(dia):
    # lista de listas. Cada sublista la cantidad de veces que aparece el 
    # idioma, y el nombre del idioma en cuestion
    lista = []
    shows = orden_del_dia(dia)
    for codigo in shows:
        prog = buscar_programa(codigo)
        idioma = prog[4]
        encontrado = False
        for i in lista:
            if i[1] == idioma:
                i[0] += 1
                encontrado = True
        if not encontrado:
            lista.append([1, idioma])
    lista.sort()
    lista.reverse()
    el_mas_hablado = lista[0]
    return el_mas_hablado[1]

def programacion_del_dia(dia):
    lista = []
    shows = orden_del_dia(dia)
    for codigo in shows:
        prog = buscar_programa(codigo)
        lista.append(prog)
    return lista
