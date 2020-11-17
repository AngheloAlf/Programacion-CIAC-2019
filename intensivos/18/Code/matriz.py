# Se crea una variable para leer un archivo
arch=open('grid.txt')
# Se crea la matriz para guardar los numeros de la grilla
matriz=[]
# Con un ciclo for se recorre el archivo linea (horizontal) por linea
for linea in arch:
    # Comando strip quita un caracter especial de salto de linea en el
    # extremo derecho, lo que se logra apretando enter generalmente

    # El comando split crea una lista a partir de un string separando
    # los numeros por los espacios, estos numeros quedan en formato de string

    #Para transformar cada numero de string a entero se utiliza la funcion map
    # y posteriormente se genera una lista (map retorna un generador, parecido
    # a lo que hace la funcion range)
    lista=list(map(int,linea.strip().split()))

    #Luego se agrega esta lista de numeros a la matriz
    matriz.append(lista)
#Para evitar problemas, y como regla general, se cierra el archivo
#despues de haber sido leido
arch.close()

#Ahora puede probar la matriz creada
for fila in matriz:
    print(fila)



    
