from DB.conection import conection


class prueba(conection):

    def __init__(self):
        self.mydb = conection.mydb
        self.cursor = self.mydb.cursor()

    def verData(self,tableName):
        try:
            self.cursor.execute("select * from "+tableName)
            fname = self.cursor.fetchall()
            #for data in fname:
            #   for val in data:
            #      print(val)
            for row in fname:
                print("name: ", row[0])
                print("owner: ", row[1])
                print("species: ", row[2])
                print("sex: ", row[3])
                print("birth: ", row[4])
                print("death: ", row[5])
            self.mydb.commit()
        except sql.Error as error:
            print("error de consulta"+error)

    def createDb(self, DBname):
        try:
            self.cursor.execute("CREATE DATABASE " + DBname)
            self.cursor.execute("show databases")
            Dbs = self.cursor.fetchall()

            for i in Dbs:
                if i == (DBname,):
                    print("Database ", DBname, " creada con exito")
                    break
        except sql.Error as error:
            print("error de consulta"+error)

    def deleteDb(self, DBname='foo'):
        try:
            self.cursor.execute("show databases")
            Dbs = self.cursor.fetchall()
            if (DBname,) in Dbs:
                for db in Dbs:
                    if db == (DBname,):
                        self.cursor.execute("drop database "+ DBname)
                        print("DataBase eleminada con exito")
                        break
            else:
                print("DataBase no existente")
        except sql.Error as error:
            print("error de consulta"+error)

## otros comandos:
#craer una database
#cursor.execute("CREATE DATABASE " + DBname)
#ver las databases existentes
#cursor.execute("show databases")
#eliminar una database
#cursor.execute("drop database "+ DBname)
#crear table
#cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
#actualizacion
#cursor.execute("UPDATE users SET name = 'Kareem' WHERE id = 1")