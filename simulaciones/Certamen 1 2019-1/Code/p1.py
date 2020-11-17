rut = 60419
cont = 0
suma = 0
while rut > 0:
    unidad = rut % 10
    suma += unidad*(2+(cont % 6))
    rut = rut//10
    cont = cont + 1
d =  (suma %11)
d =  11 - d
if d == 10:
    digitov = "k"
elif d == 11:
    digitov = "0"
else:
    digitov = str(d)
print(digitov)
