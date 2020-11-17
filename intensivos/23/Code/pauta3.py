encomiendas = [
(10234, (90, 90, 50)),
(34102, (100, 140, 20)),
(36890, (25, 50, 70)),
# ...
]
destinos = [
(10234, (-4, 15)),
(36890, (2, 4)),
(34102, (40, -13)),
# ...
]

# Esta funcion toma 2 puntos y entrega la distancia entre ellos.
# punto1 y punto2 son tuplas con los puntos a calcular su distancia.
def distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# Calcula el volumen de la valija.
def volumen(valija):
    largo, alto, ancho = valija
    return largo * alto * ancho

# Calcula el ingreso estimado de dicho envio.
def ingreso(valija, origen, destino):
    return 0.1 * volumen(valija) * distancia(origen, destino)

# Esta funcion busca el destino de el codigo entregado en la lista destinos.
def buscar_destino(destinos, codigo):
    for codi, dest in destinos:
        if codigo == codi:
            return dest

def viajes_a_realizar(encomiendas, destinos):
    # Anotamos la velocidad y el tiempo maximo de los camiones.
    velocidad = 60 # km/hr
    tiempoMaximo = 0.5 # hrs
    distancia_maxima = velocidad * tiempoMaximo
    # Anotamos el punto de origen de la empresa.
    origen = (0, 0)

    # Como nos piden una lista ordenada segun el ingreso que nos dara cada
    # viaje, creamos una lista de tuplas, donde cada tupla contiene el dinero 
    # que nos aporta dicho viaje y el codigo de dicha valija. Esto nos servira 
    # para ordenarla segun el ingreso mas facilmente mas adelante.
    dinero_y_valijas = []

    # Recorremos las encomiendas
    for codigo, dimensiones in encomiendas:
        # Obtenemos el destino de esta encomienda especifica.
        destino = buscar_destino(destinos, codigo)

        # Calculamos la distancia, con el objetivo de asegurarnos de que no 
        # sobrepase el limite que nos indicaron.
        dist = distancia(origen, destino)
        if dist <= distancia_maxima:
            # Calculamos el ingreso que nos generaria dicho envio.
            dinero = ingreso(dimensiones, origen, destino)
            # Al crear la tupla que agregaremos, ponemos primero el dinero que 
            # obtendremos y luego el codigo. Asi podremos ordenarlo por la 
            # cantidad de dinero.
            tupla = (dinero, codigo)
            dinero_y_valijas.append(tupla)

    # Oredenamos nuestra lista. Como el dinero esta primero en cada tupla, 
    # ordenara segun eso primero.
    dinero_y_valijas.sort()
    # Al hacerle un reverse, quedaran primero los que den mayores ingresos 
    # al hacer el envio.
    dinero_y_valijas.reverse()

    # Creamos la lista que contrendra unicamente los codigos.
    lista_viajes = []

    for _, codigo in cantidad:
        # Nos indican que podemos tener a lo mas 10 codigos, verificamos 
        # cuantos llevamos antes de agregar un codigo nuevo.
        if len(lista_viajes) < 10:
            lista_viajes.append(codigo)

    return lista_viajes

print(viajes_a_realizar(encomiendas, destinos))
