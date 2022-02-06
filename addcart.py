from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
add_cart_item = Blueprint("add_cart_item",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@add_cart_item.route("/categories",methods = ["POST"])
def add_cart():
	try:
		mycursor = mysql.connection.cursor()
		name = request.json["name"].capitalize()
		password = request.json["password"]
		item = request.json["item"].capitalize()
		item_type = request.json["item-type"].capitalize()

		customer_record_value = (name,password,)

		customer_record_query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''

		mycursor.execute(customer_record_query,customer_record_value)
		customer_record_result = mycursor.fetchall()
		if customer_record_result:
			item_check_value = (item,)
			item_check_query = '''SELECT PRICE FROM {} WHERE ITEMS = %s'''.format(item_type)
			mycursor.execute(item_check_query,item_check_value)
			item_check_result = mycursor.fetchall()
			if item_check_result:
				mycursor.execute("INSERT INTO {}(ITEM_TYPE,ITEM,PRICE)VALUES(%s,%s,%s)".format(name),(item_type,item,item_check_result[0][0]))
				mysql.connection.commit()
				return "Item added in cart"
			else:
				return " wrong Item_data"
		else:
			return "Wrong Customer Data"
	except:
		return "404error"