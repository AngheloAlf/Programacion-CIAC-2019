abogados={
    'mike':{'juicios':[('julio',3),('agosto',1),('octubre',4)],
            'sueldo':100,
            'empresas':['google','samsung','ciac'] },
    'rachel':{'juicios':[('enero',3),('marzo',4),('julio',8)],
              'sueldo':70,
              'empresas':['google','codelco']},
    'harvey':{'juicios':[('enero',5),('febrero',12),('julio',24)],
              'sueldo':1000,
              'empresas':['mesa verde','samsung']}
    }


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

def se_conocen(abogado_1,abogado_2):
    empresas_1=abogados[abogado_1]['empresas']
    empresas_2=abogados[abogado_2]['empresas']
    for empresa in empresas_1:
        if empresa in empresas_2:
            return True
    return False
