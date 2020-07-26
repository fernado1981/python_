from POO.Alumnos.alumnado import alumnado
from POO.Alumnos.profesor import profesor


class alumnos:

    student = alumnado()
    #student.addalumno()
    student.delAlumno(533865004)
    Alumnos = student.getAlumno()

    A1 = profesor(Alumnos, 'Fernando')
    A1.aprobar()
    A1.suspender()
    A1.amonestaciones(6)
    A1.desamonestar(4)
    #A1.verAlumnado()
    #A1.suspensos()
    A1.aprobados()
