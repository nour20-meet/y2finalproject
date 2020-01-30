from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")
	
@app.route('/signup' ,methods=["GET","POST"])
def signup():
	if request.method == "GET":

		return render_template("signup.html")
	else:
		add_user(request.form['name'],request.form['password'])
		return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)