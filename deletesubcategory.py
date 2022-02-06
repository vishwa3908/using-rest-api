from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
delsubcategory = Blueprint("delsubcategory",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'
mysql = MySQL(app)


@delsubcategory.route("/categories/delete/subcategory",methods=["DELETE"])
def delete_subcategory():
	try:
		mycursor = mysql.connection.cursor()
		sub_category = request.json["sub-category"].capitalize()
		category = request.json["category"].capitalize()
		check_existence_value = (sub_category,)
		check_existence_query = '''SELECT * FROM {} WHERE ITEMS = %s'''.format(category)
		mycursor.execute(check_existence_query,check_existence_value)
		check_existence_result = mycursor.fetchall()
		if check_existence_result:
			delete_subcategory_value = (sub_category,)
			delete_subcategory_query = '''DELETE FROM {} WHERE ITEMS = %s'''.format(category)
			mycursor.execute(delete_subcategory_query,delete_subcategory_value)
			mysql.connection.commit()
			return "{} sub-category deleted".format(sub_category)
		else:
			return "Not Found"
	except:
		return '404 Error'