def alimento(ali, arch):
    estadisticas = dict()

    arch_comida = open(arch)
    for linea in arch_comida:
        datos = linea.strip().split(";")
        nombre, feli, satis = datos

        if nombre == ali:
            estadisticas["feliz"] = int(feli)
            estadisticas["satisfecho"] = int(satis)
    arch_comida.close()

    if len(estadisticas) == 2:
        return estadisticas
    return False

def status(tomo, arch):
    estadisticas = dict()
    esta_muerto = False
    estaba_en_archivo = False

    temp = open("temp_"+arch, "w")
    arch_tomo = open(arch)
    for linea in arch_tomo:
        datos = linea.strip().split(";")
        nombre, feli, satis = datos
        feli = int(feli)
        satis = int(satis)

        if nombre == tomo:
            estaba_en_archivo = True
            if feli != 0 and satis != 0:
                estadisticas["feliz"] = feli
                estadisticas["satisfecho"] = satis
            else:
                esta_muerto = True
        else:
            temp.write(linea)
    arch_tomo.close()
    temp.close()

    if estaba_en_archivo and not esta_muerto:
        return estadisticas

    if not estaba_en_archivo:
        return None

    arch_tomo = open(arch, "w")
    temp = open("temp_"+arch)
    for linea in temp:
        arch_tomo.write(linea)
    temp.close()
    arch_tomo.close()
    return False

def alimentar(tomo, ali, arch1, arch2):
    estadisticas = dict()

    estadisticas = status(tomo, arch1)
    if estadisticas == False:
        return "X.X"
    if estadisticas == None:
        return "hizo la muricion"

    comida = alimento(ali, arch2)
    if comida == False:
        return "no existe alimento"

    estadisticas["feliz"] += comida["feliz"]
    estadisticas["satisfecho"] += comida["satisfecho"]

    arch_tomo = open(arch1, "a")
    arch_tomo.write(tomo+";")
    arch_tomo.write(str(estadisticas["feliz"])+";")
    arch_tomo.write(str(estadisticas["satisfecho"])+"\n")
    arch_tomo.close()

    return estadisticas
