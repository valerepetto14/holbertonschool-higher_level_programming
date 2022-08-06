#!/usr/bin/python3
"""
Start link class to table in database
"""


if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    stados = session.query(State).all()
    print(stados[0].cities)
    # for i in stados:
    #     print(f"{i.id}: {i.name}")
    #     for a in i.cities:
    #         print(f"    {a}")
    session.close()
