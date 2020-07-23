class Asignaturas:
    materias = {}
    lunes = {"lengua": True, "Mates": True, "Fisica": True, "Historia": True}
    martes = {"lengua": False, "Mates": True, "Fisica": True, "Historia": False}
    miercoles = {"lengua": True, "Mates": True, "Fisica": False, "Historia": False}
    jueves = {"lengua": False, "Mates": False, "Fisica": True, "Historia": True}
    viernes = {"lengua": True, "Mates": False, "Fisica": False, "Historia": True}

    materias['lunes'] = [lunes]
    materias['martes'] = [martes]
    materias['miercoles'] = [miercoles]
    materias['jueves'] = [jueves]
    materias['viernes'] = [viernes]

    diasSemana = []
    x = 0

    def __init__(self, dias):
        self.diasSemana = dias

    def asiganturasTrue(self, dia):
        if dia in self.diasSemana:
            if dia in self.diasSemana:
                self.x = dia
                for c, v in self.materias.items():
                    if c == dia:
                        print("el ",dia)
                        for c in v:
                            for c, v in c.items():
                                if v:
                                    print("tienes", c)
                                else:
                                    pass
