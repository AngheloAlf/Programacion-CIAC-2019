# ejercicios = [(nombre1, horas, aporte), ...]
# Necesitamos que el sennor Estrella nos especifique sus ejericicios para
# poder llenar la lista.

def rutina(ejercicios, limite):
    ejer_por_aporte = []
    # Recorremos la lista de ejercicios.
    for nom, horas, apor in ejercicios:
        # Generamos una nueva tupla, agregando al inicio la division entre
        # el aporte y las horas, y lo agregamos a una lista nueva.
        tupla = (apor/horas, nom, horas, apor)
        ejer_por_aporte.append(tupla)

    # Ordenamos la lista de mayor a menor, segun la division en cuestion.
    ejer_por_aporte.sort()
    ejer_por_aporte.reverse()

    # Necesitaremos saber cuantas horas llevamos acumuladas.
    horas_acumuladas = 0
    resultado = []
    # Recorremos nuestros ejercicios, partiendo por los que tienen mayor 
    # impacto en nuestro heroe.
    for division, nom, horas, apor in ejer_por_aporte:
        # Nos aseguramos que lo que nos demora el ejercicio no supere la
        # cantidad de tiempo estipulado.
        # Si lo supera, lo ignoramos.
        if horas_acumuladas + horas <= limite:
            tupla = (nom, horas, apor)
            # Si no lo supera, agregamos el ejercicio a la lista.
            resultado.append(tupla)
            # No olvidar contabilizar las horas acumuladas.
            horas_acumuladas += horas
    # Entregar nuestra rutina de ejercicios para nuestro heroe.
    return resultado
