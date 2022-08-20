from mysql import connector

def connetDataBase():
    connection = connector.connect(host='localhost',
                                         database='pruebaBlob',
                                         user='root',
                                         password='')
    return connection