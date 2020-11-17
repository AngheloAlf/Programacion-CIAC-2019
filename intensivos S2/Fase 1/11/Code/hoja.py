# Pregunta 1

def crearUsuario(archUsuarios, nombre, fecha):

    return False

#print('>>> print(crearUsuario("usuarios.csv", "full detonao", (2020, 2, 12)))')
#print(crearUsuario("usuarios.csv", "full detonao", (2020, 2, 12)))
#print('>>> print(crearUsuario("usuarios.csv", "jaja xd", (2020, 2, 12)))')
#print(crearUsuario("usuarios.csv", "jaja xd", (2020, 2, 12)))



def cambiarNombreUsuario(archUsuarios, idUser, nombreNuevo):
    nombre_cambiado = False

    return nombre_cambiado

#print('>>> print(cambiarNombreUsuario("usuarios.csv", "42", "cool_guy"))')
#print(cambiarNombreUsuario("usuarios.csv", "42", "cool_guy"))
#print('>>> print(cambiarNombreUsuario("usuarios.csv", "24", "animal_lover"))')
#print(cambiarNombreUsuario("usuarios.csv", "24", "animal_lover"))



def buscarPostsFechaIncorrecta(archPosts, archUsuarios):
    posts_erroneos = list()

    return posts_erroneos

#print('>>> print(buscarPostsFechaIncorrecta("posts.csv", "usuarios.csv"))')
#print(buscarPostsFechaIncorrecta("posts.csv", "usuarios.csv"))



def contarEtiquetas(archPosts):
    etiquetas_dict = dict()

    return etiquetas_dict

#print('>>> print(contarEtiquetas("posts.csv"))')
#print(contarEtiquetas("posts.csv"))




# Pregunta 2

def postear(archPosts, archUsers, titulo, url, usuario, etiquetas, fecha):

    return False

titu = "ski-ba-bop,ba-dop-bop"
url = "https://youtu.be/Hy8kmNEo1i8"
fecha = (2020, 2, 12)
etiquetas = ["musica", "retro"]

url2 = "http://pagina.falsa/meme"

#print('>>> print(postear("posts.csv", "usuarios.csv", titu, url, "cool_guy", etiquetas, fecha))')
#print(postear("posts.csv", "usuarios.csv", titu, url, "cool_guy", etiquetas, fecha))
#print('>>> print(postear("posts.csv", "usuarios.csv", "jaja", url2, "hackerman", etiquetas, fecha))')
#print(postear("posts.csv", "usuarios.csv", "jaja", url2, "hackerman", etiquetas, fecha))



def upvotePost(archPost, archUsers, idPost, username):

    return False

def downvotePost(archPost, archUsers, idPost, username):

    return False

#print('>>> print(downvotePost("posts.csv", "usuarios.csv", "75", "usuario_falso"))')
#print(downvotePost("posts.csv", "usuarios.csv", "75", "usuario_falso"))
#print('>>> print(upvotePost("posts.csv", "usuarios.csv", "75", "jaja xd"))')
#print(upvotePost("posts.csv", "usuarios.csv", "75", "jaja xd"))



def actualizarCantidadPosts(archUsers, archPosts):
    posts_totales = 0

    return posts_totales

#print('>>> print(actualizarCantidadPosts("usuarios.csv", "posts.csv"))')
#print(actualizarCantidadPosts("usuarios.csv", "posts.csv"))



def mostrarPost(archPost, idPost):
    post = dict()

    return post

#print('>>> print(mostrarPost("posts.csv", "74"))')
#print(mostrarPost("posts.csv", "74"))




# Pregunta 3

def comentar(archComs, archPosts, archUsers, idPost, username, com, fecha):

    return False

com = "que adorable!"
fecha = (2020, 2, 12)

#print('>>> print(comentar("comentarios.csv", "posts.csv", "usuarios.csv", "1", "ultimate_chef", com, fecha))')
#print(comentar("comentarios.csv", "posts.csv", "usuarios.csv", "1", "ultimate_chef", com, fecha))



def comentariosDePost(archComs, archPosts, idPost):
    comentarios = dict()

    return comentarios

#print('>>> print(comentariosDePost("comentarios.csv", "posts.csv", "39"))')
#print(comentariosDePost("comentarios.csv", "posts.csv", "39"))
#print('>>> print(comentariosDePost("comentarios.csv", "posts.csv", "45"))')
#print(comentariosDePost("comentarios.csv", "posts.csv", "45"))
#print('>>> print(comentariosDePost("comentarios.csv", "posts.csv", "800"))')
#print(comentariosDePost("comentarios.csv", "posts.csv", "800"))



def borrarComentariosFechaErronea(archComs, archPosts, archUsers):
    comentarios_borrados = []

    return comentarios_borrados

#print('>>> print(borrarComentariosFechaErronea("comentarios.csv", "posts.csv", "usuarios.csv"))')
#print(borrarComentariosFechaErronea("comentarios.csv", "posts.csv", "usuarios.csv"))



def eliminarPost(archPosts, archComs, idPost):
    comentarios_borrados = 0

    return comentarios_borrados

#print('>>> print(eliminarPost("posts.csv", "comentarios.csv", "42"))')
#print(eliminarPost("posts.csv", "comentarios.csv", "42"))



def actualizarPuntajeUsers(archUsers, archPosts, archComs):
    upvotes_totales = 0
    downvotes_totales = 0

    return (upvotes_totales, downvotes_totales)

#print('>>> print(actualizarPuntajeUsers("usuarios.csv", "posts.csv", "comentarios.csv"))')
#print(actualizarPuntajeUsers("usuarios.csv", "posts.csv", "comentarios.csv"))



# Felicidades por llegar hasta el final! :D

