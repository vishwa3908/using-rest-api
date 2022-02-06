from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
sub_category = Blueprint("sub_category",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'

mysql = MySQL(app)

@sub_category.route("/categories/<sub>")
def subcategory(sub):
	try:
		mycursor = mysql.connection.cursor()
		mycursor.execute("SELECT * FROM {}".format(sub.capitalize()))
		result = mycursor.fetchall()
		if result:
			sub_category = []
			for i in range(len(result)):
				data = {"ID":result[i][0],
				'Item':result[i][1],
				'Price':"Rs"+" " + str(result[i][2])}
				sub_category.append(data)
			return {"{}".format(sub.capitalize()):sub_category}
		else:
			return "Empty"
	except:
		return "404 Error"