# Pregunta 3

from funciones_auxiliares import obtener_id_usuario, obtener_ultimo_id
from funciones_auxiliares import tupla_a_fecha, fecha_a_tupla
from funciones_auxiliares import obtener_datos_por_id
from funciones_auxiliares import obtener_posts_de_usuario, obtener_comentarios_de_usuario


def comentar(archComs, archPosts, archUsers, idPost, username, com, fecha):
    user_id = obtener_id_usuario(archUsers, username)
    # Verificar que el usuario existe.
    if user_id == None:
        return False
    # Verificar que el post existe.
    if obtener_datos_por_id(archPosts, idPost) == None:
        return False

    formato = "{},{},{},{},0,0,{}\n"

    # Reemplazamos las comas por puntos y comas.
    com = com.replace(",", ";")
    # Generamos un id para el comentario.
    comm_id = str(obtener_ultimo_id(archComs) + 1)
    fecha_formateada = tupla_a_fecha(fecha)

    linea = formato.format(comm_id, idPost, user_id, com, fecha_formateada)

    arch = open(archComs, "a")
    arch.write(linea)
    arch.close()

    return True


def comentariosDePost(archComs, archPosts, idPost):
    # Verificar que el post existe.
    if obtener_datos_por_id(archPosts, idPost) == None:
        return False

    comentarios = dict()
    primera = True

    arch = open(archComs)
    for linea in arch:
        if primera:
            primera = False
        else:
            comentario_id, post_id, usuario_id, contenido, upvotes, downvotes, fecha = linea.strip().split(",")
            if post_id == idPost:
                comment = dict()

                # Generamos un diccionario con los datos del comentario.
                comment["comentario_id"] = int(comentario_id)
                comment["post_id"] = int(post_id)
                comment["usuario_id"] = int(usuario_id)
                comment["contenido"] = contenido
                comment["upvotes"] = int(upvotes)
                comment["downvotes"] = int(downvotes)
                comment["fecha"] = fecha_a_tupla(fecha)

                # Agregamos el comentario al diccionario general.
                comentarios[int(comentario_id)] = comment
    arch.close()

    return comentarios


def borrarComentariosFechaErronea(archComs, archPosts, archUsers):
    comentarios_borrados = []
    primera = True

    temp = open("temp_"+archComs, "w")
    arch = open(archComs)
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            datos = linea.strip().split(",")
            comentario_id, post_id, usuario_id, _, _, _, fecha = datos
            fecha_comentario = fecha_a_tupla(fecha)

            # Obtenemos la fecha de creacion del usuario
            datos_usuario = obtener_datos_por_id(archUsers, usuario_id)
            fecha_usuario = fecha_a_tupla(datos_usuario[2])

            # Obtenemos la fecha en que se hizo el post.
            datos_post = obtener_datos_por_id(archPosts, post_id)
            fecha_post = fecha_a_tupla(datos_post[7])

            # Si alguno de ambas fechas es erronea, el post se elimina.
            if fecha_comentario < fecha_usuario or fecha_comentario < fecha_post:
                comentarios_borrados.append(comentario_id)
            else:
                temp.write(linea)
    arch.close()
    temp.close()

    temp = open("temp_"+archComs)
    arch = open(archComs, "w")
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()

    return comentarios_borrados


def eliminarPost(archPosts, archComs, idPost):
    comentarios_borrados = 0
    idPost = int(idPost)

    # Eliminamos el post.
    primera = True
    temp = open("temp_"+archPosts, "w")
    arch = open(archPosts)
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            datos = linea.strip().split(",")
            post_id = int(datos[0])

            # Si el id no corresponde con el buscado,
            # se escribe en el archivo temporal.
            # Si el id es del post buscado, se ignora
            # (no se escribe y se pierde, eliminandose).
            if post_id != idPost:
                temp.write(linea)
    arch.close()
    temp.close()

    temp = open("temp_"+archPosts)
    arch = open(archPosts, "w")
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()

    # Eliminamos los comentarios del post.
    primera = True
    temp = open("temp_"+archComs, "w")
    arch = open(archComs)
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            comentario_id,post_id,usuario_id,contenido,upvotes,downvotes,fecha = linea.strip().split(",")
            post_id = int(post_id)

            # Si el id no corresponde con el buscado,
            # se escribe en el archivo temporal.
            if post_id != idPost:
                temp.write(linea)
            else:
                # Si es el id que buscamos, lo contabilizamos.
                comentarios_borrados += 1
    arch.close()
    temp.close()

    temp = open("temp_"+archComs)
    arch = open(archComs, "w")
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()
    return comentarios_borrados


def actualizarPuntajeUsers(archUsers, archPosts, archComs):
    upvotes_totales = 0
    downvotes_totales = 0
    formato = "{},{},{},{},{}\n"
    primera = True

    temp = open("temp_"+archUsers, "w")
    arch = open(archUsers)
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            user_id,nombre,fecha_creacion,_,cantidad_posts = linea.strip().split(",")

            upvotes_user = 0
            downvotes_user = 0

            # Obtenemos los posts del usuario y sumamos los votos que ha recibido
            posts_usuario = obtener_posts_de_usuario(archPosts, user_id)
            for post in posts_usuario:
                _, _ ,_, _, _, upvotes, downvotes, _ = post
                upvotes_user += int(upvotes)
                downvotes_user += int(downvotes)

            # Obtenemos los comentarios del usuario y sumamos los votos que ha recibido
            comentarios_usuario = obtener_comentarios_de_usuario(archComs, user_id)
            for post in comentarios_usuario:
                _, _, _, _, upvotes, downvotes, fecha = post
                upvotes_user += int(upvotes)
                downvotes_user += int(downvotes)

            upvotes_totales += int(upvotes_user)
            downvotes_totales += int(downvotes_user)

            # Calculamos el puntaje y lo actualizamos en el usuario.
            puntaje = upvotes_user - downvotes_user
            para_escribir = formato.format(user_id, nombre, fecha_creacion, puntaje, cantidad_posts)
            temp.write(para_escribir)
    arch.close()
    temp.close()

    temp = open("temp_"+archUsers)
    arch = open(archUsers, "w")
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()

    return (upvotes_totales, downvotes_totales)
