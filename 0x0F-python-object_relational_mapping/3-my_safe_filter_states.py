#!/usr/bin/python3
"""
Once again, write a script that takes in arguments and displays all values 
in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!
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
        cursor.execute("SELECT * FROM states WHERE states.name  = %(argument)s\
                    ORDER BY states.id ASC""", {'argument': argument_search})
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
        db.close()
    except(Exception) as error:
        print(error)
