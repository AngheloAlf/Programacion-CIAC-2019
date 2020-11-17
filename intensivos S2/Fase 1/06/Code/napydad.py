def archivo_a_diccionario(archivo):
    ar = open(archivo)
    dic = dict()
    for linea in ar:
        if ";" in linea:
            nombre, ubicacion, tipo = linea.strip().split(";")
            x, y = ubicacion.split(",")
            dic[nombre] = {"ubicacion": (float(x), float(y)), "tipo": tipo}
    ar.close()
    return dic

def diccionario_a_archivo(dic, archivo):
    ar = open(archivo, "w")
    plantilla = "{0};{1},{2};{3}\n"
    for nombre, datos in dic.items():
        x = str(datos["ubicacion"][0])
        y = str(datos["ubicacion"][1])
        tipo = datos["tipo"]
        ar.write(plantilla.format(nombre, x, y, tipo))
    ar.close()
    return

def calcular_distancia(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def persona_mas_cerca(personas, posicion):
    mas_cercano = ""
    menor_distancia = float("inf")
    for nombre, datos in personas.items():
        dis = calcular_distancia(datos["ubicacion"], posicion)
        if dis < menor_distancia and datos["tipo"] == "B":
            dis = menor_distancia
            mas_cercano = nombre
    return mas_cercano

def quedan_personas_buenas(personas):
    for datos in personas.values():
        if datos["tipo"] == "B":
            return True
    return False

def mejor_ruta(archivo, posicion):
    personas = archivo_a_diccionario(archivo)
    print(personas)
    orden = []
    terminar = False
    while quedan_personas_buenas(personas):
        persona = persona_mas_cerca(personas, posicion)
        orden.append(persona)
        del personas[persona]
    return orden

def restaurar(archivo, respaldo):
    personas = archivo_a_diccionario(archivo)
    resp = dict(respaldo)
    for nombre in personas:
        personas[nombre]["tipo"] = resp[nombre]
    diccionario_a_archivo(personas, archivo)
    return