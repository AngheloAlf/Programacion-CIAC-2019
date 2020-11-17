A=int(input('Ingrese el primer numero: '))
B=int(input('Ingrese el segundo numero: '))

suma = 0
mult = 1
C = A + 1
while C < B:
    suma += C
    mult *= C
    C += 1

print('La suma es',suma)
print('La multiplicacion es',mult)
