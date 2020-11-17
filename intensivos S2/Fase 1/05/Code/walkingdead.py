grupo = {'rick':(172,10),'daryl':(136,11),'michonne':(80,6),'glenn':(73,0),
         'maggie':(55,4),'carl':(62,1),'tyreese':(35,0),'carol':(17,3) }

def total(grupo):
    walkers=0.0
    humanos=0.0
    for w,h in grupo.values():
        walkers+=w
        humanos+=h
    return walkers,humanos

def puntaje(grupo):
    t_walkers,t_humanos=total(grupo) #t de total
    puntos={}
    for nombre,(w,h) in grupo.items():
        puntuacion=w/t_walkers +2*(h/t_humanos)
        puntos[nombre]=round(puntuacion,2)
    return puntos

def ranking(grupo):
    ordenada=[]
    for nombre,puntos in puntaje(grupo).items():
        ordenada.append((puntos,nombre))
    ordenada.sort()
    ordenada.reverse()
    lista=[]
    for puntos, nombre in ordenada:
        lista.append(nombre)
    return lista
    
    
        
