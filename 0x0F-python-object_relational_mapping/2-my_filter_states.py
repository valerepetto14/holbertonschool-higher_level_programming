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
    argument_search = argv[4]
    db = MySQLdb.connect("localhost", username, password, name)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states WHERE name\
                    LIKE BINARY '{argument_search}' ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
