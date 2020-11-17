def costo_total(arch):
    total = 0
    archivo = open(arch)
    for linea in archivo:
        datos = linea.strip()
        costo = int(datos)
        total += costo
    archivo.close()
    return total

# Funcion auxiliar
# Recibe el nombre de un mes.
# Retorna su numero correspondiente.
def mes_a_numero(mes):
    meses = {"enero": 1, "febrero": 2, "marzo": 3,
             "abril": 4, "mayo": 5, "junio": 6, 
             "julio": 7, "agosto": 8, "septiembre": 9,
             "octubre": 10, "noviembre": 11, "diciembre": 12}
    return meses[mes]

def busqueda_por_mes(arch, mes):
    busqueda = dict()
    mes_num = mes_a_numero(mes)

    arch_viajes = open(arch)
    for linea in arch_viajes:
        rut, datos = linea.strip().split("#")

        datos_viajes = datos.split(";")
        for viaje in datos_viajes:
            mes, pais, indice = viaje.strip().split(",")

            if int(mes) == mes_num:
                if rut not in busqueda:
                    busqueda[rut] = []
                busqueda[rut].append(pais)
    arch_viajes.close()

    return busqueda


def realizar_sumario(arch1, arch2):
    lista = []
    arch_viajes = open(arch1)
    for linea in arch_viajes:
        rut, datos = linea.strip().split("#")

        lista_paises = []
        acumulado = 0

        datos_viajes = datos.split(";")
        for viaje in datos_viajes:
            mes, pais, indice = viaje.strip().split(",")
            lista_paises.append(pais)

            i = 1
            arch_costos = open(arch2)
            for linea_costos in arch_costos:
                costo = int(linea_costos.strip())

                if i == int(indice):
                    acumulado += costo

                i += 1
            arch_costos.close()

        if acumulado >= 10000000:
            paises = ";".join(lista_paises)
            tupla = (acumulado, rut, paises)
            lista.append(tupla)
    arch_viajes.close()

    lista.sort()

    sumario = open("sumario.txt", "w")
    for acumulado, rut, paises in lista:
        sumario.write(rut+","+str(acumulado)+","+paises+"\n")
    sumario.close()
    return
