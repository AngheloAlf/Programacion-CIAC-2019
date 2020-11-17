regiones = [
# (numero, nombre, poblacion, superficie, capital)
  ("XV",   "Region de Arica y Parinacota", 226068,  16873.3, "Arica"), 
  ("I",    "Region de Tarapaca",           581802,  42225.8, "Iquique"), 
  ("II",   "Region de Antofagasta",        607534, 126049.1, "Antofagasta"),
  ("III",  "Region de Atacama",            286168,  75176.2, "Copiapo"),
  ("IV",   "Region de Coquimbo",            757586,  40579.9, "La Serena"),
  ("V",    "Region de Valparaiso",        1815902,  16396.1, "Valparaiso"),
  ("RM",   "Region Metropolitana",        7112808,  15403.2, "Santiago"),
  ("VI",   "Region de O'Higgins",          914555,  16387.0, "Rancagua"),
  ("VII",  "Region del Maule",            1044950,  30296.1, "Talca"),
  ("XVI",  "Region de Nuble",              480609,  13178.5, "Chillan"),
  ("VIII", "Region del Biobio",           1556805,  23890.2, "Concepcion"),
  ("IX",   "Region de La Araucania",       957224,  31842.3, "Temuco"),
  ("XIV",  "Region de Los Rios",           384837,  18429.5, "Valdivia"),
  ("X",    "Region de Los Lagos",          828708,  48583.6, "Puerto Montt"),
  ("XI",   "Region de Aysen",              103158, 108494.4, "Coyhaique"),
  ("XII",  "Region de Magallanes",         166533, 132297.2, "Punta Arenas")
]

zonas = [
  ("norte grande", ["XV", "I", "II"]),
  ("norte chico",  ["III", "IV"]), 
  ("zona central", ["V", "RM", "VI", "VII", "XVI", "VIII"]),
  ("zona sur",     ["IX", "XIV", "X"]),
  ("zona austral", ["XI", "XII"])
]

def buscar_region(regiones, numero):
    pos_region = 0
    region_encontrada = ()
    # Recorremos la lista de regiones segun su indice.
    # Usamos el indice para recorrer para asi tener la posicion de la region
    # con respecto a la lista.
    for i in range(len(regiones)):
        reg = regiones[i]
        if reg[0] == numero:
            # En caso de que la region corresponda a la pedida, almacenamos
            # dichos datos
            pos_region = i
            region_encontrada = reg
    return (pos_region, region_encontrada)

def densidad_por_zona(regiones, zonas):
    lista_final = []
    for nombre, regiones_de_la_zona in zonas:
        # Primero necesitamos calcular la poblacion y superficie total de 
        # la zona en cuestion.
        pobla_total = 0.0
        superf_total = 0.0
        for numero in regiones_de_la_zona:
            # Usamos la funcion anterior para obtener los datos de cada 
            # region de la zona
            _, region = buscar_region(regiones, numero)
            # Desempaquetamos la tupla. 
            # Los guiones bajos los usamos para explicitar que no nos
            # interesan los valores en esas posiciones.
            _, _, pobla, superf, _ = region
            pobla_total += pobla
            superf_total += superf
        # Calculamos la densidad y la agregamos a la lista como una tupla.
        densidad = pobla_total/superf_total
        tupla = (nombre, densidad)
        lista_final.append(tupla)
    return lista_final

def cambiar_region(regiones, numero, datos):
    # Buscamos la posicion de la region
    posicion, _ = buscar_region(regiones, numero)
    # Desempaquetamos los datos nuevos
    nombre, poblacion, superficie, capital = datos
    # Y lo reempaquetamos respetando la estructura inicial.
    nuevos_datos = (numero, nombre, poblacion, superficie, capital)
    # Reemplazamos la region correspondiente.
    regiones[posicion] = nuevos_datos
    return


def crear_region(regiones, zonas, nueva_region, numero_antigua):
    posicion, region_antigua = buscar_region(regiones, numero_antigua)

    # primer punto
    # Sumamos 1 a la posicion para que se inserte despues de la region 
    # anterior.
    regiones.insert(posicion+1, nueva_region)

    # segundo punto
    # Desempaquetamos ambas regiones
    _, nombre, pobla, superf, capital = region_antigua
    numero_nuevo, _, pobla_nueva, superf_nueva, _ = nueva_region
    # Disminuimos la poblacion y superficie de la region anterior.
    pobla -= pobla_nueva
    superf -= superf_nueva
    # Empaquetamos la tupla con el formato que requiere la funcion
    # que se encarga de actualizar las regiones.
    datos = (nombre, pobla, superf, capital)
    cambiar_region(regiones, numero_antigua, datos)

    # tercer punto
    for nombre_zona, lista_numeros in zonas:
        # Buscamos la zona que contiene la region antigua.
        if numero_antigua in lista_numeros:
            # Cuando la encontremos, agregamos la nueva region a dicha zona.
            lista_numeros.append(numero_nuevo)
    return

regi = buscar_region(regiones, "XI")
print(regi)

lista_densidades = densidad_por_zona(regiones, zonas)
print(lista_densidades)

datos =  ("Region de Tarapaca", 750000, 42225.8, "Iquique")
cambiar_region(regiones, "I", datos)
print(regiones[0:3])

nueva_region = ("XVII", "Republica independiente de Placeres", 2790, 30, "USM")
crear_region(regiones, zonas, nueva_region, "V")
print(regiones[4:8])
