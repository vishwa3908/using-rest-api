from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
newlog = Blueprint("newlog",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@newlog.route("/customer",methods=["POST"])
def new_customer():
	try:
		mycursor = mysql.connection.cursor()
		name = request.json["name"].capitalize()
		mycursor.execute("CREATE TABLE IF NOT EXISTS {}(ITEM_TYPE VARCHAR(20) , ITEM VARCHAR(33) ,PRICE INT)".format(name.capitalize()))
		age = request.json["age"]
		gender = request.json["gender"].capitalize()
		password = request.json["password"]
		mycursor.execute("INSERT INTO customers(NAME,AGE,GENDER,PASSWORD)VALUES(%s,%s,%s,%s)",(name,age,gender,password))
		mysql.connection.commit()
		return {'name':name,"age":age,"gender":gender}
	except:
		return "Error 404"