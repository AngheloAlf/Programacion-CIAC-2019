def cant_divisores(numero):
    cantidad=0
    i=1
    while i<=numero:
        if numero%i==0:
            cantidad+=1
        i+=1
    return cantidad

def es_primo1(numero): #usando la funcion anterior
    if cant_divisores(numero)==2:
        return True
    return False

def es_primo2(numero): #Sin usar la funcion anterior
    if numero==2:
        return True
    cont=2
    while cont<(numero**0.5)+1: #Solo para hacerlo mas eficiente
        if numero%cont==0:      #Si usa cont<numero tambien sirve
            return False
        cont+=1
    return True

#Cuantos numeros primos existen hasta n
n=int(input('Ingrese numero maximo: '))
cantidad=0
suma=0
numero=2
while numero<=n:
    if es_primo2(numero):
        cantidad+=1
        suma+=numero
    numero+=1
print('Hasta el numero',n,'existen',cantidad,'primos')
print('La suma de estos es',suma)
    
    
    
