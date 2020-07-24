from POO.Equipo.Entrenador import entrenadores


class jugador:
    jugadores = {"Marta", "David", "Elvira", "Juan", "Marcos"}
    Entrenadores = {"Juan", "Marta"}

    admin = entrenadores(jugadores, Entrenadores)
    admin.changeEntrenador('Marcos', 'Juan')
    admin.addEntrenador("David")
    admin.delEntrenador("Marta")
    admin.addJugador("Paco")
    admin.delJugador("David")
    admin.show()
