def agregarNota(estudiantes, nombre, nota):
    # Definimos una variable (flag) en la cual indicaremos si existe el estudiante
    # en la lista de estudiantes.
    existeEstudiante = False
    for estudi in estudiantes:
        # Desempaquetamos la tupla
        nom, notas, asistencia = estudi
        if nom == nombre:
            # Si la persona es la que estamos buscando, agregamos su nota,
            # y ademas indicamos que si existe la persona en la lista.
            notas.append(nota)
            existeEstudiante = True
    # Si no encontramos a la persona en la lista, la agregamos a la lista,
    # respetando la estructura.
    if not existeEstudiante:
        tupla = (nombre, [nota], [])
        estudiantes.append(tupla)

def alumnoAsistio(estudiantes, nombre):
    existeEstudiante = False
    # Desempaquetamos inmediatamente en el for.
    for nom, notas, asistencia in estudiantes:
        if nom == nombre:
            asistencia.append(True)
            existeEstudiante = True
    if not existeEstudiante:
        tupla = (nombre, [], [True])
        estudiantes.append(tupla)

def alumnoNoAsistio(estudiantes, nombre):
    existeEstudiante = False
    # Desempaquetamos inmediatamente en el for.
    for nom, notas, asistencia in estudiantes:
        if nom == nombre:
            asistencia.append(False)
            existeEstudiante = True
    if not existeEstudiante:
        tupla = (nombre, [], [False])
        estudiantes.append(tupla)

def calcularPromedioNotas(estudiantes, nombre):
    suma = 0.0
    total = 0.0
    # Desempaquetamos la tupla al iterar la lista de estudiantes.
    for nom, notas, asistencia in estudiantes:
        if nom == nombre:
            # Si llegamos a encontrar la persona, sumamos todas sus
            # notas y la cantidad de notas.
            for i in notas:
                suma += i
                total += 1
    # Si el estudiante no existia o tenia ninguna nota, retornaremos 0.
    if total == 0.0:
        return 0
    return suma/total

def calcularPorcentajeAsistencia(estudiantes, nombre):
    suma = 0.0
    total = 0.0
    # Desempaquetamos la tupla al iterar la lista de estudiantes.
    for nom, notas, asistencia in estudiantes:
        if nom == nombre:
            # Si llegamos a encontrar la persona, contamos todas sus
            # asistencias y la asistencia/inasistencia.
            for i in asistencia:
                if i:
                    suma += 1
                total += 1
    # Si el estudiante no existia o tenia ninguna nota, retornaremos 0.
    if total == 0.0:
        return 0
    return suma/total*100

def mejorEstudiante(estudiantes):
    # Para encontrar al mejor estudiante, usaremos el algoritmo del mayor.
    # Definimos el promedio que vamos a maximizar y la variable donde
    # almacenaremos el nombre de dicho mejor estudiante.
    el_mejor = ""
    mejor_promedio = -float("inf")
    for nombre, notas, asistencia in estudiantes:
        # Usamos las funciones anteriores para calcular los promedios
        # requeridos para saber que tan buen estudiante es.
        notas = calcularPromedioNotas(estudiantes, nombre)
        asis = calcularPorcentajeAsistencia(estudiantes, nombre)
        # Calculamos el promedio de estos 2 datos.
        prom = (notas + asis)/2.0
        # Y si este promedio es mejor que el que habiamos encontrado
        # anteriormente, lo reemplazamos con el nuevo valor mejor.
        if prom > mejor_promedio:
            el_mejor = nombre
            mejor_promedio = prom
    return el_mejor, mejor_promedio

def peorEstudiante(estudiantes):
    # Esta funcion pide lo mismo que la anterior, pero ahora debe
    # ser el peor estudiante.
    # Haremos lo mismo, pero aplicaremos el algoritmo del menor en vez
    # del algoritmo del mayor.
    peor = ""
    peor_promedio = float("inf")
    for nombre, notas, asistencia in estudiantes:
        notas = calcularPromedioNotas(estudiantes, nombre)
        asis = calcularPorcentajeAsistencia(estudiantes, nombre)
        prom = (notas + asis)/2.0
        if prom < peor_promedio:
            peor = nombre
            peor_promedio = prom
    return peor, peor_promedio
