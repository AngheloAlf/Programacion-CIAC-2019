# Se pasan los datos a una lista
numeros=[]
arch=open('triangulo.txt')
for linea in arch:
    fila=list(map(int,linea.strip().split()))
    numeros.append(fila)
arch.close()
# Asumiendo que los datos están ordenados en una lista de listas,
# donde cada lista es una de las filas del triangulo

N=len(numeros) # Se obtiene numero de filas del triangulo

# Se recorre cada fila desde la segunda base hacia arriba
for i in range(-2,-N-1,-1):
    # Se recorre cada numero de la fila de la base i
    for j in range(len(numeros[i])):
        # A cada numero se le suma el mayor numero posible con la funcion max
        numeros[i][j]+=max(numeros[i+1][j],numeros[i+1][j+1])
# Se imprime maximum path sum o suma maxima de ruta
print(numeros[0][0])
        
    
    
