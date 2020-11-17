grupos = [
    # (letraGrupo, listaEquipos)
    ("A", ["Brasil", "Peru", "Venezuela", "Bolivia"]),
    ("B", ["Colombia", "Paraguay", "Catar", "Argentina"]),
    ("C", ["Chile", "Uruguay", "Ecuador", "Japon"])
]

detalles_puntaje = [
    # (Pais, partidosjugados, ganados, empatados, perdidos, goles a favor, 
    #  goles en contra, diferenciagoles, puntos)
    ("Argentina", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Brasil", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Bolivia", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Catar", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Chile", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Colombia", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Ecuador", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Japon", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Paraguay", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Peru", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Uruguay", 0, 0, 0, 0, 0, 0, 0, 0),
    ("Venezuela", 0, 0, 0, 0, 0, 0, 0, 0)
]



def mismo_grupo(grupos, pais1, pais2):
    return False

print(mismo_grupo(grupos, "Chile", "Japon"))
print(mismo_grupo(grupos, "Brasil", "Argentina"))






def jugar_partido(grupos, puntaje, pais1, pais2, goles1, goles2):
    lista = []
    return lista

jugar_partido(grupos, detalles_puntaje, "Brasil", "Bolivia", 3, 0)
jugar_partido(grupos, detalles_puntaje, "Venezuela", "Peru", 0, 0)
jugar_partido(grupos, detalles_puntaje, "Argentina", "Colombia", 0, 2)
jugar_partido(grupos, detalles_puntaje, "Paraguay", "Catar", 2, 2)
jugar_partido(grupos, detalles_puntaje, "Uruguay", "Ecuador", 4, 0)
jugar_partido(grupos, detalles_puntaje, "Japon", "Chile", 0, 4)
print(detalles_puntaje)





def datos_grupo(grupos, puntaje, letra_grupo):
    return ()

print(datos_grupo(grupos, detalles_puntaje, "C"))







def cuartos_de_final(grupos, puntaje):
    lista = []
    return lista

print(cuartos_de_final(grupos, detalles_puntaje))
