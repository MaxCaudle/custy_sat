from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from models import Base, Rating

import datetime

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def add_rating(rating, session):
    session.add(rating)
    session.commit()


s = Session()

rating = Rating(
    device = "test",
    date = datetime.datetime.now(),
    rating = 5
)
add_rating(rating, s)
print(s.query(Rating).first())
s.close()
