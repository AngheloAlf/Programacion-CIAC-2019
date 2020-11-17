def mismo_grupo(grupos, pais1, pais2):
    for letra, equipos in grupos:
        if pais1 in equipos and pais2 in equipos:
            return True
    return False

# Funcion auxiliar
# Esta funcion recibe la tupla de un pais, los goles que hizo en el partido
# y los goles que le hicieron. Actualiza los datos de forma correspondiente y 
# retorna dicha tupla actualizada.
def actualizar_pais_auxiliar(datos_pais, goles_realizados, goles_en_contra):
    n, pj, pg, pe, pp, gf, ge, gdif, pts = datos_pais
    pj += 1
    if goles_realizados > goles_en_contra:
        pg += 1
        pts += 3
    elif goles_realizados == goles_en_contra:
        pe += 1
        pts += 1
    else:
        pp += 1
    gf += goles_realizados
    ge += goles_en_contra
    gdif = gf - ge
    return (n, pj, pg, pe, pp, gf, ge, gdif, pts)

def jugar_partido(grupos, puntaje, pais1, pais2, goles1, goles2):
    if not mismo_grupo(grupos, pais1, pais2):
        # Como no son del mismo grupo, no tiene sentido que juegen el partido.
        return
    tupla1 = ()
    tupla2 = ()
    # Buscamos ambos paises en cuestion
    for datos in puntaje:
        if pais1 in datos:
            tupla1 = datos
        if pais2 in datos:
            tupla2 = datos

    # Quitamos ambos paises, mas adelante los agregaremos de nuevo
    puntaje.remove(tupla1)
    puntaje.remove(tupla2)

    # Procesamos el primer pais
    tupla1 = actualizar_pais_auxiliar(tupla1, goles1, goles2)
    puntaje.append(tupla1)

    # Procesamos el segundo pais
    tupla2 = actualizar_pais_auxiliar(tupla2, goles2, goles1)
    puntaje.append(tupla2)
    return None

def datos_grupo(grupos, puntaje, letra_grupo):
    paises = []
    # Buscamos los paises del grupo en cuestion.
    for letra, equipos in grupos:
        if letra_grupo == letra:
            paises = equipos

    resultado = []
    for pais in paises:
        for datos in puntaje:
            if pais == datos[0]:
                n, pj, pg, pe, pp, gf, ge, gdif, pts = datos
                # Como nos piden que se ordene por puntaje, y en segunda
                # instancia por diferencia de goles, ponemos esos 2 datos
                # primeros. Como no nos indican que hacer en caso de que 
                # esos 2 sean iguales, ponemos el resto de los datos en el 
                # orden que estimemos conveninente.
                tupla = (pts, gdif, n, pj, pg, pe, pp, gf, ge)
                resultado.append(tupla)
    # Ordenamos de mayor a menor
    resultado.sort()
    resultado.reverse()
    ordenado = []
    for datos in resultado:
        # Reordenamos los datos en el orden correcto.
        pts, gdif, n, pj, pg, pe, pp, gf, ge = datos
        tupla = n, pj, pg, pe, pp, gf, ge, gdif, pts
        ordenado.append(tupla)
    return tuple(ordenado)

# Funcion auxiliar
# Recibe 3 tuplas correspondiente a paises.
# Entrega una lista con los nombres de los paises ordenados de mejor a 
# peor segun su puntaje.
def ordenar_terceros(A3, B3, C3):
    # Desempaquetamos y ponemos primero los puntos y la diferencia de
    # goles de cada pais.
    n, pj, pg, pe, pp, gf, ge, gdif, pts = A3
    A3 = pts, gdif, n, pj, pg, pe, pp, gf, ge
    n, pj, pg, pe, pp, gf, ge, gdif, pts = B3
    B3 = pts, gdif, n, pj, pg, pe, pp, gf, ge
    n, pj, pg, pe, pp, gf, ge, gdif, pts = C3
    C3 = pts, gdif, n, pj, pg, pe, pp, gf, ge
    lista = [A3, B3, C3]
    # Ordenamos de mayor a menor.
    lista.sort()
    lista.reverse()
    nombres = []
    for datos in lista:
        # Solo nos interesan los nombres de estos paises, por lo que
        # solo tomamos estos datos.
        nombres.append(datos[2])
    return nombres

def cuartos_de_final(grupos, puntaje):
    grupo_A = datos_grupo(grupos, detalles_puntaje, "A")
    grupo_B = datos_grupo(grupos, detalles_puntaje, "B")
    grupo_C = datos_grupo(grupos, detalles_puntaje, "C")
    # La funcion datos_grupo nos entrega los paises ordenados de mejor a
    # peor, por lo que nos aprovechamos de eso.
    A1, A2, A3, _ = grupo_A
    B1, B2, B3, _ = grupo_B
    C1, C2, C3, _ = grupo_C
    tercero1, tercero2, tercero3 = ordenar_terceros(A3, B3, C3)
    primer_partido = (A1[0], tercero1)
    segundo_partido = (A2[0], C2[0])
    tercer_partido = (B1[0], tercero2)
    cuarto_partido = (C1[0], B2[0])
    return [primer_partido, segundo_partido, tercer_partido, cuarto_partido]
