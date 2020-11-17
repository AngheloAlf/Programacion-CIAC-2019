def impuestos_por_ley(utilidad):
    if utilidad < 50:
        return utilidad * 0.25
    elif utilidad < 80:
        return utilidad * 0.3
    return utilidad * 0.4

def empresa_grande(utilidad):
    impuesto = impuestos_por_ley(utilidad)
    if impuesto > 64:
        return 0 # Se fue al extranjero.
    elif impuesto > 36:
        # La empresa se divide en 2 y la utilidad se reparte por igual.
        impuesto = impuestos_por_ley(utilidad/2)
        # Como son 2 empresas, tenemos que pagar el impuesto de ambas.
        return 2*impuesto
    return impuesto

def empresa_mediana(utilidad):
    impuesto = impuestos_por_ley(utilidad)
    if utilidad > 70:
        return impuesto*(1-0.3) # Paga un 30% menos
    elif utilidad > 60:
        return impuesto*(1-0.1) # Paga un 10% menos
    return impuesto

def empresa_pequena(utilidad):
    impuesto = impuestos_por_ley(utilidad)
    if utilidad < 20:
        return impuesto*(1+0.2) # 20% extra por multa.
    return impuesto

# Programa
i = 1
platita = int(input("Ingrese utilidad empresa "+str(i)+": "))
impuestos_esperados = 0
impuestos_pagados = 0
impuesto = 0
menor = float("inf")
nombre_menor = 0
mayor = -float("inf")
nombre_mayor = 0
while platita != 0:
    impuestos_esperados += impuestos_por_ley(platita)

    if platita < 50:
        impuesto = empresa_pequena(platita)
    elif platita < 80:
        impuesto = empresa_mediana(platita)
    else:
        impuesto = empresa_grande(platita)
    impuestos_pagados += impuesto

    if impuesto < menor:
        menor = impuesto
        nombre_menor = i
    if impuesto > mayor:
        mayor = impuesto
        nombre_mayor = i
    i += 1
    platita = int(input("Ingrese utilidad empresa "+str(i)+": "))

print("El impuesto esperado es", impuestos_esperados)
print("pero lo pagado fue", impuestos_pagados)
print("La empresa que pago menos impuestos fue la empresa", nombre_menor)
print("la cual pago", menor)
print("La empresa que pago mas impuestos fue la empresa", nombre_mayor,)
print("la cual pago", mayor)
