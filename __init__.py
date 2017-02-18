from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
from hello_world import views
