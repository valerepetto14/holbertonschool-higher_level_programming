#!/usr/bin/python3
"""
sql alchemy
"""


from sys import argv
import MySQLdb

username = argv[1]
password = argv[2]
name = argv[3]

if __name__ == "__main__":
    try:
        db = MySQLdb.connect("localhost", username, password, name)
        cursor = db.cursor()
        cursor.execute("SELECT cities.id ,cities.name, states.name\
                        FROM cities\
                        JOIN states on states.id = cities.state_id")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
        db.close()
    except(Exception) as error:
        print(error)
