#!/usr/bin/python3
"""Start link class to table in database
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    user = sys.argv[1]
    passw = sys.argv[2]
    bd = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    datos = session.query(State).all()
    session.close()
    # db.Base.metadata.create_all(db.engine)
    # db.session.add(jugo)
    # db.session.commit()
    for i in datos:
        print(i)
