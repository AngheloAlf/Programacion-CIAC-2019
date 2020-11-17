def alumnos_ramo(archivo,ramo):
    arch=open(archivo)
    cont=0
    for linea in arch:
        if ramo in linea:
            cont+=1
    arch.close()
    return cont

def promedio_ramo(archivo,ramo):
    arch=open(archivo)
    parcial=0
    for linea in arch:
        cortadito = linea.strip().split('#')
        if ramo == cortadito[1]:
            notas = cortadito[2].split(';')
            promedio = 0
            total = 0
            for i in notas:
                promedio += int(i)
                total += 1
            parcial += promedio//total
    arch.close()
    total=alumnos_ramo(archivo,ramo)
    return parcial//total

def agregar_promedio(archivo):
    temp=open('temp.txt','w')
    original=open(archivo)
    for linea in original:
        datos = linea.strip().split('#')
        notas = datos[2].split(';')

        promedio = 0
        total = 0
        for i in notas:
            promedio += int(i)
            total += 1

        promedio = promedio//total
        f='{0}#{1}\n'
        temp.write(f.format(linea.strip(),promedio))
    temp.close()
    original.close()

    temp=open('temp.txt')
    original=open(archivo,'w')
    for linea in temp:
        original.write(linea)
    temp.close()
    original.close()
    return None
