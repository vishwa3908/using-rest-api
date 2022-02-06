from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
remove_cart_item = Blueprint("remove_cart_item",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@remove_cart_item.route("/record/<name>",methods=["DELETE"])
def remove_item(name):
	mycursor = mysql.connection.cursor()
	name = name.capitalize()
	password= request.json["password"]
	item_type = request.json["item-type"].capitalize()
	item = request.json["item"].capitalize()
	check_customer_value = (name,password,)
	check_customer_query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
	mycursor.execute(check_customer_query,check_customer_value)
	check_customer_result= mycursor.fetchall()
	if check_customer_result:
		item_check_value = (item,)
		item_check_query = '''SELECT * FROM {} WHERE ITEMS = %s'''.format(item_type)
		mycursor.execute(item_check_query,item_check_value)
		item_check_result = mycursor.fetchall()
		if item_check_result:
			delete_cart_value = (item,)
			delete_cart_query = '''DELETE FROM {} WHERE ITEM = %s'''.format(name)
			mycursor.execute(delete_cart_query,delete_cart_value)
			mysql.connection.commit()
			return "{} Deleted".format(item)
		else:
			return "Wrong item details"

	else:
		return "Wrong item record"