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
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=name,
                         charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
