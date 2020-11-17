def juicios_por_mes(abogados):
    juicios={}
    for diccionario in abogados.values():
        for mes,cantidad in diccionario['juicios']:
            if mes not in juicios:
                juicios[mes]=0
            juicios[mes]+=cantidad
    return juicios

def total_juicios(abogado):
    total=0
    for mes,cantidad in abogados[abogado]['juicios']:
        total+=cantidad
    return total

def quien_trabajo(empresa):
    lista=[]
    for abogado,diccionario in abogados.items():
        if empresa in diccionario['empresas']:
            lista.append(abogado)
    return lista
