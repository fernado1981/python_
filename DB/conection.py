import mysql.connector


class conection:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="very_strong_password",
        database="prueba_db",
        auth_plugin='mysql_native_password')
