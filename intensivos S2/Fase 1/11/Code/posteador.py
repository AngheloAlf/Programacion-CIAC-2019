# Pregunta 2

from funciones_auxiliares import obtener_id_usuario, obtener_ultimo_id
from funciones_auxiliares import tupla_a_fecha, fecha_a_tupla
from funciones_auxiliares import obtener_posts_de_usuario


def postear(archPosts, archUsers, titulo, url, usuario, etiquetas, fecha):
    # Verificamos que el usuario existe.
    id_usuario = obtener_id_usuario(archUsers, usuario)
    if id_usuario == None:
        return False

    formato = "{},{},{},{},{},0,0,{}\n"

    # Reemplazamos las comas por puntos y comas en el titulo.
    titulo = titulo.replace(",", ";")

    # Generamos un id para el post y preparamos los otros datos.
    post_id = str(obtener_ultimo_id(archPosts) + 1)
    etiquetas_formateado = "-".join(etiquetas)
    fecha_formateada = tupla_a_fecha(fecha)

    arch = open(archPosts, "a")
    linea = formato.format(post_id, titulo, url, id_usuario, etiquetas_formateado, fecha_formateada)
    arch.write(linea)
    arch.close()

    return True


def upvotePost(archPost, archUsers, idPost, username):
    # Verificamos que el usuario existe.
    idUser = obtener_id_usuario(archUsers, username)
    if idUser is None:
        return False

    post_existe = False
    primera = True

    arch = open(archPost)
    temp = open("temp_"+archPost, "w")
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            datos = linea.strip().split(",")
            if datos[0] == idPost:
                post_existe = True

                # Actualizamos los upvotes del usuario.
                upvotes = int(datos[5])
                upvotes = upvotes + 1
                datos[5] = str(upvotes)

                resultado = ",".join(datos) + "\n"
                temp.write(resultado)
            else:
                temp.write(linea)
    arch.close()
    temp.close()

    arch = open(archPost, "w")
    temp = open("temp_"+archPost)
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()
    return post_existe

def downvotePost(archPost, archUsers, idPost, username):
    # Verificamos que el usuario existe.
    idUser = obtener_id_usuario(archUsers, username)
    if idUser is None:
        return False

    post_existe = False
    primera = True

    arch = open(archPost)
    temp = open("temp_"+archPost, "w")
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            datos = linea.strip().split(",")
            if datos[0] == idPost:
                post_existe = True

                # Actualizamos los downvotes del usuario.
                downvotes = int(datos[6])
                downvotes = downvotes + 1
                datos[6] = str(downvotes)

                resultado = ",".join(datos) + "\n"
                temp.write(resultado)
            else:
                temp.write(linea)
    arch.close()
    temp.close()

    arch = open(archPost, "w")
    temp = open("temp_"+archPost)
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()
    return post_existe


def actualizarCantidadPosts(archUsers, archPosts):
    cantidad_total_posts = 0
    primera = True

    temp = open("temp_"+archUsers, "w")
    arch = open(archUsers)
    for linea in arch:
        if primera:
            primera = False
            temp.write(linea)
        else:
            datos = linea.strip().split(",")
            user_id = datos[0]

            # Obtenemos la cantidad de posts del usuario.
            posts_user = obtener_posts_de_usuario(archPosts, user_id)
            cantidad_posts = len(posts_user)

            # Contamos el total de posts
            cantidad_total_posts += cantidad_posts

            # Actualizamos la cantidad de posts.
            datos[-1] = str(cantidad_posts)
            escribir = ",".join(datos)+"\n"
            temp.write(escribir)
    temp.close()
    arch.close()

    arch = open(archUsers, "w")
    temp = open("temp_"+archUsers)
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()
    return cantidad_total_posts


def mostrarPost(archPost, idPost):
    post = dict()
    primera = True

    arch = open(archPost)
    for linea in arch:
        if primera:
            primera = False
        else:
            datos = linea.strip().split(",")
            post_id, titulo, meme_url, usuario_id, etiquetas, upvotes, downvotes, fecha = datos
            if idPost == post_id:
                post["post_id"] = int(post_id)
                post["titulo"] = titulo
                post["meme_url"] = meme_url
                post["usuario_id"] = int(usuario_id)
                post["etiquetas"] = etiquetas.split("-")
                post["upvotes"] = int(upvotes)
                post["downvotes"] = int(downvotes)
                post["fecha"] = fecha_a_tupla(fecha)
    arch.close()
    return post
