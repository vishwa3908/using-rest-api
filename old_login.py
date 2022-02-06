from re import A
from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL



app = Flask(__name__)

old_login= Blueprint("old_login",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)



@old_login.route("/login",methods = ["POST"])
def old_customer_login():
	try:
		name = request.json["name"].capitalize()
		password = request.json["password"]
		value = (name,password,)
		mycursor = mysql.connection.cursor()
		query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
		mycursor.execute(query,value)
		result = mycursor.fetchall()
		if result:
			data = {"Name":result[0][0],"Age":result[0][1],"Gender":result[0][2]}
			return data
		else:
			return "No record found"
	except:
		return "404 error"