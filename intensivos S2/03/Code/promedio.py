suma=0.0 #Para que el resultado sea flotante
cont=0.0
op=int(input('Ingrese dato: '))
while op!=-1:
    suma+=op
    cont+=1
    op=int(input('Ingrese dato (-1 para salir): '))
print ('El promedio de los datos es', round(suma/cont,1))
#Promedio redondeado a un decimal
