from flask import render_template
from hello_world import app
from hello_world import mysql

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/omnie")
def about():
    return render_template('about.html')

@app.route("/kontakt")
def contact():
    return render_template('contact.html')

@app.route("/wszystkiePosty")
def database_posts():
    cursor = mysql.connect().cursor()
    cursor.excute("SELECT * from flask.posty")
    data = cursor.fetchall()
    return render_template('database_posts.html', data = data)

@app.context_processor
def inject_variables():
    return dict()


