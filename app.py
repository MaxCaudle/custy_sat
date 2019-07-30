from flask import Flask, render_template

from helpers import add_rating, get_session


app = Flask(__name__)

engine, Session = get_session()

@app.route('/')
def buttons():
    s = Session()
    return render_template('survey.html')

@app.route('/background_add_1')
def background_add_1():
    print("calling add 1")
    add_rating(Session, 1)
    return "nothing"

@app.route('/background_add_2')
def background_add_2():
    print("calling add 2")
    add_rating(Session, 2)
    return "nothing"

@app.route('/background_add_3')
def background_add_3():
    print("calling add 3")
    add_rating(Session, 3)
    return "nothing"

if __name__ == "__main__":
    app.run()

