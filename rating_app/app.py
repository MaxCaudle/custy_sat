from flask import Flask, render_template,request, redirect, url_for

from helpers import add_rating, get_session


app = Flask(__name__)

engine, Session = get_session()

@app.route('/', methods=['GET','POST'])
def log_device():
    if request.method == 'POST':
        return redirect(url_for('.buttons', location=request.form.get('location')))
    return render_template('login.html')

@app.route('/buttons', methods=['GET','POST'])
def buttons():
    s = Session()
    if request.method == 'POST':
        rating = request.form.get('rating')
        location = request.args.get('location')
        print(f"calling add_rating with rating: {rating} and  location: {location}")
        add_rating(Session, rating, location=request.args.get('location'))
    return render_template('survey.html', location=request.args.get('location'))


if __name__ == "__main__":
    app.run()

