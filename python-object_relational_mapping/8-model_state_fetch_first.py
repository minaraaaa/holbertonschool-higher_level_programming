#!/usr/bin/python3
"""
Verilənlər bazasındakı ilk State obyektini çap edən skript.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Arqumentlərin götürülməsi
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Engine yaradılması (localhost:3306)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Sessiyanın yaradılması
    Session = sessionmaker(bind=engine)
    session = Session()

    # İlk state obyektinin tapılması (states.id-yə görə)
    # .first() metodundan istifadə edərək bütün datanı çəkmədən birini alırıq
    first_state = session.query(State).order_by(State.id).first()

    # Nəticənin çap olunması
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Sessiyanın bağlanması
    session.close()
