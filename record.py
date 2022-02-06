from flask import Blueprint,Flask,request
from flask_mysqldb import MySQL
app = Flask(__name__)
record = Blueprint("record",__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'vishwa'
app.config["MYSQL_PASSWORD"] = 'Password.123'
app.config["MYSQL_DB"] = 'shopping'

mysql = MySQL(app)

@record.route("/records")
def v():
    try:
        mycursor = mysql.connection.cursor()
        mycursor.execute("SELECT * FROM customers")
        result = mycursor.fetchall()
        customer_result = []
        for  i in range(len(result)):
            data = {'Name':result[i][0],
            'Age':result[i][1],
			'Gender':result[i][2]}
            customer_result.append(data)
        return {"Customer Records":customer_result}
    except:
        return "404 error found"