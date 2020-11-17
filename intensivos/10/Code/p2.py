def producto_escalar(matriz, escalar):
    # En esta lista se almacenara la matriz resultante
    resultado = []
    # Recorremos la matriz en cuestion.
    for fila in matriz:
        # Creamos la lista donde almacenaremos la fila que vamos a calcular.
        fila_nueva = []
        # Recorremos dicha fila.
        for elemento in fila:
            # Calculamos el producto entre el escalar y el elemento de la matriz
            producto = escalar*elemento
            # Almacenamos dicho valor en la fila nueva
            fila_nueva.append(producto)
        # Despues de calcular dicha fila, la agregamos a la matriz resultado.
        resultado.append(fila_nueva)
    return resultado

def suma(matriz_1, matriz_2):
    # Las matrices deben tener las mismas dimensiones
    # para poder sumarlas
    if len(matriz_1) != len(matriz_2):
        return None
    # Creamos una lista donde almacenaremos el resultado de la suma
    resultado = []
    # Normalmente recoreriamos la lista usando un 
    # for i in matriz_1:
    # Pero como queremos recorrer ambas listas simultaneamente, 
    # las recoreremos por los indices.
    for i in range(len(matriz_1)):
        # Revisamos que cada fila de cada matriz tenga la misma dimension.
        if len(matriz_1[i]) != len(matriz_2[i]):
            return None
        # Creamos una nueva lista para almacenar cada fila nueva a procesar.
        fila_nueva = []
        # Al igual que antes, como queremos recorrer 
        # ambas filas de forma simultanea, usaremos los indices para 
        # recorrer ambas filas.
        for j in range(len(matriz_1[i])):
            # Tomamos la fila correspondiente de cada matriz
            fila_matriz_1 = matriz_1[i]
            fila_matriz_2 = matriz_2[i]
            # Tomamos el numero correspondiente de la fila en cuestion
            n1 = fila_matriz_1[j]
            n2 = fila_matriz_2[j]
            # Sumamos los elementos
            suma = n1 + n2
            # Guardamos el resultado calculado en la fila nueva.
            fila_nueva.append(suma)
        # Guardamos la fila calculada en la matriz final
        resultado.append(fila_nueva)
    return resultado

def resta(matriz1, matriz2):
    # Para resolver esta parte, podemos aprovecharnos del hecho de que
    # una resta de dos matrices (M1 - M2) es equivalente a sumar la primera
    # matriz con la segunda matriz multiplicada por -1 (M1 + (-1*M2)).
    # En base a eso, procedemos a multiplicar la segunda matriz por -1.
    matriz_2_negativa = producto_escalar(matriz2, -1)
    # Luego sumamos la matriz1 con el resultado anterior (la matriz 
    # multiplicada por -1) para obtener el resultado buscado.
    resultado = suma(matriz1, matriz_2_negativa)
    return resultado
    # Ojo que tambien hubiera sido valido hacer lo que se hizo en
    # la funcion de suma, pero como queremos optimizar el tiempo, 
    # reutilizamos funciones ya construidas.

def traspuesta(matriz):
    resultado = []
    for j in range(len(matriz[0])):
        nuevo = []
        for i in range(len(matriz)):
            nuevo.append(matriz[i][j])
        resultado.append(nuevo)
    return resultado
