def agregarVendedor(lista_vendedores, lista_ventas, nombre):
    lista_vendedores.append(nombre)
    for mes in lista_ventas:
        # A cada mes le agregamos la lista respectiva de nuestro
        # nuevo vendedor.
        mes.append([])
    # Esta parte se puede omitir.
    return None

# Funcion auxiliar que se encarga de convertir el numero de mes a un
# indice de la lista de ventas mensuales, respetando el anno fiscal.
def mes_indice(mes):
    if mes >= 5:
        return mes - 5
    else:
        return mes + 7

def resumenMensual(vendedores, ventas, mes):
    # Contadores.
    recaudado = 0
    elementos_vendidos = 0
    precios_unitarios = 0
    # Obtenemos la lista correspondiente del mes que nos piden.
    indice_mes = mes_indice(mes)
    lista_mes = ventas[indice_mes]
    # Recorremos dicha lista.
    for datos_mes in lista_mes:
        # Desempaquetamos la tupla de producto inmediatamente.
        for nom, cantidad, plata, dia in datos_mes:
            # Sumamos los datos pedidos.
            recaudado += plata
            elementos_vendidos += cantidad
            precios_unitarios += plata/cantidad
    # Armamos la tupla y retornamos
    return (recaudado, elementos_vendidos, precios_unitarios)

def resumenAnual(vendedores, ventas):
    # Para esta funcion, nos aprovecharemos de que la funcion anterior realiza
    # exactamente lo mismo, pero por cada mes, por ende, la llamaramos para
    # cada mes y lo que nos entregue lo guardaremos en una lista de resultado.
    meses = [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
    resultado = []
    for i in meses:
        tupla = resumenMensual(vendedores, ventas, i)
        resultado.append(tupla)
    return resultado



def vendioProducto(vendedores, lista_ventas, vendedor, nom_producto, fecha):
    dia, mes = fecha
    mes = mes_indice(mes)
    # Obtenemos el indice del vendedor en la lista de vendedores.
    # Asumiremos que dicho vendedor siempre existe en la lista.
    indice = vendedores.index(vendedor)
    lista_mes = lista_ventas[mes]
    # Como sabemos que la cada mes tiene cada vendedor en el mismo orden que 
    # la lista de vendedores, usamos ese indice para saber donde estan sus 
    # ventas en la lista del mes.
    ventas_del_vendedor = lista_mes[indice]
    for producto in ventas_del_vendedor:
        nom, cantidad, plata, dia2 = producto
        # Recorremos la lista, buscando la tupla que tiene el nombre, 
        # considerando que debe ser el mismo dia que el estipulado.
        if nom_producto == nom and dia==dia2:
            # Si la encontramos, retornamos la tupla.
            return producto
    return None


def agregarVenta(vendedores, ventas, nombre, informacion_venta):
    fecha, nom_producto, cantidad, precio_unitario = informacion_venta
    # Revisamos si el vendedor ya vendio el producto en dicho dia.
    # Esto es importante, debido a que si se vendio varias veces el mismo 
    # producto, este debe ser agregado una unica vez, pero acumulando las 
    # cantidades y dinero vendidos.
    se_vendio = vendioProducto(vendedores, ventas, nombre, nom_producto, fecha)

    dia, mes = fecha
    mes = mes_indice(mes)
    indice = vendedores.index(nombre)
    if se_vendio != None:
        # Si el vendedor vendio el producto en cuestion, se mezclan ambas 
        # ventas y se almacena el resultado.
        # Aqui se obtiene el indice del producto.
        indice_2 = ventas[mes][indice].index(se_vendio)
        # Aqui se recalculan los nuevos datos de venta.
        _, cantidad_antigua, dinero, dia = se_vendio
        cantidad_nueva = cantidad_antigua + cantidad
        dinero_nuevo = dinero + cantidad*precio_unitario
        # Aqui se genera la nueva tupla con los datos en cuestion.
        tupla = (nom_producto, cantidad_nueva, dinero_nuevo, dia)
        # Se reemplaza la tupla antigua con los datos nuevos..
        ventas[mes][indice][indice_2] = tupla
    else:
        # Este caso ocurre si el vendedor no ha vendido el producto el dia 
        # de hoy.
        posicion = 0
        # Buscamos en que posicion debemos agregar la venta, debido a que 
        # esto debe estar ordenado segun el dia del mes.
        for i in range(len(ventas[mes][indice])):
            _, _, _, dia2 = ventas[mes][indice][i]
            if dia > dia2:
                posicion = i
        tupla = (nom_producto, cantidad, cantidad*precio_unitario, dia)
        # Lo agregamos en la posicion que encontramos.
        ventas[mes][indice].insert(posicion, tupla)
    return None

def eliminarVendedor(vendedores, ventas_mensuales, nombre):
    if nombre in vendedores:
        # Obtenemos la posicion del vendedor.
        indice = vendedores.index(nombre)
        # Eliminamos al vendedor de la lista de vendedores.
        vendedores.remove(nombre)
        for mes in ventas_mensuales:
            # Removemos al vendedor de cada mes en cuestion.
            del mes[indice]
    return None
