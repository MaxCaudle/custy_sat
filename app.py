from flask import Flask
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from models import Rating

app = Flask(__name__)

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@app.route('/')
def hello():
    s = Session()
    a = str(repr(s.query(Rating).first()))
    print(a)
    return a
    #return "hello"

if __name__ == "__main__":
    app.run()

