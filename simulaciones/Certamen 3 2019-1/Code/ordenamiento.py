def esta_palabra(archivo,palabra):
    arch=open(archivo)
    for linea in arch:
        if palabra in linea:
            arch.close()
            return True
    arch.close()
    return False

def encontrar_virus(archivos,malignos):
    infectados=[]
    for palabra in malignos:
        for archivo in archivos:
            arch=open(archivo+'.txt')
            for linea in arch:
                if palabra in linea:
                    if archivo+'.txt' not in infectados:
                        infectados.append(archivo+'.txt')
            arch.close()
    return infectados
