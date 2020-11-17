def buscar_precio(producto,precios):
    arch=open(precios)
    for linea in arch:
        if producto in linea:
            nombre,precio=linea.strip().split(':$')
            arch.close()
            return int(precio)
    arch.close()
    return False

def diccionario_pedido(linea_pedido):
    #linea pedido es una linea en string separado por ; de la forma
    #producto1-cantidad1;producto2-cantidad2;...
    lista=linea_pedido.split(';')
    diccionario={}
    for elemento in lista:
        producto,cantidad=elemento.split('-')
        diccionario[producto]=int(cantidad)
    return diccionario

def crear_archivos(precios,pedidos):
    arch_pedidos=open(pedidos)
    for linea in arch_pedidos:
        nombre,linea_pedido=linea.strip().split(':')
        dicc_pedido=diccionario_pedido(linea_pedido)
        boleta=open('boleta_{}.txt'.format(nombre),'w')
        boleta.write('Boleta de {}:\n'.format(nombre))
        boleta.write('\tProducto\tCantidad\tP. unitario\tTotal\n')
        total=0
        for producto,cantidad in dicc_pedido.items():
            f='\t{0}\t\t{1}\t\t${2}\t\t${3}\n'
            p_unitario=buscar_precio(producto,precios)
            total_unitario=p_unitario*cantidad
            total+=total_unitario
            boleta.write(f.format(producto,cantidad,p_unitario,total_unitario))
        boleta.write('\nEl total de su compra es: ${}'.format(total))
        boleta.close()
    arch_pedidos.close()
    return None
    
