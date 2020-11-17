def suscritosPorCategoria(listas, categoria):
    total = 0

    for tipo, datos in listas.items():
        # Desampaquetamos la tupla datos. Como no  nos interesa el 
        # segundo valor de la tupla, usamos un guion bajo para 
        # desempaquetarlo, explicitando que no nos interesa.
        cantidad_susc, _, cate = datos
        if cate == categoria:
            total += cantidad_susc
    return total

def vistaCategoria(listas):
    recuento = dict()

    # tipo contendria la llave del diccionario
    for tipo in listas:
        # buscamos la tupla asociada a la llave en cuestion
        datos_tipo = listas[tipo]
        # desempaquetamos la tupla
        suscritos, dominio, categoria = datos_tipo

        # si la categoria en cuestion no se encuentra en el diccionario, 
        # lo agregamos.
        if categoria not in recuento:
            # Al agregarlo, le asignamos la estructura que nos indican, 
            # una lista de 2 elementos, la cual contiene un numero 
            # (cantidad de listas) y una lista (nombre de las listas)
            recuento[categoria] = [0, []]

        # actualizamos los datos que tengamos dentro de este diccionario.
        # Tomamos la cantidad de listas y le agregamos uno.
        recuento[categoria][0] += 1
        # Tomamos la lista de nombres y le agregamos el nombre nuevo.
        recuento[categoria][1].append(tipo)

    return recuento
