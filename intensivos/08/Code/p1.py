def puntoEnRecta(punto, recta):
    x, y = punto
    m, n = recta
    resultado = m * x + n
    return resultado == y

def sonParalelas(recta1, recta2):
    m1, _ = recta1
    m2, _ = recta2
    return m1 == m2

def sonPerpendiculares(recta1, recta2):
    m1, _ = recta1
    m2, _ = recta2
    return m1 * m2 == -1

def rectaQuePasaPor(punto1, punto2):
    x0, y0 = punto1
    x1, y1 = punto2
    m = (y1 - y0)/float(x1 - x0)
    n = m*(-x0) + y0
    return [m, n]

def puntoInterseccion(recta1, recta2):
    if sonParalelas(recta1, recta2):
        return None
    m_0, n_0 = recta1
    m_1, n_1 = recta2
    x = (n_1 - n_0)/float(m_0 - m_1)
    y = m_0*x + n_0
    return [x, y]
