from connection import  connector, connetDataBase
from DDL.createUsers import ddlCreateUsersTable
from DML import insert,select

#Para convertir el archivo en binario
from convertFile import convert_data

# Necesario para la obtención de
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def insertUser(connection,id,name,fileName):
    try:
        cursor = connection.cursor()    
        insert.dmlInsertUser(cursor,id,name,fileName)
        connection.commit()
        print("Successfully Inserted Values")
    except connector.Error as error:
        print(format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    
def selectUser(name,connection):
    try:
        cursor = connection.cursor()    
        select.dmlSelectUSer(name,connection)
        connection.commit()
    except connector.Error as error:
        print(format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    connection = connetDataBase()
    selectUser("Will Smith",connection)
