from patrones import *

def mundo_muerto(ancho, largo):
    mundo = []
    for _ in range(largo):
        col = []
        for _ in range(ancho):
            col.append(0)
        mundo.append(col)
    return mundo

def vecinos_vivos(mundo, x, y):
    suma = 0
    largo = len(mundo)
    ancho = len(mundo[0])
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if 0 <= x+i <= largo-1 and 0 <= y+j <= ancho-1 and (x+i, y+j)!=(x,y):
                suma += mundo[x+i][y+j]
    return suma

def sig_estado(mundo):
    largo = len(mundo)
    ancho = len(mundo[0])
    nuevo_mundo = mundo_muerto(ancho, largo)
    for i in range(largo):
        for j in range(ancho):
            num_vecinos_vivios = vecinos_vivos(mundo, i, j)
            if mundo[i][j] == 1:
                if 2 <= num_vecinos_vivios <= 3:
                    nuevo_mundo[i][j] = 1
                else:
                    nuevo_mundo[i][j] = 0
            else:
                if num_vecinos_vivios == 3:
                    nuevo_mundo[i][j] = 1
                else:
                    nuevo_mundo[i][j] = 0
    return nuevo_mundo

def dibujar(arch, mundo):
    black_sqr = "\u2b1b"
    white_sqr = "\u2b1c"
    largo = len(mundo)
    ancho = len(mundo[0])
    for j in range(ancho):
        linea = ""
        for i in range(largo):
            if mundo[i][j] == 1:
                linea+=white_sqr
            else:
                linea+=black_sqr
        arch.write(linea+"\n")

def leer_mundo(nombre_mundo):
    mtx_fila = []
    arch = open(nombre_mundo)
    for linea in arch:
        fila = list(map(int, linea.strip().split(",")))
        mtx_fila.append(fila)
    arch.close()
    ancho = len(mtx_fila)
    largo = len(mtx_fila[0])
    mundo = []
    for i in range(largo):
        col = []
        for j in range(ancho):
            col.append(mtx_fila[j][i])
        mundo.append(col)
    return mundo

def leer_mundo_por_comando(nombre_mundo):
    arch = open(nombre_mundo)
    primero = True
    for linea in arch:
        if primero:
            ancho, largo = map(int, linea.strip().split(" "))
            mundo = mundo_muerto(ancho, largo)
            primero = False
        else:
            comando, pos = linea.strip().split(" ")
            x, y = map(int, pos.split(","))
            if comando == "glider":
                glider(mundo, x, y)
            elif comando == "t":
                t(mundo, x, y)
            elif comando == "r-pentomino":
                r_pentomino(mundo, x, y)
    arch.close()
    return mundo

def simular(max_generacion, lectura, nombre_mundo):
    if lectura == "comando":
        mundo = leer_mundo_por_comando(nombre_mundo)
    elif lectura == "matriz":
        mundo = leer_mundo(nombre_mundo)
    arch = open(nombre_mundo.split(".txt")[0]+"_simulacion_CGoL.txt", "w"
                , encoding="utf8")
    for gen in range(max_generacion):
        poblacion = 0
        for col in mundo:
            poblacion += col.count(1)
        arch.write("GENERACION:"+str(gen)+"\tPOBLACION:"+str(poblacion)+"\n")
        dibujar(arch, mundo)
        mundo = sig_estado(mundo)
    arch.close()

simular(50, "comando","m2.txt")
simular(50, "matriz", "m1.txt")