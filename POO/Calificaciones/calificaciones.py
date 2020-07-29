from POO.Calificaciones.alumnocalificado import calificaciones


class alumno:
    nombre = input("Alumno: ")

    nota = calificaciones(nombre)
    nota.notas()
    nota.vernotas()
    nota.medias()
    nota.setAlumno()
    nota.notas()
    nota.vernotas()
    nota.medias()
