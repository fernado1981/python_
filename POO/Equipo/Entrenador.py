class entrenadores:
    jugadores = {}
    Entrenadores = {}

    def __init__(self, jug, Ent):
        self.jugadores = jug
        self.Entrenadores = Ent
        self.Entrenadores = list(self.Entrenadores)
        self.jugadores = list(self.jugadores)

    def changeEntrenador(self, jug, Ent):
        for i in self.Entrenadores:
            if i == "Juan":
                pos = self.Entrenadores.index(Ent)
                self.Entrenadores.pop(pos)
        self.Entrenadores.append(jug)

    def addEntrenador(self, Ent):
        self.Entrenadores.append(Ent)

    def delEntrenador(self, Ent):
        pos = self.Entrenadores.index(Ent)
        self.Entrenadores.pop(pos)

    def addJugador(self, Jug):
        self.jugadores.append(Jug)

    def delJugador(self, Jug):
        pos = self.jugadores.index(Jug)
        self.jugadores.pop(pos)

    def show(self):
        self.Entrenadores = set(self.Entrenadores)
        self.jugadores = set(self.jugadores)
        print(self.jugadores)
        print(self.Entrenadores)
