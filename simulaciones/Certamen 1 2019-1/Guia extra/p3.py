def binario_a_numero(binario):
    indice = 0
    suma = 0
    while binario > 0:
        bit = binario % 10
        if bit != 0:
            suma += 2**indice
        indice += 1
        binario //= 10
    return suma

def numero_a_letra(numero):
    if numero == 1:
        return "a"
    elif numero == 2:
        return "b"
    elif numero == 3:
        return "c"
    elif numero == 4:
        return "d"
    elif numero == 5:
        return "e"
    elif numero == 6:
        return "f"
    elif numero == 7:
        return "g"
    elif numero == 8:
        return "h"
    elif numero == 9:
        return "i"
    elif numero == 10:
        return "j"
    elif numero == 11:
        return "k"
    elif numero == 12:
        return "l"
    elif numero == 13:
        return "m"
    elif numero == 14:
        return "n"
    elif numero == 15:
        return "o"
    elif numero == 16:
        return "p"
    elif numero == 17:
        return "q"
    elif numero == 18:
        return "r"
    elif numero == 19:
        return "s"
    elif numero == 20:
        return "t"
    elif numero == 21:
        return "u"
    elif numero == 22:
        return "v"
    elif numero == 23:
        return "w"
    elif numero == 24:
        return "x"
    elif numero == 25:
        return "y"
    elif numero == 26:
        return "z"
    else:
        return " "

bina = int(input("Ingrese binario: "))
mensaje = ""
while bina != 0:
    numero = binario_a_numero(bina)
    letra = numero_a_letra(numero)
    mensaje += letra
    bina = int(input("Ingrese binario: "))

print(mensaje)
