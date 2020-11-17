def calcular_capacidad(consumo, base_tiempo, autonomia):
    return consumo * base_tiempo * (autonomia/base_tiempo)**(1/1.15)

h = float(input("Base del tiempo de la bateria: "))
autonomia = float(input("Autonomia de la bateria: "))
voltaje = float(input("Voltaje de la bateria: "))
sol = float(input("Potencia del sol: "))

potencia_ampolletas = 0
i = 1
potencia_por_precio = float("inf")
precio_mas_barato = float("inf")
pack_mas_barato = 0
total_dinero = 0
while potencia_ampolletas < sol:
    precio = float(input("Precio pack " + str(i) + ": "))
    cantidad = float(input("Cantidad pack " + str(i) + ": "))
    potencia = float(input("Potencia pack " + str(i) + ": "))
    total_dinero += precio
    potencia_ampolletas += cantidad * potencia
    if potencia * precio / cantidad < potencia_por_precio:
        potencia_por_precio = potencia * precio / cantidad
        precio_mas_barato = precio / cantidad
        pack_mas_barato = i
    i += 1

consumo = potencia_ampolletas / voltaje
capacidad = calcular_capacidad(consumo, h, autonomia)

print("La capacidad de la bateria a comprar es " + str(capacidad)+".")
print("Se gastaria " + str(total_dinero)+" en ampolletas.")
print("El pack mas barato es el " + str(pack_mas_barato)+" con precio unitario " + str(precio_mas_barato) + " por ampolleta.")
