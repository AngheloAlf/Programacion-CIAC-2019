def contar(lista):
    diccionario={}
    for numero in lista:
        if numero not in diccionario:
            diccionario[numero]=0
        diccionario[numero]+=1
    return diccionario