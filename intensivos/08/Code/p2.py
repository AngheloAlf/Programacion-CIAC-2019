n = int(input("Ingrese la cantidad: "))

contador = 1
largo_larga = -float("inf")
mas_larga = ""
largo_corta = float("inf")
mas_corta = ""
while contador <= n:
    palabra = input("Ingrese la palabra " + str(contador) + ": ")

    if len(palabra) > largo_larga:
        largo_larga = len(palabra)
        mas_larga = palabra

    if len(palabra) < largo_corta:
        largo_corta = len(palabra)
        mas_corta = palabra

print("La palabra mas corta es: ", mas_corta)
print("La palabra mas larga es: ", mas_larga)
