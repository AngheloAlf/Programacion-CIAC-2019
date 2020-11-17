def multiplicar(A,B):
    matriz=[]
    filasA=len(A)
    colB=len(B[0])
    filasB=len(B)
    for i in range(filasA):
        lista=[]
        for j in range(colB):
            lista.append(0)
        matriz.append(lista)
    for y in range(colB):
        for x in range(filasA):
            for z in range(filasB):
                matriz[x][y]+=A[x][z]*B[z][y]
    return matriz
