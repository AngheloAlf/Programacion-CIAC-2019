configuracion=input('Ingrese configuracion (serie/paralelo): ')
cantidad=int(input('Ingrese cantidad de resistencias: '))
contador=1
suma=0.0
while contador<=cantidad:
    resistencia=float(input('Ingrese magnitud de la resistencia '+str(contador)+': '))
    if configuracion=='serie':
        suma+=resistencia
    else:
        suma+=1/resistencia
    contador+=1
if configuracion=='serie':
    print('Req=',suma)
else:
    print('Req=',suma**-1)
    
    
    
                        
