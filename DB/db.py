from DB.prueba import prueba


class db:

    data = prueba()
    data.verData('pet')
    data.createDb('libros')
    data.deleteDb('libros')