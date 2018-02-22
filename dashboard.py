from flask import Flask, render_template, session, request, url_for, redirect,flash

app = Flask(__name__)
app.secret_key = 'diljev87ej983jkv'

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