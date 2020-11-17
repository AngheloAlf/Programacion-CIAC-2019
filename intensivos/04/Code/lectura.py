palabra=input('Ingrese palabra: ')
indice=0
vocales=0
while indice<len(palabra):
    if palabra[indice] in 'AEIOUaeiou':
        vocales+=1
    indice+=1
print('La palabra',palabra,'tiene',vocales,'vocales')

        
