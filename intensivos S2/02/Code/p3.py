x = float(input('x: '))
print('Coeficientes:')

# La variable donde almacenaremos la suma total.
suma = 0.0
# Nuestra variable contador para el while.
i = 0
# Esta variable indicara que debemos seguir pidiendo coeficientes.
# Cuando sea False el usuario habria ingresado FIN.
flag = True
while flag:
    coeficiente = input("a"+str(i)+": ")
    if coeficiente == "FIN":
        flag = False
    else:
        # Calculamos el coeficiente por el x.
        suma += (x**i)*float(coeficiente)
        i += 1
print("p("+str(x)+") =", suma)
