from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
category = Blueprint("category",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)




@category.route("/categories")
def categories():
	try:
		mycursor = mysql.connection.cursor()
		mycursor.execute("SELECT * FROM category")
		result = mycursor.fetchall()
		category = []
		if result:
			for i in range(len(result)):
				data = {"Category":result[i]}
				category.append(data)
			return {"Categories":category}
		else:
			return "Empty "
	except:
		return "404 error"