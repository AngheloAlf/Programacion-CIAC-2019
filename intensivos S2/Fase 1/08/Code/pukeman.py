def promedio(datos):
    suma = 0
    total = 0
    for xi in datos:
        suma += int(xi)
        total += 1
    prom = suma/total
    return prom

def varianza(datos):
    prom = promedio(datos)
    var = 0
    total = 0
    for xi in datos:
        var += (int(xi) - prom)**2
        total += 1
    return var/total

def buscarNombrePorIde(nombres, ide):
    archNombres = open(nombres)
    nombreNuevo = ""
    for linea in archNombres:
        datos = linea.strip().split(";")
        ide_pkmn, nombre = datos
        if ide_pkmn == ide:
            nombreNuevo = nombre
    archNombres.close()
    return nombreNuevo


# Pregunta 1
def mejor_Nash(pukemones, nombres):
    menorVar = float("inf")
    menorIde = ""

    arch = open(pukemones)    
    for linea in arch:
        datos = linea.strip().split(";")
        ide, stats, tipo = datos

        stats = stats.split(",")
        var = varianza(stats)

        if var < menorVar:
            menorVar = var
            menorIde = ide
    arch.close()

    nom = buscarNombrePorIde(nombres, menorIde)
    return nom

# Pregunta 2
def mejor_Fisty(pukemones, nombres):
    sumaMayor = 0
    ideMayor = ""

    arch = open(pukemones)
    for linea in arch:
        datos = linea.strip().split(";")
        ide, stats, tipo = datos

        stats = stats.split(",")
        salud, atk, defe, atk_esp, def_esp, vel = stats

        if tipo == "Grass":
            suma = int(atk_esp) + int(def_esp)
            if suma > sumaMayor:
                sumaMayor = suma
                ideMayor = ide
    arch.close()

    nom = buscarNombrePorIde(nombres, ideMayor)
    return nom

# Pregunta 3
def filtro_Block(pukemones, nombres, saludMin):
    dicc = dict()

    arch = open(pukemones)
    for linea in arch:
        datos = linea.strip().split(";")
        ide, stats, tipo = datos

        stats = stats.split(",")
        stats = tuple(map(int, stats))
        salud, atk, defe, atk_esp, def_esp, vel = stats

        if tipo == "Normal" or tipo == "Electric":
            if int(salud) >= saludMin:
                dicc[ide] = (stats, tipo)
    arch.close()

    nuevoDict = dict()
    for ide, datosPuke in dicc.items():
        nuevoNombre = buscarNombrePorIde(nombres, ide)
        nuevoDict[nuevoNombre] = datosPuke
    return nuevoDict

# Pregunta 4
def quitar_pukeman(pukemones, nombres, nombrePukeman):
    ide_quitar = ""

    archNombres = open(nombres)
    for linea in archNombres:
        datos = linea.strip().split(";")
        ide_pkmn, nombre = datos

        if nombre == nombrePukeman:
            ide_quitar = ide_pkmn
    archNombres.close()

    listaArch = list()
    arch = open(pukemones)
    for linea in arch:
        datos = linea.strip().split(";")
        ide, stats, tipo = datos

        if ide != ide_quitar:
            listaArch.append(linea)
    arch.close()

    arch = open(pukemones, "w")
    for linea  in listaArch:
        arch.write(linea)
    arch.close()
    return
