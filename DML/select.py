import base64
from PIL import Image
import io

def dmlSelectUSer(name, connection):
    query = f"SELECT profile_pic FROM users WHERE name='{name}';"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    image = data[0][0]

    
    dataByteIO = io.BytesIO(image)
    image = Image.open(dataByteIO)
    image.show()
    