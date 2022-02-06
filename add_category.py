from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
addcategory = Blueprint("addcategory",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@addcategory.route("/categories/add",methods=["POST"])
def add_category():
	try:
		mycursor = mysql.connection.cursor()
		category_name = request.json["category"].capitalize()
		category_add_value = (category_name,category_name)
		category_add_query = '''INSERT INTO category(CATEGORY_NAME)SELECT * FROM(SELECT %s) as temp WHERE NOT EXISTS(SELECT CATEGORY_NAME FROM category WHERE CATEGORY_NAME = %s)LIMIT 1'''
		mycursor.execute(category_add_query,category_add_value)
		mycursor.execute('''CREATE TABLE IF NOT EXISTS {}(ID INT AUTO_INCREMENT PRIMARY KEY,ITEMS VARCHAR(20),PRICE INT )'''.format(category_name))
		mysql.connection.commit()
		return "{} Category added".format(category_name)
	except:
		return "404 error"