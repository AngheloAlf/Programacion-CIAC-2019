autos=[('Impreza',35000,7,9990000,'CC1212'),
       ('Lancer',20000,4,8500000,'GGWP88'),
       ('Palio',45000,10,5000000,'XG1907'),
       ('Camaro',5000,1,30000000,'FMBB80'),
       ('Corsa',23000,5,3500000,'FGDW20'),
       ('i20',50000,8,4500000,'IG2030') ]

categorias=['modelo','kilometraje','antiguedad','precio','patente']

def intersectar(lista1,lista2):
    nueva=[]
    for elemento in lista1:
        if elemento in lista2:
            nueva.append(elemento)
    return nueva

def filtro_categoria(categoria,valor,autos):
    lista=[]
    indice=categorias.index(categoria)
    for auto in autos:
        if auto[indice]<=valor and auto not in lista:
            lista.append(auto)
    return lista

def filtro_compuesto(parametros,valores,autos):
    filtro=list(autos) #Para poder modificar individualmente
    for i in range(len(parametros)):
        lista1=filtro_categoria(parametros[i],valores[i],autos)
        filtro=intersectar(lista1,filtro)
    return filtro

def ranking_con_filtro(parametros,valores,autos,cantidad):
    lista = []
    filtro = filtro_compuesto(parametros,valores,autos)
    for modelo,kms,antig,precio,codigo in filtro:
        lista.append((codigo,kms*antig*precio))
    lista_ord=[]
    for codigo,puntaje in lista:
        lista_ord.append((puntaje,codigo))
    lista_ord.sort()
    mejores=[]
    for i in range(cantidad):
        mejores.append(lista_ord[i][1])
    return mejores
