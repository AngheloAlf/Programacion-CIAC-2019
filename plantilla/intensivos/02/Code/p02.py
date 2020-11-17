n=int(input('Ingrese numero de puntajes: '))
maximo=-float('inf')
minimo=float('inf')
i=1
suma=0
while i<=n:
    puntaje=float(input('Puntaje '+str(i)+': '))
    i+=1
    suma+=puntaje
    if puntaje>maximo:
        maximo=puntaje
    if puntaje<minimo:
        minimo=puntaje
promedio=(suma-minimo-maximo)/(n-2)
if promedio>=8.0:
    feedback='Excelente!'
elif promedio>=5.0:
    feedback='Muy bien!'
elif promedio>=3.0:
    feedback='No esta mal'
else:
    feedback='Esto no es un concurso de guatazos, sigue practicando!'
print('El puntaje minimo fue',minimo)
print('El puntaje maximo fue',maximo)
print('El puntaje final es '+str(round(promedio, 2)))
print(feedback)