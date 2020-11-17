turno = 1
seguirJugando = True
while seguirJugando:
    turno = (turno+1)%2
    print("Juega el jugador", turno+1)
    jugada = input("Ingrese su jugada: ")
    contador = 5
    while traducirJugada(jugada,turno)[0] == False and contador > 0:
        contador -= 1
        if contador == 0:
            print ("Gana el jugador "+str((turno+1)%2+1)+" por jaque mate")
            seguirJugando = False
        jugada = input("Jugador "+str(turno+1)+" ingrese una jugada valida: ")
