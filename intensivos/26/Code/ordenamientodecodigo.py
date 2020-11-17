def encriptador(archivo):
    arch = open(archivo)
    temp = open("temp.txt", "w")
    for linea in arch:
        linea = linea.strip()
        linea = linea.replace("paro", "jugar")
        linea = linea.replace("toma", "junta")
        linea = linea.replace("edificio A", "mall")
        linea = linea[::-1]
        temp.write(linea+"\n")
    arch.close()
    temp.close()
    arch = open(archivo, "w")
    temp = open("temp.txt")
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()
    return


def obtenerMayor(archivo):
    arch = open(archivo)
    mayorNum = -float("inf")
    mayorPalabra = ""
    for linea in arch:
        linea = linea.strip().split(";")
        nombre = linea[0]
        archNombre = open(nombre+".txt")
        for linea2 in archNombre:
            num, palabra = linea2.strip().split("-")
            num = float(num)
            if num > mayorNum:
                num = mayorNum
                mayorPalabra = palabra
        archNombre.close()
    arch.close()
    return mayorPalabra
