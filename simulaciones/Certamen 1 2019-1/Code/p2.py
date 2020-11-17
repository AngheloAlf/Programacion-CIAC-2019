def valor(plazo,devolucion,objeto,demanda):
    if devolucion<=plazo:
        return 0
    hr_inicio=plazo//100
    min_inicio=plazo%100
    hr_final=devolucion//100
    min_final=devolucion%100
    minutos=hr_final*60+min_final-hr_inicio*60-min_inicio
    if objeto=='libro':
        if demanda=='alta':
            return minutos*30
        else:
            return minutos*10
    elif objeto=='calculadora':
        return minutos*50
    else:
        if demanda=='alta':
            return minutos*5
        else:
            return minutos

n=int(input('Ingrese numero de elementos a cobrar: '))
contador=1
total=0
demanda='' #Solo en caso de que el primer objeto sea una calculadora
while contador<=n:
    objeto=input('Ingrese objeto '+str(contador)+': ')
    if objeto!='calculadora':
        demanda=input('Ingrese demanda [alta/baja]: ')
    inicio=int(input('A que hora debia devolverlo? [HHMM]: '))
    final=int(input('A que hora lo devolvio? [HHMM]: '))
    total+=valor(inicio,final,objeto,demanda)
    contador+=1
print('El total de multas fue de',total)
        
        
    
