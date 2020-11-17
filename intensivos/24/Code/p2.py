def mejor_Nash(Pukemanes):
    varianza = 100
    pukemon  = ''
    for p, datos in Pukemanes.items():
        numeros  = datos[0:-1]
        promedio = 0
        for i in numeros:
            promedio += i
        promedio   = float(promedio) / 6.0
        varianza_t = 0
        for i in numeros:
            varianza_t += (i)**2
        varianza_t = varianza_t / 6.0 - promedio**2
        if varianza_t < varianza:
            pukemon = p
    return pukemon

def mejor_Fisty(Pukemanes):
    umbral  = 0
    pukemon = ''
    for p, datos in Pukemanes.items():
        tipo    = datos[-1]
        if tipo == 'Grass':
            temp = datos[3] + datos[4]
            if temp > umbral:
                pukemon = p
    return pukemon

def filtro_Block(Pukemanes, salud):
    filtro = dict()
    for p, datos in Pukemanes.items():
        if datos[-1] == 'Normal' or datos[-1] == 'Electric':
            if datos[0] >= salud:
                filtro[p] = datos
    return filtro
