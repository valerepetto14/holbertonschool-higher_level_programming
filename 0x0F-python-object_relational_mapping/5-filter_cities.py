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
    try:
        db = MySQLdb.connect("localhost", username, password, name)
        cursor = db.cursor()
        cursor.execute("SELECT cities.name\
                        FROM cities\
                        JOIN states on states.id = cities.state_id\
                        WHERE states.name = %(argument)s\
                        ORDER BY states.id ASC\
                        """, {'argument': argument_search})
        data = cursor.fetchall()
        cont = len(data)
        cont2 = 0
        for row in data:
            for row1 in row:
                print(row1, end="")
                cont2 = cont2 + 1
                if(cont2 != cont):
                    print(", ", end="")
        print()
        cursor.close()
        db.close()
    except(Exception) as error:
        print(error)
