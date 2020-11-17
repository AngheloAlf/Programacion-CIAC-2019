def contar_pasajes(asientos):
    adulto = 0
    estudiante = 0
    for tipo in asientos:
        if tipo == "a":
            adulto += 1
        elif tipo == "e":
            estudiante += 1
    return adulto, estudiante

def calcular_recaudado(asientos):
    total = 0
    for tipo in asientos:
        if tipo == "a":
            total += 4000
        elif tipo == "e":
            total += 2200
    return total

asientos = input("Ingrese los asientos actuales: ")

tipo_pasaje = input("Ingrese tipo de pasaje: ")
while tipo_pasaje != "0" and "v" in asientos:
    posicion = int(input("Ingrese el asiento que quiere comprar: "))
    while asientos[posicion] != "v":
        print("Ocupado!")
        posicion = int(input("Ingrese el asiento que quiere comprar: "))

    tipo = "a"
    if tipo_pasaje == "estudiante":
        tipo = "e"
    asientos = asientos[:posicion] + tipo + asientos[posicion+1:]
    print("Asignado!")

    if "v" in asientos:
        tipo_pasaje = input("Ingrese tipo de pasaje: ")

if "v" not in asientos:
    print("Bus lleno.")

adulto, estudiante = contar_pasajes(asientos)

print("Se vendieron", adulto, "pasajes de adulto.")
print("Se vendieron", estudiante, "pasajes de estudiante.")
print("Se recaudo", calcular_recaudado(asientos))
print("Los asientos finales son:", asientos)
