from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
log = Blueprint("log",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@log.route("/login")
def login():
	try:
		return "For old customer enter login/name/password and for new customer enter /record/name"
	except:
		return "Error"