import mysql.connector


db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'barezia12',
    auth_plugin = 'mysql_native_password'
)

# prepare cursor object
cursorObject = db.cursor()

# create database
cursorObject.execute("CREATE DATABASE blackoutz")

print("Database created! ")

