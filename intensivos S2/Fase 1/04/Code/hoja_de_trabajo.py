## Pregunta 1

def contar_letras(palabra):
    dicc = dict()
    # Escriba su codigo
    return dicc

#print(contar_letras('Ciac'))
#print(contar_letras('Intensivo'))


def son_anagramas(p1, p2):
    # Escriba su codigo
    return False

#print(son_anagramas('grite','tigre'))
#print(son_anagramas('ciac','progra'))


def es_panvocalica(palabra):
    # Escriba su codigo
    return False

#print(es_panvocalica('neumatico'))
#print(es_panvocalica('panvocalica'))


def en_orden(palabra):
    # Escriba su codigo
    return False

#print(en_orden('himnos'))
#print(en_orden('zapato'))


def en_orden_segun(palabra, guia):
    # Escriba su codigo
    return False

#print(en_orden_segun('intensivo','iso'))
#print(en_orden_segun('limitacion','amc'))


def palabras_repetidas(oracion):
    # Escriba su codigo
    return False

#print(palabras_repetidas('El sobre esta sobre el escritorio'))
#print(palabras_repetidas('este intensivo es entretenido'))



## Pregunta 2


animales=[
    #(nombre cientifico, nombre comun, f_nacimiento,correo)
    ('Panthera tigris','tigre',(1972,7,20),'tiger@animail.in'),
    ('Vultur gryphus','condor',(1989,4,27),'condorito@pelotillehue.cl'),
    ('Macropus fuliginosus','canguro',(1986,10,18),'rocko@animail.au'),
    ('Elephas maximus','elefante asiatico',(1973,11,10),'lfant@chinchan.wa.cn'),
    ('Loxodonta africana','elefante africano',(1993,7,8),'orejon@wakawaka.za')
    ]

paises={
    'in':'India',
    'cl':'Chile',
    'au':'Australia',
    'cn':'China',
    'za':'Sudafrica',
    'ar':'Argentina',
    'ch':'Suiza'
    }
    
meses=['enero','febrero','marzo','abril','mayo','junio','julio',
       'agosto','septiembre','octubre','noviembre','diciembre']


def listaPaises(animales):
    lista = []
    # Pongale con el codigo
    return lista

#print(listaPaises(animales))


def animalMasJoven(animales):
    jovencito = ''
    # Escriba codigo bonito
    return jovencito

#print(animalMasJoven(animales))


def obtenerCumpleaneros(animales, mes):
    lista = list()
    # Escriba codigo pulento
    return lista

#print(obtenerCumpleaneros(animales, 'julio'))


def depositar(animal, monto, archivo):
    # Escriba codigo bakan
    return ''

#print(depositar('canguro', 10, 'saldos.txt'))


def sacarDinero(animal,monto,archivo):
    # Escriba codigo bakan
    return ''

#print(sacarDinero('canguro', 200, 'saldos.txt'))
#print(sacarDinero('condor', 100, 'saldos.txt'))
