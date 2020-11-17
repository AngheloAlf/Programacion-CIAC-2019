def quienes_ejercitan(usuarios):
    diccionario={}
    # Recorremos nuestro diccionario, considerando tanto sus llaves
    # como sus valores.
    for nombre, lista in usuarios.items():
        for rutina in lista:
            # Si es que no habiamos contabilizado esta rutina antes,
            # la agregamos a nuestro diccionario.
            if rutina not in diccionario:
                diccionario[rutina]=[]
            # Como no queremos contabilizar varias veces a la misma persona
            # dentro de la misma rutina, verificamos que este no se encuentre
            # dentro.
            if nombre not in diccionario[rutina]:
                diccionario[rutina].append(nombre)   
    return diccionario

def rutina_mas_usada(usuarios):
    diccionario={}
    # Contamos que tan usada es cada rutina usando un diccionario
    for las_rutinas in usuarios.values():
        for rutina in las_rutinas:
            if rutina not in diccionario:
                diccionario[rutina]=0
            diccionario[rutina]+=1
    # Usamos algoritmo del mayor para encontrar la rutina mas usada.
    maximo = -float('inf')
    for rutina, repeticiones in diccionario.items():
        if repeticiones > maximo:
            maximo = repeticiones
            mas_repetida = rutina
    return mas_repetida

def crear_plantilla(rutinas,usuarios,series,nombre):
    nuevo=open('rutina de '+str(nombre)+'.txt','w')
    # Esto es para que se vea bonito.
    nuevo.write('{0} esta es tu rutina de ejercicios\n'.format(nombre))
    nuevo.write('####################################\n')
    total = 0
    # Recorremos las rutinas de la persona que se nos indica.
    for rutina in usuarios[nombre]:
        # Mensaje bonito
        nuevo.write('Entrenamiento {0}\n'.format(rutina))
        # Iteramos segun la cantidad de series de la rutina en cuestion.
        for i in range(series[rutina]):
            nuevo.write('\tRonda {0} de {1}\n'.format(i+1,series[rutina]))
            # Buscamos los ejercicios de la rutina en la que vamos.
            for ejercicio, repeticiones in rutinas[rutina]:
                # Escribimos un mensaje indicando los datos de este ejercicio.
                formato = '\t\t {0}\t {1} repeticiones\n'
                nuevo.write(formato.format(ejercicio,repeticiones))
                # Contamos la cantidad de repeticiones de de cada ejercicio.
                total += repeticiones
    nuevo.write('\n')
    nuevo.write('En total hiciste: ')
    nuevo.write(str(total))
    nuevo.write(' repeticiones de ejercicios\n')
    nuevo.close()
    return None
