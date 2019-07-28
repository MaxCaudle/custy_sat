from flask import Flask, render_template

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from models import Rating

import datetime

app = Flask(__name__)

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def add_rating(rating):
    session = Session()
    rating = Rating(device = "test",
                    date = datetime.datetime.now(),
                    rating = rating
                    )

    session.add(rating)
    session.commit()
    session.close()

@app.route('/')
def buttons():
    s = Session()
    return render_template('survey.html')

@app.route('/background_add_1')
def background_add_1():
    add_rating(1)
    return "nothing"

@app.route('/background_add_2')
def background_add_2():
    add_rating(2)
    return "nothing"

@app.route('/background_add_3')
def background_add_3():
    add_rating(3)
    return "nothing"


if __name__ == "__main__":
    app.run()

