import mysql.connector

user="root"
password="13231414"
host="localhost"
port=3308
database="grupoispc"



conexion= mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database)

print(conexion)