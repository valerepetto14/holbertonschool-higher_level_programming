#!/usr/bin/python3
"""
Start link class to table in database
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    datos = session.query(State).order_by(State.id).first()
    session.close()
    if(datos):
        print(datos)
    else:
        print("Nothing")
