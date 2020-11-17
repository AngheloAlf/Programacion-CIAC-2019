#Retorna tramo de la estacion correspondiente
def tramo(estacion):
    for tupla in tramos:
        if estacion in tupla:
            return tupla[0]        

#Entrega el costo del viaje dependiendo el tipo de tarifa y estaciones
def costo_viaje(origen,destino,tipo):
    tipos=['baja','media','alta']
    indice=tipos.index(tipo)+2
    tramo_origen=tramo(origen)
    tramo_destino=tramo(destino)
    for tupla in tarifas:
        TO,TD,_,_,_=tupla
        if TO==tramo_origen and TD==tramo_destino:
            return tupla[indice]    

def actualizar_saldo(estacion_origen, estacion_destino, codigo_tarjeta,tipo_tarifa):
    for codigo, monto in tarjetas:
        if codigo_tarjeta==codigo:
            saldo=monto
    costo=costo_viaje(estacion_origen,estacion_destino,tipo_tarifa)
    print("Costo del viaje:",costo)
    if costo>=saldo:
        print("Saldo insuficiente")
    else:
        print("Nuevo saldo:",saldo-costo)
        print("Muchas gracias")
    
    #Se actualiza lista de tarjetas
    for tarjeta in tarjetas:
        if tarjeta[0]==codigo_tarjeta:
            indice=tarjetas.index(tarjeta)
            tarjetas[indice]=[codigo_tarjeta,saldo-costo]
            return tarjetas
