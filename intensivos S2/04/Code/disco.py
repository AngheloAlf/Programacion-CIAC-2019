def mensaje(edad):
    if edad<18:
        return 'Eres muy chico para entrar'
    elif edad <80:
        return 'Adelante y paselo bien'
    else:
        return 'Estos lugares le hacen mal a su salud, vaya al parque mejor'

flag=True
while flag:
    valor=int(input('Ingrese edad (0 para salir): '))
    if valor==0:
        flag=False
    else:
        print(mensaje(valor))
print('Adios')
