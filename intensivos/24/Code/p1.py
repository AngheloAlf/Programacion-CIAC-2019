def contar_letras(palabra):
    dicc = dict()
    for letra in palabra:
        letra = letra.lower()
        if letra not in dicc:
            dicc[letra] = 0
        dicc[letra] += 1
    return dicc

def son_anagramas(p1, p2):
    cant1 = contar_letras(p1)
    cant2 = contar_letras(p2)
    return cant1 == cant2

def es_panvocalica(palabra):
    vocales = ["a", "e", "i", "o", "u"]
    vocalesEnPalabras = list()
    for letra in palabra.lower():
        if letra in vocales:
            if letra not in vocalesEnPalabras:
                vocalesEnPalabras.append(letra)
    vocalesEnPalabras.sort()
    return vocalesEnPalabras == vocales

def en_orden(palabra):
    palabra = palabra.lower()
    for i in range(len(palabra) - 1):
        if palabra[i] > palabra[i+1]:
            return False
    return True

def en_orden_segun(palabra, guia):
    i = 0
    for letra in palabra:
        if letra == guia[i]:
            i += 1
            if i >= len(guia):
                return True
    return False

def palabras_repetidas(oracion):
    contador = dict()
    repetidas = list()
    for palabra in oracion.lower().split(" "):
        if palabra not in contador:
            contador[palabra] = 0
        contador[palabra] += 1
    for palabra, cantidad in contador.items():
        if cantidad > 1:
            repetidas.append(palabra)
    return repetidas
