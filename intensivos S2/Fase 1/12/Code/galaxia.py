# Funcion auxiliar.
# Recibe el nombre del archivo planetas y el nombre de un planeta.
# Retorna una lista la posicion de ese planeta.
# Si el planeta no se llama, retorna una lista vacia.
def obtenerPlaneta(planetas, plan):
    arch=open(planetas)
    # Si no encontramos el planeta, tendremos una lista vacia de 
    # emergencia.
    datos_paneta = list()
    for linea in arch:
        nombre, pos = linea.strip().split('#')
        if nombre == plan:
            # Si el planeta es el buscado, guardamos la posicion
            # de dicho planeta
            datos_paneta = pos.split(";")
    arch.close()
    return datos_paneta

# Funcion auxiliar.
# Recibe 2 listas de strings con posiciones tridimensionales.
# Retorna la distancia esntre esas 2 posiciones
def distancia(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    x1, y1, z1 = int(x1), int(y1), int(z1)
    x2, y2, z2 = int(x2), int(y2), int(z2)
    dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    return dist**0.5

def masCercaTierra(planetas):
    # Como nos piden comparar con la tierra, obtenemos su posicion
    # inmediatamente para poder usarla.
    pos_tierra = obtenerPlaneta(planetas, "Tierra")

    minimo = float('inf')
    cercano = ""

    arch=open(planetas)
    for linea in arch:
        # Recorremos todos los planetas del archivo
        nombre, pos = linea.strip().split('#')
        # Revisamos que el planeta que vamos a revisar no sea la Tierra 
        # (Obviamente el planeta mas cercano a la Tierra es la Tierra, pero
        # no nos interesa eso).
        if 'Tierra' != nombre:
            pos = pos.split(';')
            dist = distancia(pos_tierra, pos)
            # Aplicamos algoritmo del minimo para encontrar el planeta con 
            # la menor distancia, y guardamos el nombre de dicho planeta.
            if dist < minimo:
                minimo = dist
                cercano = nombre
    arch.close()
    return cercano

def nuevo(planetas,caracteristicas):
    galaxia = open('galaxia.txt','w')
    arch = open(caracteristicas)
    # Contiene la estructura del archivo galaxia.
    formato = "{0}#{1}#{2}#{3}\n"
    for linea in arch:
        nombre, rotacion, traslacion = linea.strip().split('#')
        # Para cada planeta del archivo de caracteristicas, buscamos su 
        # posicion en el archivo de planetas.
        posicion = obtenerPlaneta(planetas, nombre)
        # Tenemos que dejar el string de posicion con la estructura correcta.
        pos = ";".join(posicion)
        escribir = formato.format(nombre, pos, rotacion, traslacion)
        galaxia.write(escribir)
    arch.close()
    galaxia.close()

def masParecidoTierra():
    arch = open('galaxia.txt')
    minimo = float('inf')
    planeta = ""
    # Recorremos el archivo en busqueda del mas parecido.
    for linea in arch:
        nom, pos, rot, tras = linea.strip().split('#')
        # Nos aseguramos de no contabilizar la tierra.
        if 'Tierra' != nom:
            # Calculamos que tanto se parecen estos 2 planetas entre ellos.
            funcion = (int(rot)-24)**2 + (int(tras)-365)**2
            # El mas parecido sera el que tenga este resultado menor.
            if funcion < minimo:
                minimo = funcion
                planeta = nom
    arch.close()
    return planeta
