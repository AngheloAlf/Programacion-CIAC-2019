def agregar_guerrero(listaGuerreros, nombre, poderDePelea, latitud, longitud):
    # Generamos una tupla como lo indica el enunciado
    tupla = (nombre, poderDePelea, latitud, longitud)
    # Agregamos la tupla a la lista
    listaGuerreros.append(tupla)
    return

def buscar_al_mas_debil(listaGuerreros):
    # Usaremos algoritmo del minimo para buscar al mas debil.
    menor_poder = float("inf")
    debilucho = ()
    for guerrero in listaGuerreros:
        # Desempaquetamos la tupla.
        nombre, poderDePelea, latitud, longitud = guerrero
        # Comparamos si tiene un poder de pelea menor al guerrero anterior.
        if poderDePelea < menor_poder:
            # Si es asi, guardamos al guerrero en cuestion:
            menor_poder = poderDePelea
            debilucho = (nombre, poderDePelea, latitud, longitud)
        # Si no es mas debil que el ya encontrado, no nos interesa
        # por lo que no hay else.
    # Retornamos al mas debil que encontramos.
    # Ojo, hay que recordar que estamos en una funcion
    # por lo que usamos un return y no un print.
    return debilucho

def ruta_de_pelea(listaGuerreros):
    # Aqui almacenaremos la ruta que nos piden.
    ruta_final = list() # o bien ruta_final = []
    # Como nos indican que no podemos modificar la lista original, crearemos una nueva.
    lista_auxiliar = list(listaGuerreros)
    while len(lista_auxiliar) > 0:
        # Aqui lo que haremos es buscar al mas debil, agregarlo a nuestra ruta,
        # y eliminaremos a dicho guerrero de la otra lista.
        # Repetiremos esto hasta que no queden guerreros.
        debil = buscar_al_mas_debil(lista_auxiliar)
        ruta_final.append(debil)
        lista_auxiliar.remove(debil)
    return ruta_final

def distancia(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def distancia_recorrida(lista_guerreros, posicion):
    # Como nos piden la distancia, empezando por el mas debil, 
    # usaremos la funcion anterior que calcula eso.
    ruta = ruta_de_pelea(lista_guerreros)
    # Desempaquetamos la tupla.
    # Usaremos las variables x1, y1 para indicar la posicion actual.
    x1, y1 = posicion
    # En este contador almacenaremos la distancia recorrida.
    total_recorrido = 0
    for guerrero in ruta:
        # Desempaquetamos al guerrero
        nombre, poderDePelea, latitud, longitud = guerrero
        # Calculamos la distancia entre la posision actual y la posicion del guerrero.
        total_recorrido += distancia(x1, y1, latitud, longitud)
        # Como ahora nos encontramos en la posicion del guerrero nuevo, 
        # actualizamos las variables de nuestra posicion, dandoles el valor
        # del ultimo guerrero.
        x1, y1 = latitud, longitud
    return total_recorrido
