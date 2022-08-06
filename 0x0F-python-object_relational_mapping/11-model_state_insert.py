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
    Louisiana = State("Louisiana")
    session.add(Louisiana)
    session.commit()
    id = session.query(State).filter(State.name == Louisiana.name).all()
    session.close()

    print(id[0].id)
