from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
addsubcategory = Blueprint("addsubcategory",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)











@addsubcategory.route("/categories/add/subcategory",methods=["POST"])
def add_subcategory():
	try:
		mycursor = mysql.connection.cursor()
		category_name = request.json["category"].capitalize()
		check_category_value = (category_name,)
		check_category_query = '''SELECT * FROM category WHERE CATEGORY_NAME = %s'''
		mycursor.execute(check_category_query,check_category_value)
		category_result= mycursor.fetchall()
		if category_result:
			sub_category_name = request.json["sub-category"].capitalize()
			price  = request.json["price"]
			mycursor.execute('''INSERT INTO {}(ITEMS,PRICE)VALUES(%s,%s)'''.format(category_name),(sub_category_name,price))
			mysql.connection.commit()
			return "{} subcategory created".format(sub_category_name)
		else:
			return "No category Found"
	except:
		return "404 Error"