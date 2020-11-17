def tipos_donantes(tipo_sangre,matriz,sangres):
    indice=sangres.index(tipo_sangre)
    lista=[]
    contador=0
    for posible_donante in matriz[indice]:
        if posible_donante: #se puede agregar ==1, pero 1 es True y 0 es False
            lista.append(contador)
        contador+=1
    nueva=[]
    for indice in lista:
        nueva.append(sangres[indice])
    return nueva

def donantes(gente,tipos):
    personas=[]
    for tipo in tipos:
        for nombre,grupo_sanguineo in gente:
            if tipo==grupo_sanguineo:
                personas.append((nombre,tipo))
    return personas

def sobrevive(max_donacion,requerida,tipo_sanguineo):
    tipos=tipos_donantes(tipo_sanguineo,matriz,sangres)
    gente=donantes(gente,tipos)
    cantidad=len(gente)
    return cantidad*max_donacion>=requerida

