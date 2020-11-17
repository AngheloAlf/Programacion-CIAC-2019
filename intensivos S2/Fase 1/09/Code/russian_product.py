def gen_tabla(producto):
    tabla = [producto]
    n1, n2 = producto
    while n1 > 1:
        n1 = n1//2
        n2 = 2*n2
        tupla = (n1, n2)
        tabla.append(tupla)
    return tabla

def sumar_impares(tabla):
    suma = 0
    for n1, n2 in tabla:
        if n1%2 == 1:
            suma += n2
    return suma

# Funcion auxiliar
def russian_product(n1,n2):
    tabla = gen_tabla((n1, n2))
    resultado = sumar_impares(tabla)
    return (tabla, resultado)

def resolver(nombre_arch):
    arch = open(nombre_arch)

    nombre_sin_txt = nombre_arch.split(".txt")[0]
    nombre_solucion = nombre_sin_txt + "_sol.txt"
    arch_sol = open(nombre_solucion, "w")

    for linea in arch:
        datos = linea.strip().split("x")
        n1, n2 = map(int, datos)

        tabla, res = russian_product(n1,n2)

        arch_sol.write("TABLA de ")
        arch_sol.write(str(tabla[0][0]))
        arch_sol.write("x")
        arch_sol.write(str(tabla[0][1]))
        arch_sol.write("=" + str(res) + "\n")

        for n1, n2 in tabla:
            if n1%2 == 0:
                fila = "0\t"+str(n1)+"\t\t"+str(n2)+"\n"
            else:
                fila = "1\t"+str(n1)+"\t\t"+str(n2)+"\n"
            arch_sol.write(fila)

    arch.close()
    arch_sol.close()
