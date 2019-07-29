from models import Rating
from config import DATABASE_URI

import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def _recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def get_session():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    return Session

def add_rating(Session, rating, rating_time=None):
    session = Session()
    if not rating_time:
        rating_time = datetime.datetime.now()
    rating = Rating(device = "test",
                    date = rating_time,
                    rating = rating
                    )

    session.add(rating)
    session.commit()
    session.close()

def add_data(n):
    import numpy as np
    from random import randrange
    import time

    Session = get_session()

    start_timestamp = time.mktime(time.strptime('Jun 1 2019  01:33:00', '%b %d %Y %I:%M:%S'))
    end_timestamp = time.mktime(time.strptime('Aug 1 2019  12:33:00', '%b %d %Y %I:%M:%S'))

    for _ in range(n):
        rating = np.random.randint(1,4)
        rating_time = time.strftime('%b %d %Y %I:%M:%S', time.localtime(randrange(start_timestamp,
                                                                                  end_timestamp)))
        add_rating(Session, rating, rating_time)