def ponderarPuntaje(puntajes, ponderaciones):
    total = 0
    for llave in ponderaciones:
        total += puntajes[llave]*ponderaciones[llave]/100
    return total

# Solucion alternativa
def ponderarPuntaje2(puntajes, ponderaciones):
    total = 0
    total += puntajes["mat"]*ponderaciones["mat"]/100
    total += puntajes["leng"]*ponderaciones["leng"]/100
    total += puntajes["ciencias"]*ponderaciones["ciencias"]/100
    return total

def obtenerPuntajes(archPuntajes):
    arch = open(archPuntajes)
    datos_de_personas = dict()
    for linea in arch:
        datos = linea.strip().split(",")
        uiu, nombre, edad, lugar, puntajes, nota = datos

        uiu = int(uiu)
        edad = int(edad)
        nota = int(nota)

        nelpn = {"nombre": nombre, "edad": edad, "lugar": lugar, 
                  "nota": nota, "puntajes": dict()}

        puntos_separados = puntajes.split("-")
        nelpn["puntajes"]["mat"] = int(puntos_separados[0])
        nelpn["puntajes"]["leng"] = int(puntos_separados[1])
        nelpn["puntajes"]["ciencias"] = int(puntos_separados[2])

        datos_de_personas[uiu] = nelpn

    arch.close()
    return datos_de_personas

def alcanzaCorte(nelpn, ponderacion, corte):
    puntajes = nelpn["puntajes"]
    ponderado = ponderarPuntaje(puntajes, ponderacion)
    nota = nelpn["nota"]
    puntaje_final = (ponderado + nota)/2
    if puntaje_final > corte:
        return (True, puntaje_final)
    return (False, puntaje_final)
    # Tambien hubiera funcionado:
    # return (puntaje_final > corte, puntaje_final)

def mayoresQueElCorte(ponderacion, corte, archivoPuntajes):
    datos_de_personas = obtenerPuntajes(archivoPuntajes)

    tuplatoria = []
    for uiu, nelpn in datos_de_personas.items():
        alcanza, puntaje_final = alcanzaCorte(nelpn, ponderacion, corte)
        if alcanza:
            # Ponemos primero el puntaje para que sea mas facil ordenar
            tupla = (puntaje_final, uiu)
            tuplatoria.append(tupla)

    tuplatoria.sort() # De menor a mayor
    tuplatoria.reverse() # De mayor a menor

    lista_ordenada = []
    for puntaje_final, uiu in tuplatoria:
        # Agregamos los datos segun el orden que nos pidieron
        tupla = (uiu, puntaje_final)
        lista_ordenada.append(tupla)

    return lista_ordenada

def asignarBonus(archPuntajes, lugar, bonus):
    datos_de_personas = obtenerPuntajes(archPuntajes)
    for uiu, nelpn in datos_de_personas.items():
        if nelpn["lugar"] == lugar:
            nelpn["puntajes"]["mat"] += bonus
            if nelpn["puntajes"]["mat"] > 700:
                nelpn["puntajes"]["mat"] = 700
            nelpn["puntajes"]["leng"] += bonus
            if nelpn["puntajes"]["leng"] > 700:
                nelpn["puntajes"]["leng"] = 700
            nelpn["puntajes"]["ciencias"] += bonus
            if nelpn["puntajes"]["ciencias"] > 700:
                nelpn["puntajes"]["ciencias"] = 700

    arch = open(archPuntajes, "w")
    formato = "{},{},{},{},{},{}\n"
    formato_puntajes = "{}-{}-{}"
    for uiu, nelpn in datos_de_personas.items():
        nombre = nelpn["nombre"]
        edad = nelpn["edad"]
        lugar = nelpn["lugar"]
        puntajes = nelpn["puntajes"]
        nota = nelpn["nota"]

        mat = puntajes["mat"]
        leng = puntajes["leng"]
        ciencias = puntajes["ciencias"]

        puntos = formato_puntajes.format(mat, leng, ciencias)
        datos = formato.format(uiu, nombre, edad, lugar, puntos, nota)

        arch.write(datos)
    arch.close()
    return
