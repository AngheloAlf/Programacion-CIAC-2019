def ordenar(nombres,alias,poderes):
    contador=0
    fin=len(nombres)
    while contador<len(lista):
        i=0
        while i+1<fin:
            if nombres[i]>nombres[i+1]:
                nombres[i],nombres[i+1]=nombres[i+1],nombres[i]
                alias[i],alias[i+1]=alias[i+1],alias[i]
                poderes[i],poderes[i+1]=poderes[i+1],poderes[i]
            i+=1
        fin-=1
        contador+=1
    return None

ordenar(nombres,alias,poderes)
for i in range(len(nombres)):
    mensaje=nombres[i]+', '
    
    if alias[i]!='-':
        mensaje+='a.k.a. '+alias[i]+', '
    if ' y ' in poderes[i]:
        mensaje+='sus habilidades son '+poderes[i]
    else:
        mensaje+='su habilidad es '+poderes[i]
    print(mensaje)
