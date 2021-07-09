import mysql.connector

mydb = mysql.connector.connect(
    host="localhost/IP",
    user="userName",
    password="password",
    database="yourDB"
)

print("Connected!")

cur = mydb.cursor()

sql = """CREATE TABLE yourTable 
            (ID int AUTO_INCREMENT PRIMARY KEY,
             Nmae varchar(50),
             address varchar(100)
            )"""

cur.execute(sql)

print("Finished")
