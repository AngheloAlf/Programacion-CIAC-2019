programas = [
    # nombre, codigo,  origen, duracion en minutos, idioma
    ("El matinal", 1, "Chile", 240, "Espagnol"),
    ("Noticiero", 2, "Chile", 60, "Espagnol"),
    ("Game of Thrones", 3, "Estados Unidos", 24, "Ingles"),
    ("Reality", 4, "Chile", 60, "Espagnol"),
    ("Shingeki no Kiojin", 5, "Japon", 24, "Japones"),
    ("Las mil y una noches", 6, "Turquia", 90, "Espagnol"),
    ("La rosa de Guadalupe", 7, "Mexico", 44, "Espagnol"),
    ("Jojo's Bizarre adventures", 8, "Japon", 24, "Japones"),
    ("El chavo del ocho", 9, "Mexico", 22, "Espagnol"),
    ("Los Simpsons", 10, "Estados Unidos", 25, "Espagnol"),
    ("The late show - Paro edition", 11, "USM", 65, "Espagnol"),
    ("Copa America", 12, "Brasil", 180, "Espagnol"),
    ("Misa", 13, "Chile", 120, "Espagnol"),
    # No olvide incluir su programa favorito!
]

programas_por_dia = [
    # dia, [orden de los programas]
    ("Lunes", [1, 9, 2, 12]), 
    ("Martes", [1, 3, 7, 9, 10]), 
    ("Miercoles", [7, 4, 3, 11]), 
    ("Jueves", [4, 6, 9, 10]), 
    ("Viernes", [1, 12, 2, 10, 8]), 
    ("Sabado", [7, 2, 6, 11]), 
    ("Domingo", [13, 2, 10, 5]), 
]

dia = input('Ingrese dia: ')

print('Ese dia hay programados ', cantidad_de_programas(dia),' programas.')
print('El primer programa del dia sera', nombre_primer_programa(dia))
print('El ultimo programa del dia viene de', pais_origen_ultimo(dia))
print('La programacion completa durara ', tiempo_total(dia), ' minutos')
print('El programa mas largo del dia es ', nombre_programa_largo(dia))
print('Dicho programa dura ', tiempo_programa_largo(dia), ' minutos')
print('El idioma mas hablado de ese dia es ', idioma(dia))

print("")
print("Presentacion del dia " + dia + ":")
for prog in programacion_del_dia(dia):
    nombre, codigo, origen, duracion, idioma = prog
    print("   ",nombre, "-", duracion, "minutos - Idioma:", idioma)
