def buscarPais(listaPaises, nombre_del_pais):
    for numero, nombre in listaPaises:
        if nombre == nombre_del_pais:
            return numero
    return 0

def encontrarCoordenadas(mundo, numero_del_pais):
    for y in range(len(mundo)):
        for x in range(len(mundo[y])):
            if mundo[y][x] == numero_del_pais:
                return (x, y)
    return (0, 0)

# Funcion auxiliar
def distanciaEntrePuntos(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2-x1
    dy = y2-y1
    return (dx**2 + dy**2)**0.5

def estimarPrecio(planeta, listaPaises, origen, destino):
    numero_origen = buscarPais(listaPaises, origen)
    numero_destino = buscarPais(listaPaises, destino)
    coord_origen = encontrarCoordenadas(planeta, numero_origen)
    coord_destino = encontrarCoordenadas(planeta, numero_destino)
    distancia = distanciaEntrePuntos(coord_origen, coord_destino)
    dolar_por_kilometro = 0.2
    return distancia * dolar_por_kilometro * 1000


def calcularRuta(planeta, listaPaises, ruta):
    precioTotal = 0
    for i in range(len(ruta) - 1):
        origen = ruta[i]
        destino = ruta[i+1]
        precioTotal += estimarPrecio(planeta, listaPaises, origen, destino)
    return precioTotal
