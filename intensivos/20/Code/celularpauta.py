def traducir_numero(numero):
    lista=[' ','','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    largo=len(numero)
    indice=largo-1
    return lista[int(numero[0])][largo-1]

mensaje_num=input('Ingrese mensaje: ')
mensaje_num+=' '
mensaje_let=''
numeros=''
for caracter in mensaje_num:
    if caracter==' ':
        letra=traducir_numero(numeros)
        mensaje_let+=letra
        numeros=''        
    else:
        numeros+=caracter

print('El mensaje es: '+mensaje_let)

def traducir_letra(letra):
    lista=[' ','','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    numero=0
    for caracteres in lista:
        if letra in caracteres:
            posicion=0
            for caracter in caracteres:
                if caracter==letra:
                    return str(numero)*(posicion+1)
                posicion+=1
        numero+=1

#OTRA OPCION
def traducir_letra2(letra):
    lista=[' ','','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    for numero in lista:
        for i in range(len(numero)):
            if letra==numero[i]:
                return str(lista.index(numero))*(i+1)
    
men_letra=input('Ingrese mensaje: ')
men_numeros=''
for caracter in men_letra:
    men_numeros+=traducir_letra(caracter)
    men_numeros+=' '
print (men_numeros[:-1]) # se coloca el rebanado para evitar imprimir el ultimo espacio
            
            
        
