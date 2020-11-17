# Pregunta 1

from funciones_auxiliares import obtener_id_usuario, obtener_ultimo_id
from funciones_auxiliares import tupla_a_fecha, fecha_a_tupla
from funciones_auxiliares import obtener_datos_por_id


def crearUsuario(archUsuarios, nombre, fecha):
    # Verificamos que el nombre no este ocupado.
    id_existente = obtener_id_usuario(archUsuarios, nombre)
    if id_existente != None:
        return False

    formato = "{},{},{},0,0\n"
    # Generamos un id para el usuario
    user_id = str(obtener_ultimo_id(archUsuarios) + 1)
    
    arch = open(archUsuarios, "a")
    linea = formato.format(user_id, nombre, tupla_a_fecha(fecha))
    arch.write(linea)
    arch.close()

    return True


def cambiarNombreUsuario(archUsuarios, idUser, nombreNuevo):
    # Verificamos que el nombre no este ocupado.
    id_existente = obtener_id_usuario(archUsuarios, nombreNuevo)
    if id_existente != None:
        return False

    nombre_cambiado = False

    temp = open("temp_"+archUsuarios, "w")
    arch = open(archUsuarios)
    primera = True
    for linea in arch:
        # Verificamos si esta linea es la primera 
        # (la que tiene los nombres de los datos).
        if primera:
            primera = False
            # Tenemos que mantener los datos de la primera linea, 
            # por lo que la escribimos sin modificarla.
            temp.write(linea)
        else:
            datos = linea.strip().split(",")
            # Si es la linea que contiene el usuario a modificar.
            if idUser == datos[0]:
                nombre_cambiado = True

                # Reemplazamos el nombre.
                datos[1] = nombreNuevo
                para_escribir = ",".join(datos) + "\n"
                temp.write(para_escribir)
            else:
                # Si no es el usuario, escribimos la linea tal cual.
                temp.write(linea)
    arch.close()
    temp.close()

    # Transcribimos los datos de nuestro archivo temporal al
    # archivo original.
    arch = open(archUsuarios, "w")
    temp = open("temp_"+archUsuarios)
    for linea in temp:
        arch.write(linea)
    arch.close()
    temp.close()

    return nombre_cambiado


def buscarPostsFechaIncorrecta(archPosts, archUsuarios):
    posts_erroneos = list()

    primera = True
    posts = open(archPosts)
    for linea in posts:
        if primera:
            primera = False
        else:
            post_id, _, _, usuario_id, _, _, _, fecha = linea.strip().split(",")
            fecha_post = fecha_a_tupla(fecha)

            # Obtenemos la fecha de creacion del usuario.
            datos_usuario = obtener_datos_por_id(archUsuarios, usuario_id)
            fecha_usuario =  fecha_a_tupla(datos_usuario[2])
            # Comparamos las fechas como tuplas (elemento a elemento)
            if fecha_post < fecha_usuario:
                posts_erroneos.append(post_id)
    posts.close()
    return posts_erroneos


def contarEtiquetas(archPosts):
    etiquetas_dict = dict()
    primera = True

    arch = open(archPosts)
    for linea in arch:
        if primera:
            primera = False
        else:
            post_id, _, _, _, etiquetas, _, _, _ = linea.strip().split(",")

            etiquetas_lista = etiquetas.split("-")
            for eti in etiquetas_lista:
                # Verificamos si tenemos la etiqueta en el diccionario antes
                # de agregar el post a dicha etiqueta.
                if eti not in etiquetas_dict:
                    etiquetas_dict[eti] = list()
                etiquetas_dict[eti].append(post_id)
    arch.close()
    return etiquetas_dict
