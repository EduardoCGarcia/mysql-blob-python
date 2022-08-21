import string
from convertFile import convert_data

def dmlInsertUser(cursor,id:int,name:string,fileName):
    query = """ INSERT INTO users(id, name, profile_pic)\
        VALUES (%s,%s,%s)"""
    
    student_id = id
    student_name = name
    first_profile_picture = convert_data("images/" + fileName)
    
    result = cursor.execute(
            query, (student_id, student_name, first_profile_picture))