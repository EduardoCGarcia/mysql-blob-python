from connection import connetDataBase, connector
from DDL.createUsers import ddlCreateUsersTable
from DML.insert import dmlInsertUser


    

 
if __name__ == "__main__":
    try:
        connection = connetDataBase()
        #ddlCreateUsersTable(connection)
        cursor = connection.cursor()
        
        dmlInsertUser(cursor,"1","Eduardo","eduardo.jpg")
        
        
        connection.commit()
        print("Successfully Inserted Values")
        
        
    except connector.Error as error:
        print(format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


