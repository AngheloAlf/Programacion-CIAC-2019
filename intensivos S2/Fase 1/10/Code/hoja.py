# Pregunta 1

def crearUsuario(archUsuarios, nombre, fecha):
    return False

# print(crearUsuario("usuarios.csv", "full detonao", (2020, 2, 12)))
# print(crearUsuario("usuarios.csv", "jaja xd", (2020, 2, 12)))


def cambiarNombreUsuario(archUsuarios, idUser, nombreNuevo):
    return False

# print(cambiarNombreUsuario("usuarios.csv", "42", "cool_guy"))
# print(cambiarNombreUsuario("usuarios.csv", "24", "animal_lover"))


def buscarPostsFechaIncorrecta(archPosts, archUsuarios):
    return list()

# print(buscarPostsFechaIncorrecta("posts.csv", "usuarios.csv"))


def postear(archPosts, archUsers, titulo, url, usuario, etiquetas, fecha):
    return False

titu = "ski-ba-bop,ba-dop-bop"
url = "https://www.youtube.com/watch?v=Hy8kmNEo1i8"
fecha = (2020, 2, 12)
etiquetas = ["musica", "retro"]
# postear("posts.csv", "usuarios.csv", titu, url, "cool_guy", etiquetas, fecha)

url2 = "http://pagina.falsa/meme"
# postear("posts.csv", "usuarios.csv", "jaja", url2, "hackerman", [], fecha)


def contarEtiquetas(archPosts):
    return dict()

# print(contarEtiquetas("posts.csv"))


def actualizarCantidadPosts(archUsuarios, archPosts):
    return 0

# print(actualizarCantidadPosts("usuarios.csv", "posts.csv"))


def ordenarPorId(archivo):
    return None

# ordenarPorId("usuarios.csv")


def mostrarPost(archPost, idPost):
    return dict()

# print(mostrarPost(archPost, idPost))



# Pregunta 2

def comentar(archComs, archPosts, archUsers, idPost, username, com, fecha):
    return False

com = "que adorable!"
fecha = (2020, 2, 12)
# print(comentar("comentarios.csv", "posts.csv", "usuarios.csv", "1", "ultimate_chef", com, fecha))


def comentariosDePost(archComs, archPosts, idPost):
    return dict()

# print(comentariosDePost("comentarios.csv", "posts.csv", "39"))
# print(comentariosDePost("comentarios.csv", "posts.csv", "45"))


def borrarComentariosFechaErronea(archComs, archPosts, archUsers):
    return 0

# borrarComentariosFechaErronea("comentarios.csv", "posts.csv", "usuarios.csv")


def eliminarPost(archPosts, archComentarios, idPost):
    return 0

# print(eliminarPost("posts.csv", "comentarios.csv", "42"))


def actualizarPuntajeUsers(archComs, archPosts, archUsers):
    return 0

# actualizarPuntajeUsers("comentarios.csv", "posts.csv", "usuarios.csv")
