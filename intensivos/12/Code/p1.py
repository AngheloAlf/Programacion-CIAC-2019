def sismosOrdenados(sismos):
    # Como nos piden usar una generar una lista ordenada, usaremos el 
    # metodo lista.sort() .
    # Para ello, debemos poner como primer elemento de las tuplas el
    # elemento por el cual queremos ordenar la lista.
    lista_auxiliar = []
    for ciudad, fecha, escala in sismos:
        # Aqui recorremos la lista con el objetivo de poner la escala
        # richter como primer elemento de cada tupla y almacenarlo
        # en una lista nueva.
        tupla = (escala, fecha, ciudad)
        lista_auxiliar.append(tupla)

    # Una vez tenemos el elemento importante en la primera posicion,
    # usamos el lista.sort() para ordenar dicha lista
    lista_auxiliar.sort()
    # Como sabemos que lista.sort() ordena de menor a mayor, invertimos
    # la lista para que quede ordenada de mayor a menor, tal cual como
    # nos pide el enunciado.
    lista_auxiliar.reverse()

    # Finalmente, recorremos nuestra nueva lista ordenada, con el objetivo
    # de organizar los valores de las tuplas en el orden original.
    tembloresOrdenados = list()
    for escala, fecha, ciudad in lista_auxiliar:
        tupla = (ciudad, fecha, escala)
        tembloresOrdenados.append(tupla)
    return tembloresOrdenados

def sismosEnCiudad(sismos, ciudad):
    # Como sabemos que nos piden que los sismos de cada ciudad deben
    # estar ordenados, los ordenaremos antes de empezar a procesarlos.
    # De esta forma, cuando estemos trabajando con ellos, no tendremos
    # que preocuparnos de ordenarlos.
    ordenados = sismosOrdenados(sismos)

    listaCiudad = list()
    for ciudad_temblor, fecha, escala in ordenados:
        # Recorremos los sismos en cuestion en busca de todos los que
        # hayan ocurrido en la ciudad indicada
        if ciudad_temblor == ciudad:
            # Si la ciudad del temblor es la misma que la que nos indican, 
            # agregaremos la fecha y la escala unicamente a la lista de 
            # sismos de dicha ciudad
            tupla = (fecha, escala)
            listaCiudad.append(tupla)
    return listaCiudad

def tuplaAnnosADia(fecha):
    # Esta es una funcion auxiliar.
    # Tiene el objetivo de convertir la fecha entregada como
    # parametro a la cantidad equivalente en dias.
    # Por simplicidad, se asume que todos los anos tienen 365 dias, y que
    # todos los meses tienen 30 dias
    anno, mes, dia = fecha
    return anno * 365 + mes * 30 + dia

def probabilidadDeSismo(sismos, ciudad, fechaActual):
    # Como solo nos interesa la ciudad en cuestion, llamamos a la
    # funcion sismosEnCiudad() para que nos diga los sismos de 
    # dicha ciudad
    listaTemblores = sismosEnCiudad(sismos, ciudad)
    # Para procesar mas facil las fechas, las trabajaremos en
    # dias en vez de tupla.
    diaActual = tuplaAnnosADia(fechaActual)

    # Como nos piden usar el sismo de gran intensidad mas cercano
    # a la fecha actual, usaremos el algoritmo del menor para poder
    # encontrarlo y usarlo.
    fechaRichter = float("inf")
    for fecha, escala in listaTemblores:
        diaViejo = tuplaAnnosADia(fecha)
        diferenciaDias = diaActual - diaViejo
        # Nos interesa un sismo que sea de gran intensidad (osea
        # mayor o igual que 7 en escala richter), y que la diferencia
        # con la fecha actual sea la minima.
        if escala >= 7.0 and  diferenciaDias < fechaRichter:
            fechaRichter = diferenciaDias

    # Calculamos la probabilidad de que ocurra un sismo
    probabilidad = fechaRichter/18250.0*100
    # Como nos dicen que la probabilidad no puede ser mayor que 90%,
    # revisamos si supera dicho numero, y en caso de que lo supere
    # lo cambiamos. Este numero es nuestro tope.
    if probabilidad > 90.0:
        probabilidad = 90.0
    return probabilidad
