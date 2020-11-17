# Recibe una tupla de 3 enteros (ANNO, MES, DIA)
# Retorna un string con formato de fecha "ANNO-MES-DIA"
def tupla_a_fecha(tupla):
    lista = map(str, tupla)
    return "-".join(lista)

# Recibe un string con formato de fecha "ANNO-MES-DIA"
# Retorna una tupla de 3 enteros (ANNO, MES, DIA)
def fecha_a_tupla(fecha):
    fecha = fecha.split("-")
    return (int(fecha[0]), int(fecha[1]), int(fecha[2]))


# Recibe arch usuarios y nombre de un usuario.
# Si el usuario existe, retorna el id asociado como string.
# Si no existe, retorna None.
def obtener_id_usuario(archUsers, username):
    ide = None
    primera = True

    arch = open(archUsers)
    for linea in arch:
        if primera:
            primera = False
        else:
            user_id, nombre, _, _, _ = linea.strip().split(",")
            if nombre == username:
                ide = user_id
    arch.close()
    return ide 


# Recibe el nombre de un archivo csv.
# Retorna el id mas grande que contiene el archivo.
def obtener_ultimo_id(archivo):
    ultimo = 0
    primera = True

    arch = open(archivo)
    for linea in arch:
        if primera:
            primera = False
        else:
            datos = linea.strip().split(",")
            # El id siempre es el primer elemento de cada fila.
            ide = int(datos[0])
            if ide > ultimo:
                ultimo = ide
    arch.close()
    return ultimo


# Recibe el nombre de un csv y un id.
# Retorna una lista de strings, la cual corresponde al id entregado.
# Si no se encuentra el id en el archivo, retorna None.
def obtener_datos_por_id(archivo, ide):
    datos_buscados = None
    primera = True

    arch = open(archivo)
    for linea in arch:
        if primera:
            primera = False
        else:
            datos = linea.strip().split(",")
            if datos[0] == ide:
                datos_buscados = datos
    arch.close()
    return datos_buscados


# Recibe el archivo de posts y el id de un usuario.
# Retorna una lista que contiene los posts realizados por dicho usuario.
# Cada uno de los posts son listas de strings.
def obtener_posts_de_usuario(archPosts, user_id):
    lista = list()
    primera = True

    arch = open(archPosts)
    for linea in arch:
        if primera:
            primera = False
        else:
            datos = linea.strip().split(",")
            if user_id == datos[3]:
                lista.append(datos)
    arch.close()
    return lista


# Recibe el archivo de comentarios y el id de un usuario.
# Retorna una lista que contiene los comentarios realizados por dicho usuario.
# Cada uno de los comentarios son listas de strings.
def obtener_comentarios_de_usuario(archComs, user_id):
    lista = list()
    primera = True

    arch = open(archComs)
    for linea in arch:
        if primera:
            primera = False
        else:
            datos = linea.strip().split(",")
            if user_id == datos[2]:
                lista.append(datos)
    arch.close()

    return lista
