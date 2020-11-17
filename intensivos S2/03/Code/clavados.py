def feedback(promedio):
    if promedio>=8.0:
        f='Excelente!'
    elif promedio>=5.0:
        f='Muy bien!'
    elif promedio>=3.0:
        f='No esta mal'
    else:
        f='Esto no es un concurso de guatazos, sigue practicando!'
    return f

n=int(input('Ingrese numero de puntajes: '))
#Se usara el algoritmo de encontrar un maximo y minimo
maximo=-float('inf')
minimo=float('inf')
#Para contar los puntajes a ingresar y controlar el ciclo while
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
#Se descuentan los puntajes maximo y minimo
promedio=(suma-minimo-maximo)/(n-2)
#Se llama la funcion definida al principio para conocer el feedback del jurado
mensaje=feedback(promedio)
print('El puntaje minimo fue',minimo)
print('El puntaje maximo fue',maximo)
print('El puntaje final es '+str(round(promedio, 2)))
print(mensaje)
