import mysql.connector
from mysql.connector import Error
import os


mydb = mysql.connector.connect()


def myConnection():
    connection = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("HOST_NAME"),
            user=os.getenv("USER_NAME"),
            passwd=os.getenv("USER_PASSWORD"),
            database=os.getenv("DATABASE"),
        )
        print("Connection successful")

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
