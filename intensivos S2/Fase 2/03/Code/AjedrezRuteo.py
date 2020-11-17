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


