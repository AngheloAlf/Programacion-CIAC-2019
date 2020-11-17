# Suma y Producto
A=int(input('Ingrese el primer numero: '))
B=int(input('Ingrese el segundo numero: '))
A += 1 # Se excluyen los numeros ingresados
suma = 0
mult = 1
while A < B:
    suma += A
    mult *= A
    A += 1
print('La suma es',suma)
print('La multiplicacion es',mult)

#Cachipun
J1=input('J1 ingrese seleccion: ')
J2=input('J2 ingrese seleccion: ')
if J1==J2:
    print('Empate')
else:
    if J1=='piedra':
        if J2=='papel':
            print('Gana el jugador 2')
        else:
            print('Gana el jugador 1')
    elif J1=='papel':
        if J2=='piedra':
            print('Gana el jugador 1')
        else:
            print('Gana el jugador 2')
    else: #J1 es tijera
        if J2=='piedra':
            print('Gana el jugador 2')
        else:
            print('Gana el jugador 1')

#Sumatoria
x_i = 1.0
x_i_1 = 1.0
suma = 0.0
numero = float(input("Ingrese numero: "))
while numero != 0.0:
    x_i_1 = x_i
    x_i = numero
    suma += x_i/x_i_1
    numero = float(input("Ingrese numero: "))

print("El resultado de la sumatoria es:", suma)
