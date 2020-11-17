def ingreso_total(entradas):
    total=0
    arch=open(entradas)
    for linea in arch:
        edad=int(linea.strip().split(';')[1])
        if edad<=15:
            total+=1500
        elif edad <=65:
            total+=3500
        else:
            total+=2000
    arch.close()
    return total

def mas_tiempo_en_cine(entradas):
    tiempos={}
    arch=open(entradas)
    for linea in arch:
        nombre,_,_,minutos=linea.strip().split(';')
        minutos=int(minutos)
        if nombre not in tiempos:
            tiempos[nombre]=0
        tiempos[nombre]+=minutos
    arch.close()
    maximo=-float('inf')
    for nombre,minutos in tiempos.items():
        if minutos>maximo:
            maximo=minutos
            mejor_espectador=nombre
    return mejor_espectador
