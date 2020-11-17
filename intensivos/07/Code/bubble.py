def bubble_sort(lista):
    contador=0 #tiene como fin contar cuantos numeros estan ordenados
    fin=len(lista) #indica el ultimo numero a iterar
    while contador<len(lista):
        i=0 #indice del iterador
        while i+1<fin:
            if lista[i]>lista[i+1]:
                temp=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=temp
                #este paso se puede hacer tambien como
                #lista[0],lista[1]=lista[1],lista[0]
            i+=1
        fin-=1
        contador+=1
    return None