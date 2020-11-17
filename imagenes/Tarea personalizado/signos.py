def determinar_signo(fecha):
    anio,mes,dia=fecha
    for signo,(fech_i, fech_f) in signos.items():
        if fech_i<=(mes,dia)<=fech_f:
            return signo
    return 'capricornio'

def dic_nobre_signo(fechas):
    diccionario={}
    for nombre,fecha in fechas.items():
        diccionario[nombre]=determinar_signo(fecha)
    return diccionario

def elemento(signo):
    for elemento, lista in elementos.items():
        if signo in lista:
            return elemento
