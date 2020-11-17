# funcion 1:
def areaPozo(diametro, profundidad):
    pi        = 3.14
    perimetro = float(diametro) * pi
    area      = perimetro * float(profundidad)
    return area
    
# funcion 2:
def volumenPozo(diametro, profundidad, nivel):
    pi    = 3.14
    radio = float(diametro) / 2.0
    area  = pi * radio ** 2
    volumen = area * float(profundidad - nivel)
    return volumen
    
# Programa
print 'Posos Ltda'
print 'Bienvenido al calculador de costo'
diametro    = int(raw_input('Ingrese el diametro del poso a construir: '))
profundidad = int(raw_input('Ingrese la profundidad de la excavacion : '))
nivel       = int(raw_input('Ingrese el nivel de profundidad de agua : '))

excavacion  = 1000.0 * float(profundidad)
pared       =  100.0 * areaPozo(diametro, profundidad)
inscripcion =   50.0 * volumenPozo(diametro, profundidad, nivel) 

costo = excavacion + pared + inscripcion
print 'El costo de excavacion corresponde a: $', costo
