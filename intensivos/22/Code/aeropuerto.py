salidas = [('LAN123', ((2013,11,2), 'NewYork', 'EMBARQUE')),
('ALGO00',((2015,12,3),'Valparaiso','EN ESPERA')),
#...
('MX201', ((2013,4,28),  'Cancun', 'ARRIBADO'))]

vuelos = [('ALGO00', ['444444-4']), 
('LAN123', ['16740623-7', '1111111-1', '555555-5']), 
# ..., 
('MX201', ['777777-7'])]

personas = {'555555-5': ('Daniela Perez', 'Roma', (1991, 8, 17), 12000), 
'777777-7': ('Jorge Perez', 'Santiago', (1989, 2, 17), 1000), 
'444444-4': ('Edwar Lopez', 'Miami', (1900, 3, 11), 120000), 
'1111111-1': ('Sandra Lazo', 'Ibiza', (1970, 4, 14), 10000), 
'16740623-7': ('OEncina', 'NewYork', (1987, 7, 22), 62000)}

def estado_pasajero(nombre):
    saliDict = dict(salidas)
    for rut, (nombreP, ciudad, nacimiento, millas) in personas.items():
        if nombreP == nombre:
            for cod, listaRuts in vuelos:
                if rut in listaRuts:
                    estado = saliDict[cod][2]
                    return rut, ciudad, estado
    return None

def cambia_de_vuelo(rut, nuevo_vuelo, millas):
    if rut not in personas:
        return False
    else:
        datos = personas[rut]
        millas += datos[3]
        datos = (datos[0], datos[1], datos[2], millas)
        personas[rut] = datos
        for cod, listaRuts in vuelos:
            if rut in listaRuts:
                listaRuts.remove(rut)
            if cod == nuevo_vuelo:
                listaRuts.append(rut)
        return True

def personas_por_estado(estado):
    vuelDict = dict(vuelos)
    persDict = dict(personas)
    lista=[]

    for cod, (fec, ciudad, est) in salidas:
        if est == estado:
            for rut in vuelDict[cod]:
                datos = persDict[rut]
                nom = datos[0]
                if nom not in lista:
                    lista.append(nom)
    return lista

def filtro_nac(fecha, estado):
    lista=[]
    for rut, (nombre, ciudad, nacimiento, millas) in personas.items():
        estado2 = estado_pasajero(nombre)[2]
        if estado == estado2 and nacimiento > fecha and rut not in lista:
            lista.append(rut)
    return lista
