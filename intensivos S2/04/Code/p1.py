def f(x):
    return -x**2 - 3*x + 12

def f_gen(x, a, b, c):
    return a*x**2 + b*x + c

def sumator(n, a, b, c):
    i = 0
    suma = 0
    while i < n:
        suma += f_gen(i, a, b, c)
    return suma/n

def H(x, n):
    if x >= n:
        return 1
    else:
        return 0

def heav(n):
    i = 0
    suma = 0
    while i < n:
        numero = (f(i)*i**2)/n
        suma += numero * H(((-1)**i)*numero, i)
        i += 1
    return suma/n
