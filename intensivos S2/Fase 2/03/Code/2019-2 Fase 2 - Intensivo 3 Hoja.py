# Pregunta 1 - PyAjedrez

tablero = [
    ["t","a"," "," ","t"],
    ["p"," ","p"," ","p"],
    [" "," "," "," "," "],
    [" ","p","P"," ","P"],
    ["T"," "," "," ","T"]]

valores = {
    "P":1,
    "T":5,
    "C":3,
    "A":3}


## 1.1

def calcularPuntajeJugadores(tablero, valores):

    # Rellene aqui.

    print("")
    return (0, 0)


# Pruebe la función anterior:
## print(calcularPuntajeJugadores(tablero,valores))



## 1.2

def traducirJugada(jugada, turno):
    valido = False
    inicio = (0, 0)
    destino = (0, 0)

    # Rellene aqui.

    tupla_resultante = (valido, (inicio, destino))
    print(">>>", tupla_resultante)
    return tupla_resultante


# Pruebe la función anterior: (elimine los """)
"""
turno = 1
seguirJugando = True
while seguirJugando:
    turno = (turno+1)%2
    print("Juega el jugador", turno+1)
    jugada = input("Ingrese su jugada: ")
    contador = 5
    while traducirJugada(jugada,turno)[0] == False and contador > 0:
        contador -= 1
        if contador == 0:
            print ("Gana el jugador "+str((turno+1)%2+1)+" por jaque mate")
            seguirJugando = False
        jugada = input("Jugador "+str(turno+1)+" ingrese una jugada valida: ")
"""




# Pregunta 2 - PyMaps

## 2.1

def AgregarComentario(usuario, nota, blablabla, nombreLocal):

    # Pongale master

    return

# coronavirus
## AgregarComentario('VaneDM', 4, 'Muy bueno pero algo caro', 'Casa Lila')



def ActualizarNota(archivo, local):

    # Alguien leerá estos comentarios?

    return


# Saquenme de este sufrimiento llamado "fases online"
## ActualizarNota('locales.txt', 'Casa Lila')



# Pregunta 3 - Ruteo

## Para ver que es lo que imprime el ruteo, borra los """ del inicio y del final.

"""
def validarMovimientoAlfil(tablero,actual,objetivo,pieza):
    y1,x1 = actual
    y2,x2 = objetivo
    puede = False
    if actual == objetivo:
        return puede
    if tablero[y1][x1].islower() and tablero[y2][x2].islower():
        return puede
    if tablero[y1][x1].isupper() and tablero[y2][x2].isupper():
        return puede
    if x2+y2 == x1+y1:
        puede = True
        if y2 > y1:
            for i in range(1,y2-y1):
                if tablero[y1+i][x1-i] != " ":
                    puede = False
        else:
            for i in range(1,y1-y2):
                if tablero[y1-i][x1+i] != " ":
                    puede = False
    if x2-y2 == x1-y1:
        puede = True
        if x2 > x1:
            for i in range(1,x2-x1):
                if tablero[y1+i][x1+i] != " ":
                    puede = False
        else:
            for i in range(1,x1-x2):
                if tablero[y1-i][x1-i] != " ":
                    puede = False
    return puede              

tablero = [
    ["t","a","c","a","t"],
    ["p"," ","p","p","p"],
    [" "," "," "," "," "],
    [" ","p","P","P","P"],
    ["T","A","C","A","T"]]

origen = (4,1)
destino = (1,4)
pieza = tablero[origen[0]][origen[1]]
for i in range(2):
    if pieza.upper() == "A":
        if validarMovimientoAlfil(tablero,origen,destino,pieza):
            print ("se puede")
        else:
            print ("no se puede")
        destino = (3,0)
"""



