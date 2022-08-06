#!/usr/bin/python3
"""
sql alchemy
"""


from sys import argv
import MySQLdb

username = argv[1]
password = argv[2]
name = argv[3]
argument_search = argv[4]

if __name__ == "__main__":
    try:
        db = MySQLdb.connect("localhost", username, password, name)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM states \
                        WHERE states.name ='{argument_search}'\
                                            ORDER BY states.id ASC")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
        db.close()
    except(Exception) as error:
        print(error)
