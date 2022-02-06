from flask import Flask,render_template,request,jsonify,Blueprint
from flask_mysqldb import MySQL
from Routes.customer.record import record
from Routes.login.old_login import old_login
from Routes.category.categories import category
from Routes.subcategory.sub_categories import sub_category
from Routes.category.add_category import addcategory
from Routes.subcategory.add_subcategory import addsubcategory
from Routes.login.login import log
from Routes.login.newlogin import newlog
from Routes.subcategory.deletesubcategory import delsubcategory
from Routes.customer.cart import cartrecord
from Routes.customer.addcart import add_cart_item
from Routes.customer.removecartitem import remove_cart_item




app = Flask(__name__)
app.register_blueprint(record)
app.register_blueprint(old_login)
app.register_blueprint(category)
app.register_blueprint(sub_category)
app.register_blueprint(addcategory)
app.register_blueprint(addsubcategory)
app.register_blueprint(log)
app.register_blueprint(newlog)
app.register_blueprint(delsubcategory)
app.register_blueprint(cartrecord)
app.register_blueprint(add_cart_item)
app.register_blueprint(remove_cart_item)


app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'

mysql = MySQL(app)

@app.route("/")
def home():
	return '''<h1>Welcome to Shopping buddy</h1><br> To login use <b>/login </b><br> To see record use <b>/record </b><br>
			To see categories use <b>/categories</b> <br> To see sub-category use <b>/categories/sub-category-name</b>
			<br>To see customer cart use <b>/record/name</b><br>'''

#------------------Log in Route----------------------------

# @app.route("/login")
# def login():
# 	try:
# 		return "For old customer enter login/name/password and for new customer enter /record/name"
# 	except:
# 		return "Error"


# @app.route("/login",methods = ["POST"])
# def old_customer_login():
# 	try:
# 		name = request.json["name"].capitalize()
# 		password = request.json["password"]
# 		value = (name,password,)
# 		mycursor = mysql.connection.cursor()
# 		query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
# 		mycursor.execute(query,value)
# 		result = mycursor.fetchall()
# 		if result:
# 			data = {"Name":result[0][0],"Age":result[0][1],"Gender":result[0][2]}
# 			return data
# 		else:
# 			return "No record found"
# 	except:
# 		return "404 error"


# ------------------------------------------------------------------------
#----------------------Customer record --------------------------

# @app.route("/record")
# def customer_record():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		mycursor.execute("SELECT * FROM customers")
# 		result = mycursor.fetchall()
# 		customer_result = []
# 		for  i in range(len(result)):
# 			data = {'Name':result[i][0],
# 			'Age':result[i][1],
# 			'Gender':result[i][2]}
# 			customer_result.append(data)

# 		return {"Customer Records":customer_result}
# 	except:
# 		return "404 error found"
#----------------------------Category -----------------------------

# @app.route("/categories")
# def categories():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		mycursor.execute("SELECT * FROM category")
# 		result = mycursor.fetchall()
# 		category = []
# 		if result:
# 			for i in range(len(result)):
# 				data = {"Category":result[i]}
# 				category.append(data)
# 			return {"Categories":category}
# 		else:
# 			return "Empty "
# 	except:
# 		return "404 error"

#--------------adding category--------
# @app.route("/categories/add",methods=["POST"])
# def add_category():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		category_name = request.json["category"].capitalize()
# 		category_add_value = (category_name,category_name)
# 		category_add_query = '''INSERT INTO category(CATEGORY_NAME)SELECT * FROM(SELECT %s) as temp WHERE NOT EXISTS(SELECT CATEGORY_NAME FROM category WHERE CATEGORY_NAME = %s)LIMIT 1'''
# 		mycursor.execute(category_add_query,category_add_value)
# 		mycursor.execute('''CREATE TABLE IF NOT EXISTS {}(ID INT AUTO_INCREMENT PRIMARY KEY,ITEMS VARCHAR(20),PRICE INT )'''.format(category_name))
# 		mysql.connection.commit()
# 		return "{} Category added".format(category_name)
# 	except:
# 		return "404 error"


#----------------sub-category---------------------------------------------

# @app.route("/categories/<sub>")
# def subcategory(sub):
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		mycursor.execute("SELECT * FROM {}".format(sub.capitalize()))
# 		result = mycursor.fetchall()
# 		if result:
# 			sub_category = []
# 			for i in range(len(result)):
# 				data = {"ID":result[i][0],
# 				'Item':result[i][1],
# 				'Price':"Rs"+" " + str(result[i][2])}
# 				sub_category.append(data)
# 			return {"{}".format(sub.capitalize()):sub_category}
# 		else:
# 			return "Empty"
# 	except:
# 		return "404 Error"

#------------adding sub_category--------
# @app.route("/categories/add/subcategory",methods=["POST"])
# def add_subcategory():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		category_name = request.json["category"].capitalize()
# 		check_category_value = (category_name,)
# 		check_category_query = '''SELECT * FROM category WHERE CATEGORY_NAME = %s'''
# 		mycursor.execute(check_category_query,check_category_value)
# 		category_result= mycursor.fetchall()
# 		if category_result:
# 			sub_category_name = request.json["sub-category"].capitalize()
# 			price  = request.json["price"]
# 			mycursor.execute('''INSERT INTO {}(ITEMS,PRICE)VALUES(%s,%s)'''.format(category_name),(sub_category_name,price))
# 			mysql.connection.commit()
# 			return "{} subcategory created".format(sub_category_name)
# 		else:
# 			return "No category Found"
# 	except:
# 		return "404 Error"

