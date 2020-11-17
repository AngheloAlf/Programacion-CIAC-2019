x = float(input('x: '))
print('Coeficientes:')

suma = 0.0
i = 0
switch = True
while switch:
    coeficiente = input()
    if coeficiente == 'FIN':
        switch = False
    else:
        suma += (x**i)*float(coeficiente)
        i += 1
print('p(x) =', suma)
