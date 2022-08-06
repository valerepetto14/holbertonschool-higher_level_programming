#!/usr/bin/python3
"""
Start link class to table in database
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State.name, City.id, City.name).join(City).all()
    for i in data:
        print(f"{state_city[0]}: ({state_city[1]}) {state_city[2]}")
    session.commit()
    session.close()
