from flask import Flask, render_template, session, request, url_for, redirect,flash
# from hello import db, User, NameForm
from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField

from passlib.hash import sha256_crypt

from MySQLdb import escape_string as thwart

from dbconnect import connection
import gc
from functools import wraps

app = Flask(__name__)
app.secret_key = 'diljev87ej983jkv'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for("login"))
    return wrap

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard/dashboard.html")

@app.route('/login1/')
def login1():
    return render_template("login1.html")

@app.route('/dashboard2/')
def dashboard2():
    return render_template("dashboard/dashboard2.html")

@app.route('/dashboard3/')
def dashboard3():
    return render_template("dashboard/dashboard3.html")

@app.route('/chartjs/')
def chartjs():
    return render_template("dashboard/chartjs.html")

@app.route('/chartjs2/')
def chartjs2():
    return render_template("dashboard/chartjs2.html")

@app.route('/chartjs3/')
def chartjs3():
    return render_template("dashboard/chartjs3.html")

@app.route('/videos/')
@login_required
def videos():
    return render_template("videos.html")

@app.route('/location/')
def location():
    return render_template("location.html")

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4,max=20)])
    email = StringField('Email Address', [validators.Length(min=4, max=50)])
    password = PasswordField('Password',[validators.DataRequired(),validators.EqualTo('confirm',message="Passwords must match.")])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the <a href="/tos/">Terms of the service</a> and the <a href="/privacy/">Privacy Notice</a> (Last updated Oct,2017)',[validators.Required()])


@app.route('/register/', methods = ['GET','POST'])
def singup():
    # flash("flash test!!!!")
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = '{}'".format(thwart(username)))

            if int(x)>0:
                flash("That username is already taken, please chose another")
                return render_template("register.html", form=form)

            else:
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES ('{}', '{}', '{}', '{}')".format(thwart(username),thwart(password),thwart(email),thwart("/index/")))

                conn.commit()

                flash("Thanks for registering!")
                c.close()
                conn.close()

                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('videos'))

        return render_template("register.html",form=form)

    except Exception as e:
        return(str(e))

@app.route('/contact/')
def contact():
    # flash("Welcome, please login")
    return render_template("contact.html")

@app.route('/d3inaction/')
def d3inaction():
    # flash("Welcome, please login")
    return render_template("d3inaction.html")

@app.route('/matplotlib/')
def matplotlib():
    # flash("Welcome, please login")
    return render_template("matplotlib.html")

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You are logged out")
    gc.collect()
    return redirect(url_for("homepage"))


@app.route('/login/', methods = ['GET','POST'])
def login():
    error= ''
    try:
        c, conn = connection()
        if request.method == 'POST':
            data = c.execute("SELECT * FROM users WHERE username = '{}'".format(thwart(request.form['username'])))
            data = c.fetchone()[2]

            if sha256_crypt.verify(request.form['password'],data):
                session['logged_in'] = True
                session['username'] = request.form['username']

                flash('You are logged in successfully')

                return redirect(url_for('videos'))


            else:
                error= "Invalid Credentials"

        gc.collect()
        return render_template("login.html", error=error)

    except Exception as e:
        render_template("login.html", error=error)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def methods_not_found(e):
    return render_template('405.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__== "__main__":
    app.run()
