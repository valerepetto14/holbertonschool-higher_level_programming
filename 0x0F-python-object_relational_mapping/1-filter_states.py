#!/usr/bin/python3
"""
sql alchemy
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    username = argv[1]
    password = argv[2]
    name = argv[3]
    db = MySQLdb.connect("localhost", username, password, name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY states.id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
