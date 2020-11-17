def medallasPorPais(arch_medallas):
    medallas={}
    indices_medallas=['Gold','Silver','Bronze']
    archivo=open(arch_medallas)
    contador=1
    for linea in archivo:
        if contador==1:
            contador+=1
        else:
            datos=linea.strip().split(';')
            year,city,sport,discipline,NOC,event,gender,medal=datos
            if NOC not in medallas:
                medallas[NOC]=[0,0,0]
            medallas[NOC][indices_medallas.index(medal)]+=1
    archivo.close()
    return medallas
            
def paisConMasMedallas(arch_medallas):
    medallas=medallasPorPais(arch_medallas)
    maximo=-float('inf')
    mejor=""
    for pais,lista in medallas.items():
        cantidad=sum(lista)
        if cantidad>maximo:
            maximo=cantidad
            mejor=pais
    return mejor

def cantidadDeJuegos(arch_medallas):
    lista=[]
    contador_linea=1
    archivo=open(arch_medallas)
    for linea in archivo:
        if contador_linea==1:
            contador_linea+=1
        else:
            year=linea.strip().split(';')[0]
            if year not in lista:
                lista.append(year)
    archivo.close()
    return len(lista)

def escribirResumen(arch_medallas):
    A='w'
    B=cantidadDeJuegos(arch_medallas)
    C=paisConMasMedallas(arch_medallas)
    D=sum(medallasPorPais(arch_medallas)[C])
    E,F,G=medallasPorPais(arch_medallas)[C]
    H=len(medallasPorPais(arch_medallas))
    I=None
    nuevo=open('Resumen_de_medallas.txt',A) #Complete con la variable correspondiente
    nuevo.write("###### RESUMEN DE MEDALLAS EN JUEGOS OLIMPICOS DE INVIERNO DESDE 1924 HASTA 2006 #######\n")
    nuevo.write('\n')
    nuevo.write('Hasta el momento, estos juegos se han realizado en {0} oportunidades\n'.format(B))
    nuevo.write('El pais que mas medallas ha ganado es {0} con un total de {1} medallas,\ndonde {2} han sido de oro, {3} de plata y {4} de bronce\n'.format(C,D,E,F,G))
    nuevo.write('En total, {0} paises han ganado medallas en estos juegos'.format(H))
    nuevo.close()
    return I
                
    
    
