#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

argument = sys.argv[4]

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    datos = session.query(State).filter(State.name == f"{argument}").all()
    session.close()

    if(len(datos) != 0):
        for i in datos:
            print(i.id)
    else:
        print("Not found")
