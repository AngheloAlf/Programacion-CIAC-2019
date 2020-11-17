def calcular_cuota(cap_inicial, tasa_interes, cantidad_periodos):
    aux = (1+tasa_interes)**cantidad_periodos
    cuota = cap_inicial * (aux * tasa_interes)/(aux - 1)
    return cuota

def calcular_interes(capital_anterior, tasa_interes):
    return capital_anterior*tasa_interes

def calcular_amortizacion(cuota, interes):
    return cuota - interes

def calcular_capital(capital_anterior, amortizacion):
    return capital_anterior - amortizacion

capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interes: "))
periodos = int(input("Ingrese la cantidad de periodos del credito: "))

print(0, capital)

cont = 1
cuota = calcular_cuota(capital, tasa, periodos)
total = cuota * periodos
total_interes = 0
while cont <= periodos:
    interes = calcular_interes(capital, tasa)
    total_interes += interes
    am = calcular_amortizacion(cuota, interes)
    capital = calcular_capital(capital, am)
    print(cont, round(capital, 2), round(am, 2), round(interes, 2), round(cuota, 2))
    cont += 1

total = round(total, 2)
total_interes = round(total_interes, 2)
print("El monto total a pagar es", total, " y de eso,", total_interes, "son solo intereses.")
