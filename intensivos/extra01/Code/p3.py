def eliminarEstudiante(estudiantes, nombre):
    # Recorremos la lista buscando al estudiante.
    for persona in estudiantes:
        nom, notas, asistencia = persona
        if nom == nombre:
            # Si lo encontramos lo removemos y retornamos True,
            # para indicar que lo encontramos
            estudiantes.remove(persona)
            return True
    # Si terminamos el ciclo for, significa que no encontramos a la 
    # persona en cuestion, por lo que retornamos False.
    return False

def promedioGeneral(estudiantes):
    suma = 0.0
    total = 0.0
    for nombre, notas, asistencia in estudiantes:
        # Recorremos la lista de estudiantes, calculamos los promedios
        # y lo vamos sumando para poder calcular el promedio.
        suma += calcularPromedioNotas(estudiantes, nombre)
        total += 1
    if total == 0.0:
        return 0
    return suma / total

def cambiarNota(estudiantes, nombre, evaluacion, notaNueva):
    # Primero revisamos que el numero de evaluacion sea mayor a cero.
    if evaluacion < 1:
        return False
    encontrado = False
    for nom, notas, asistencia in estudiantes:
        # Buscamos al estudiante en cuestion.
        if nom == nombre:
            # Revisamos que el numero de evaluacion no sobrepase a la cantidad
            # de evaluaciones que tiene el estudiante.
            if evaluacion > len(notas):
                return False
            # Reemplazamos la evaluacion en cuestion. Hay que recordar
            # que el numero de evaluacion empieza en 1 en vez de 0, por lo que
            # hay que restarle 1 al indice.
            notas[evaluacion - 1] = notaNueva
            # Indicamos que encontramos a la persona.
            encontrado = True
    # Si no encontramos a la persona, retornamos None
    if not encontrado:
        return None
    return True

def desvEstandarEstudiante(estudiantes, nombreEstudiante):
    suma = 0.0
    total = 0.0
    for nombre, notas, asistencia in estudiantes:
        if nombre == nombreEstudiante:
            promedio = calcularPromedioNotas(estudiantes, nombre)
            total = len(notas)
            if total == 0:
                return 0
            for nota in notas:
                suma += (nota - promedio)**2
            return (suma / total) ** 0.5
    return 0.0

def desvEstandarGeneral(estudiantes):
    suma = 0.0
    total = 0.0
    promedio = promedioGeneral(estudiantes)

    for nombre, notas, asistencia in estudiantes:
        total += len(notas)
        for nota in notas:
            suma += (nota - promedio)**2
    if total == 0:
        return 0
    return (suma / total) ** 0.5

def aprobadosDelCurso(estudiantes):
    aprobados = list()
    for nombre, notas, asistencia in estudiantes:
        prom_notas = calcularPromedioNotas(estudiantes, nombre)
        prom_asis = calcularPorcentajeAsistencia(estudiantes, nombre)
        if prom_notas >= 55 and prom_asis > 65:
            tupla = (nombre, prom_notas, prom_asis)
            aprobados.append(tupla)
    return aprobados


estudiantes = list()
print("Bienvenido al sistema de notas!")
print("Las opciones son las siguientes:")
print("1. Agregar nota de un alumno")
print("2. Indicar asistencia de un alumno")
print("3. Calcular promedio de notas y porcentaje de asistencia de un alumno")
print("4. Mostrar al mejor alumno")
print("5. Mostrar al peor alumno")
print("6. Eliminar alumno")
print("7. Calcular promedio general del curso")
print("8. Cambiar la nota de un alumno")
print("9. Calcular la desviacion estandar de las notas de un estudiante")
print("10. Calcular la desviacion estandar del curso completo")
print("11. Mostar lista de aprobados")
print("0. Salir")
print("")
programa = True
while programa:
    print("")
    seleccion = int(input("Ingrese el numero de su opcion: "))

    if seleccion == 0:
        programa = False
    elif seleccion == 1:
        nombre = input("Ingrese el nombre del alumno: ")
        nota = input("Ingrese la nota del alumno: ")
        agregarNota(estudiantes, nombre, nota)
    elif seleccion == 2:
        nombre = input("Ingrese el nombre del alumno: ")
        print("El alumno " + nombre + " asistio (1) o no asistio (0)?")
        asistio = input("Ingrese opcion: ")
        if asistio == "0":
            alumnoNoAsistio(estudiantes, nombre)
        else:
            alumnoAsistio(estudiantes, nombre)
    elif seleccion == 3:
        nombre = input("Ingrese el nombre del alumno: ")
        prom = str(calcularPromedioNotas(estudiantes, nombre))
        asistencia = str(calcularPorcentajeAsistencia(estudiantes, nombre))
        print("El promedio de notas de " + nombre + " es " + prom )
        print("Su promedio de asistencia es " + asistencia + "%")
    elif seleccion == 4:
        mejor = mejorEstudiante(estudiantes)
        print("El mejor estudiante es " + mejor[0])
    elif seleccion == 5:
        mejor = peorEstudiante(estudiantes)
        print("El peor estudiante es " + mejor[0])
    elif seleccion == 6:
        nombre = input("Ingrese el nombre del alumno a ser eliminado: ")
        if eliminarEstudiante(estudiantes, nombre):
            print("Alumno eliminado satisfactoriamente")
        else:
            print("El alumno ingresado no existe")
    elif seleccion == 7:
        prom = str(promedioGeneral(estudiantes))
        print("El promedio general es " + prom)
    elif seleccion == 8:
        nombre = input("Ingrese el nombre del alumno: ")
        evalua = input("Cual es la evaluacion que desea eliminar?: ")
        nota = input("Cual es la nota nueva?: ")
        resul = cambiarNota(estudiantes, nombre, evalua, nota)
        if resul is None:
            print("El alumno ingresado no existe")
        elif resul == False:
            print("Ingreso una evaluacion invalida")
        else:
            print("Nota cambiada satisfactoriamente")
    elif seleccion == 9:
        nombre = input("Ingrese el nombre del alumno del cual quiere conocer su desviacion estandar: ")
        prom = str(desvEstandarEstudiante(estudiantes, nombre))
        print("La desviacion estandar de las notas de " + nombre + " es " + prom)
    elif seleccion == 10:
        prom = str(desvEstandarGeneral(estudiantes))
        print("La desviacion estandar de las notas del curso es " + prom)
    elif seleccion == 11:
        prom = str(aprobadosDelCurso(estudiantes))
        print("Los aprobados son:")
        for nom, nota, asis in prom:
            print(nom, "con promedio", nota, " y porcentaje de asistencia de", asis)
print("Adios.")
