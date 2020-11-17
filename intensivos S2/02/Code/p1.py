actual=int(input('Ingrese la hora actual: '))
cantidad=int(input('Ingrese cantidad de horas: '))

# Sumamos las horas y calculamos el modulo para que no nos pasemos de la
# cantidad limite de horas que tiene un dia.
futura=(actual+cantidad)%24
# Para saber cuantos dias han pasado, sumamos las horas y las dividimos por 24. 
# Ojo con el // para el calculo de la division entera
dias=(actual+cantidad)//24
print('Son',dias,'dias, y seran las',futura)
