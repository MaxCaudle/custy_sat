from database.models import Rating
from config import DATABASE_URI

import datetime
import numpy as np


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def _recreate_database():
    engine, Session = get_session()
    Base = declarative_base()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_session():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    return engine, Session


def add_rating(Session, rating, rating_time=None, location="test"):
    session = Session()
    if not rating_time:
        rating_time = datetime.datetime.now()
    rating = Rating(device = location,
                    date = rating_time,
                    rating = rating
                    )

    session.add(rating)
    session.commit()
    session.close()


def generate_data(n):
    engine, Session = get_session()
    for i in range(n):
        date = datetime.datetime.now() - datetime.timedelta(seconds=np.random.randint(31*24*60*60))
        add_rating(Session, np.random.randint(0, 4), date)


def add_data(n):
    import numpy as np
    from random import randrange
    import time

    engine, Session = get_session()

    start_timestamp = time.mktime(time.strptime('Jun 1 2019  01:33:00', '%b %d %Y %I:%M:%S'))
    end_timestamp = time.mktime(time.strptime('Aug 1 2019  12:33:00', '%b %d %Y %I:%M:%S'))

    for _ in range(n):
        rating = np.random.randint(1,4)
        rating_time = time.strftime('%b %d %Y %I:%M:%S', time.localtime(randrange(start_timestamp,
                                                                                  end_timestamp)))
        add_rating(Session, rating, rating_time)