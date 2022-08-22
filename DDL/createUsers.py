from mysql import connector

def ddlCreateUsersTable(connection):
    sql = """CREATE TABLE users(id INT PRIMARY KEY,\
    name VARCHAR (255) NOT NULL, profile_pic BLOB NOT NULL) """
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        print("Tabla creada correctamente!!!")
    except connector.Error as error:
        print(format(error))