#-----------Deleting sub-category---------------
# @app.route("/categories/delete/subcategory",methods=["DELETE"])
# def delete_subcategory():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		sub_category = request.json["sub-category"].capitalize()
# 		category = request.json["category"].capitalize()
# 		check_existence_value = (sub_category,)
# 		check_existence_query = '''SELECT * FROM {} WHERE ITEMS = %s'''.format(category)
# 		mycursor.execute(check_existence_query,check_existence_value)
# 		check_existence_result = mycursor.fetchall()
# 		if check_existence_result:
# 			delete_subcategory_value = (sub_category,)
# 			delete_subcategory_query = '''DELETE FROM {} WHERE ITEMS = %s'''.format(category)
# 			mycursor.execute(delete_subcategory_query,delete_subcategory_value)
# 			mysql.connection.commit()
# 			return "{} sub-category deleted".format(sub_category)
# 		else:
# 			return "Not Found"
# 	except:
# 		return '404 Error'
#---------------------------customer-cart-----------------------------------------
# @app.route("/record/<name>")
# def customer_cart(name):
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		mycursor.execute("SELECT * FROM {}".format(name.capitalize()))
# 		result = mycursor.fetchall()
# 		if result:
# 			sub_category = []
# 			for i in range(len(result)):
# 				data = {"Item-Type":result[i][0],
# 				'Item':result[i][1],
# 				'Price':"Rs"+" "+str(result[i][2])}
# 				sub_category.append(data)
# 			return {"{}".format(name):sub_category}
# 		else:
# 			return "Nothing on Cart"
# 	except:
# 		return "404 Error"
# ----------------adding item in cart -------------------

# @app.route("/categories",methods = ["POST"])
# def add_cart():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		name = request.json["name"].capitalize()
# 		password = request.json["password"]
# 		item = request.json["item"].capitalize()
# 		item_type = request.json["item-type"].capitalize()

# 		customer_record_value = (name,password,)

# 		customer_record_query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''

# 		mycursor.execute(customer_record_query,customer_record_value)
# 		customer_record_result = mycursor.fetchall()
# 		if customer_record_result:
# 			item_check_value = (item,)
# 			item_check_query = '''SELECT PRICE FROM {} WHERE ITEMS = %s'''.format(item_type)
# 			mycursor.execute(item_check_query,item_check_value)
# 			item_check_result = mycursor.fetchall()
# 			if item_check_result:
# 				mycursor.execute("INSERT INTO {}(ITEM_TYPE,ITEM,PRICE)VALUES(%s,%s,%s)".format(name),(item_type,item,item_check_result[0][0]))
# 				mysql.connection.commit()
# 				return "Item added in cart"
# 			else:
# 				return " wrong Item_data"
# 		else:
# 			return "Wrong Customer Data"
# 	except:
# 		return "404error"
#----------------------removing item from cart------------------------------

# @app.route("/record/<name>",methods=["DELETE"])
# def remove_item(name):
# 	mycursor = mysql.connection.cursor()
# 	name = name.capitalize()
# 	password= request.json["password"]
# 	item_type = request.json["item-type"].capitalize()
# 	item = request.json["item"].capitalize()
# 	check_customer_value = (name,password,)
# 	check_customer_query = '''SELECT * FROM customers WHERE NAME = %s AND PASSWORD = %s'''
# 	mycursor.execute(check_customer_query,check_customer_value)
# 	check_customer_result= mycursor.fetchall()
# 	if check_customer_result:
# 		item_check_value = (item,)
# 		item_check_query = '''SELECT * FROM {} WHERE ITEMS = %s'''.format(item_type)
# 		mycursor.execute(item_check_query,item_check_value)
# 		item_check_result = mycursor.fetchall()
# 		if item_check_result:
# 			delete_cart_value = (item,)
# 			delete_cart_query = '''DELETE FROM {} WHERE ITEM = %s'''.format(name)
# 			mycursor.execute(delete_cart_query,delete_cart_value)
# 			mysql.connection.commit()
# 			return "{} Deleted".format(item)
# 		else:
# 			return "Wrong item details"

# 	else:
# 		return "Wrong item record"


#-------------------------adding customer detail in database--------------------------------------

# @app.route("/customer",methods=["POST"])
# def new_customer():
# 	try:
# 		mycursor = mysql.connection.cursor()
# 		name = request.json["name"].capitalize()
# 		mycursor.execute("CREATE TABLE IF NOT EXISTS {}(ITEM_TYPE VARCHAR(20) , ITEM VARCHAR(33) ,PRICE INT)".format(name.capitalize()))
# 		age = request.json["age"]
# 		gender = request.json["gender"].capitalize()
# 		password = request.json["password"]
# 		mycursor.execute("INSERT INTO customers(NAME,AGE,GENDER,PASSWORD)VALUES(%s,%s,%s,%s)",(name,age,gender,password))
# 		mysql.connection.commit()
# 		return {'name':name,"age":age,"gender":gender}
# 	except:
# 		return "Error 404"


if __name__ =="__main__":
	app.run(debug=True)