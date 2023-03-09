import mysql.connector

my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="app"
)