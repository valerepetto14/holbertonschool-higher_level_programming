#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    name = argv[3]
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
