def determinar_signo(signos, fecha):
    # Desempaquetamos la tupla
    anio,mes,dia=fecha

    # Para saber el signo de alguien no es necesario saber el anno de 
    # nacimiento, por lo que armaremos una tupla que solo contenga el mes
    # y el dia.
    nueva_fecha = (mes,dia)

    # Recorremos nuestra lista de signos y la desempaquetamos, para poder
    # manejar los datos de forma mas facil.
    for signo,(fech_i,fech_f) in signos:
        # Preguntamos si nuestra fecha esta contenida entre las fechas de 
        # cada signo. Si llegamos a encontrarlo, lo retornamos.
        if fech_i<=(mes,dia) and (mes,dia)<=fech_f:
            return signo
    # Como el signo de capricornio es especial, empezando en diciembre y 
    # terminando en enero, nunca va a cumplirse la condicion que planteamos
    # antes, por lo que si no logramos calzar ninguna fecha antes, sabemos 
    # que debe ser capricornio.
    return 'capricornio'

def nombre_signo(signos, fechas):
    resultado = []
    # Recorremos nuestra lista de fechas, desempaquetando immediatamente 
    # los nombres y las fechas de cada persona.
    for nombre, fecha in fechas:
        # Preguntamos el signo de la persona segun su fecha de nacimiento.
        signo = determinar_signo(signos, fecha)
        # Generamos la tupla que vamos a almacenar y la agregamos a nuestra
        # lista.
        tupla = (nombre, signo)
        resultado.append(tupla)
    return resultado

def buscar_elemento(lista_elementos, signo):
    # Recorremos nuestra lista de elementos, y la desempaquetamos en 
    # elemento y la lista de signos.
    for elem, lista_signos in lista_elementos:
        # Pregutamos si esta lista de signos contiene el signo que estamos
        # buscando. Si es asi, encontramos el elemento buscado.
        if signo in lista_signos:
            return elem

def compatibilidad(signos, lista_elementos, fechas):
    # Como nos piden relacionar elementos y personas, primero necesitamos
    # los signos de cada persona, por lo que reutilizamos la funcion 
    # anterior que relaciona a las personas con sus signos.
    mapeo=nombre_signo(signos, fechas)

    # En esta lista almacenaremos las tuplas en cuestion
    nuevo=[]

    # Recorremos la lista anterior, desempaquetando los nombres y los signos.
    for nombre, signo in mapeo:
        # Buscamos el elemento relacionado a este signo en particular
        ele = buscar_elemento(lista_elementos, signo)
        # Designamos una variable en donde guardaremos si encontramos el 
        # elelento que estamos buscando
        esta = False
        # Recorremos nuestra lista, buscando la tupla que tiene el elemento 
        # en cuestion, desempaquetamos el elemento y la lista de personas.
        for elemento, personas in nuevo:
            # Preguntamos si el elemento es el que buscamos, y si es asi, 
            # agregamos el nombre de la persona a nuestra lista de personas.
            if elemento == ele:
                personas.append(nombre)
                # Si encontramos nuestro elemento, guardamos en una variable
                # que lo encontramos.
                esta = True

        # Si no encontramos el elemento en la lista, debemos agregarlo
        if not esta:
            # Generamos la estructura de la tupla, donde ponemos el elemento 
            # y la lista de personas. Como sabemos que la persona que estamos
            # procesando ya posee  este elemento, generamos la lista con esta
            # persona dentro.
            tupla = (ele, [nombre])
            # Agregamos la tupla en cuestion a la lista.
            nuevo.append(tupla)
    return nuevo
