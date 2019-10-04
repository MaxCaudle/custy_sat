from flask import Flask, render_template,request, redirect, url_for

from helpers import add_rating, get_session


app = Flask(__name__)

engine, Session = get_session()

@app.route('/', methods=['GET','POST'])
def log_device():
    if request.method == 'POST':
        return redirect(url_for('.buttons', location=request.form.get('location')))
    return render_template('login.html')

@app.route('/buttons')
def buttons():
    s = Session()
    return render_template('survey.html', location=request.args.get('location'))

@app.route('/background_add_1')
def background_add_1():
    location = request.args.get('location')
    print(f"calling add 1 with location: {location}")
    add_rating(Session, 1, location=location)
    return redirect(url_for('.buttons', location=request.form.get('location')))

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

