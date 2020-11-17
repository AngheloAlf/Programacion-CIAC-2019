secuencia=input('Ingrese un numero: ')
while secuencia!='Fin':
    i=0 #iterador que indica la posicion dentro del string
    ordenado=True
    while ordenado and i<len(secuencia)-1:
        if secuencia[i]>secuencia[i+1]:
            ordenado=False
        #Tambien se puede hacer lo siguiente fuera del if
        #ordenado=ordenado and secuencia[i]<=secuencia[i+1]
        
        i+=1
    if ordenado: # Algunas personas colocan ordenado==True
                 # pero es redundante
        print('El numero',secuencia,'esta ordenado')
    else:
        print('El numero',secuencia,'no esta ordenado')
    secuencia=input('Ingrese un numero: ')
