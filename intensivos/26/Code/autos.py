def precios(archivo):
    dic={}
    arch=open(archivo)
    for linea in arch:
        marca,modelo,precio=linea.strip().split(',')
        dic[modelo]=int(precio)
    arch.close()
    return dic

def total_ventas_mes(codigo,mes,archivo1,archivo2):
    ventas=open(archivo2)
    dic_precios=precios(archivo1)
    total=0
    for linea in ventas:
        datos=linea.strip().split(',')
        mes1=datos[0].split('/')[1]
        if codigo==int(datos[-1]) and int(mes1)==mes:
            total+=dic_precios[datos[3]]
    ventas.close()
    return total
            
def venta_diaria(archivo1,archivo2):
    nuevo=arch=open('venta_diaria.txt','w')
    ventas=open(archivo2)
    dic_precios=precios(archivo1)
    anterior=''
    for linea in ventas:
        dia,_,_,modelo,_=linea.strip().split(',')
        if anterior!=dia and anterior!='':
            nuevo.write('{0}:{1}\n'.format(anterior,total))
            anterior=dia
            total=0
        elif anterior=='':
            anterior=dia
            total=0
        total+=dic_precios[modelo]
    ventas.close()
    nuevo.write('{0}:{1}\n'.format(anterior,total))
    nuevo.close()
    return

def venta_por_marca(archivo1, archivo2):
    lista_marcas = []
    prods = open(archivo1)
    for linea in prods:
        marca, modelo, costo = linea.strip().split(",")
        lista_marcas.append(marca)
    prods.close()

    dic_precios=precios(archivo1)

    for marca in lista_marcas:
        archivo_marca = open(marca+".txt", "w")
        ventas = open(archivo2)
        anterior=''
        total = 0
        for linea2 in ventas:
            dia, _, marca2, modelo2, _ = linea2.strip().split(",")
            if marca == marca2:
                if anterior!=dia and anterior!='':
                    archivo_marca.write('{0}:{1}\n'.format(anterior,total))
                    anterior=dia
                    total=0
                elif anterior=='':
                    anterior=dia
                    total=0
                total+=dic_precios[modelo2]
        if anterior != "":
            archivo_marca.write('{0}:{1}\n'.format(anterior,total))

        archivo_marca.close()
        ventas.close()
    return
