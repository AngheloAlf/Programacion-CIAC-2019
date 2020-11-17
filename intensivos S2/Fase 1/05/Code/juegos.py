juegos={'Left 4 Dead 2':('valve',['terror','cooperativo','shooter'],[112,314]),
        'Counter Strike':('valve',['shooter','cooperativo'],[112,414,908]),
        'League of Legends':('riot',['moba','cooperativo'],[112,314,908]),
        'Red Alert 2':('CAC',['RTS'],[112,314]),
        'Age of Empires':('Microsoft',['RTS'],[408,509])
        #...
        }

def total_jugadores(juegos):
    lista=list()
    for _,(_,_,jugadores) in juegos.items():
        for jugador in jugadores:
            if jugador not in lista:
                lista.append(jugador)
    return lista

def cantidad(jugador,juegos):
    contador=0
    for _,_,lista in juegos.values():
        if jugador in lista:
            contador+=1
    return contador

def conocidos(jugador,juegos):
    amigos=[]
    for _,(_,_,lista) in juegos.items():
        if jugador in lista:
            for amigo in lista:
                if amigo!=jugador and amigo not in amigos:
                    amigos.append(amigo)
    return amigos

def preferencia(jugador,juegos):
    diccionario={}
    for _,(_,categorias,jugadores) in juegos.items():
        if jugador in jugadores:
            for categoria in categorias:
                if categoria not in diccionario:
                    diccionario[categoria]=0
                diccionario[categoria]+=1
    maximo=-float('inf')
    for categoria,cantidad in diccionario.items():
        if cantidad>maximo:
            preferido=categoria
            maximo=cantidad
    return preferido

def crear_diccionario(juegos):
    jugadores=total_jugadores(juegos)
    nuevo={}
    for jugador in jugadores:
        prefiere=preferencia(jugador,juegos)
        conoce=conocidos(jugador,juegos)
        tiene=cantidad(jugador,juegos)
        nuevo[jugador]=(prefiere,conoce,tiene)
    return nuevo
        
        

                
