def eliminar_espias(arch_aeropuertos):
    aeropuertos = open(arch_aeropuertos)
    temporal = open("temp.txt","w")
    encontrados = {}
    for linea in aeropuertos:
        rut = linea.strip().split(',')[4]
        par1, par2 = rut.split('_')
        if par1[0] != par1[1] or par2[0] != par2[1]:
            id_a,nom,pist,tam = linea.strip().split(',')[:4]
            nueva_linea = ",".join([id_a,nom,pist,tam,"XX_XX"])
            temporal.write(nueva_linea+"\n")
            encontrados[nom] = rut
        else:
            temporal.write(linea)
    aeropuertos.close()
    temporal.close()
    if not(encontrados):
        return False
    aeropuertos = open(arch_aeropuertos,"w")
    temporal = open("temp.txt")
    for linea in temporal:
        aeropuertos.write(linea)
    aeropuertos.close()
    temporal.close()
    return encontrados
