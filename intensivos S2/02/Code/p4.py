n=int(input('Ingrese numero de puntajes: '))

# En este ejercicio aplicaremos el algoritmo del mayor y el algoritmo del menor.
# El algoritmo del mayor consiste en la busqueda del numero mas grande,
# para esto empezamos con el menor numero posible (en este caso el
# infinito negativo) y cada vez que encontremos un numero mayor, lo guardamos
# en esta variable.
# Para el algoritmo del minimo es lo mismo, pero con el numero mas grande 
# posible.
maximo=-float('inf')
minimo=float('inf')
i=1
suma=0
while i<=n:
    puntaje=float(input('Puntaje '+str(i)+': '))
    i+=1
    # Sumamos todos los puntaes que nos entregan
    suma+=puntaje
    # Buscamos el mayor y menor puntaje entregado.
    if puntaje>maximo:
        maximo=puntaje
    if puntaje<minimo:
        minimo=puntaje
# Descontamos los puntajes minimos y maximos, y calculamos el promedio.
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