from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
cartrecord = Blueprint("cartrecord",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@cartrecord.route("/record/<name>")
def customer_cart(name):
	try:
		mycursor = mysql.connection.cursor()
		mycursor.execute("SELECT * FROM {}".format(name.capitalize()))
		result = mycursor.fetchall()
		if result:
			sub_category = []
			for i in range(len(result)):
				data = {"Item-Type":result[i][0],
				'Item':result[i][1],
				'Price':"Rs"+" "+str(result[i][2])}
				sub_category.append(data)
			return {"{}".format(name):sub_category}
		else:
			return "Nothing on Cart"
	except:
		return "404 Error"