disponibles=20
ganancia=0
ninios=0
adultos=0
while disponibles>0:
    entradas_ninio=int(input('Ingrese entradas ninio: '))
    entradas_adulto=int(input('Ingrese entradas adulto: '))
    total=entradas_ninio+entradas_adulto
    if total<=disponibles:
        ninios+=entradas_ninio
        adultos+=entradas_adulto
        disponibles-=total
        boleto=entradas_ninio*1000+entradas_adulto*3000
        print('Debe pagar $'+str(boleto))
        ganancia+=boleto
    else:
        print('No quedan tantos boletos')
print('')
print('Todas las entradas vendidas :D')
print('Hoy ganaste $',ganancia)
