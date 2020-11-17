sangres=['O-','O+','A-','A+','B-','B+','AB-','AB+']
matriz=[
    [1,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,0,0,0,1,0,0,0],
    [1,1,0,0,1,1,0,0],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,1]
    ]

gente=[
    ('Javiera', 'A+'),
    ('Macarena', 'AB+'),
    ('Antonio', 'O+'),
    ('Pedro', 'B+'),
    ('Daniela', 'O-'),
    ('Felipe', 'A+'),
    ('Valeria', 'B-'),
    ('Jose', 'O+'),
    ('Federico', 'AB+')
    ]

def tipos_donantes(tipo_sangre,matriz,sangres):
    indice=sangres.index(tipo_sangre)
    lista=[]
    contador=0
    for posible_donante in matriz[indice]:
        if posible_donante: #se puede agregar ==1, pero 1 es True y 0 es False
            lista.append(contador)
        contador+=1
    nueva=[]
    for indice in lista:
        nueva.append(sangres[indice])
    return nueva

def donantes(gente,tipo):
    personas=[]
    tipos_don=tipos_donantes(tipo,matriz,sangres)
    for nombre,grupo_sanguineo in gente:
        if grupo_sanguineo in tipos_don:
                personas.append((nombre,grupo_sanguineo))
    return personas

def sobrevive(max_donacion,requerida,tipo_sanguineo):
    tipos=tipos_donantes(tipo_sanguineo,matriz,sangres)
    personas=donantes(gente,tipo_sanguineo)
    cantidad=len(personas)
    return cantidad*max_donacion>=requerida

