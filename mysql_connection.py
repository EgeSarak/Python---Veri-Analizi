import mysql.connector

mydb= mysql.connector.connect(
    host="localhost", 
    user="root",
    password="Es190897?",
    database="node-app"
)

mycursor=mydb.cursor()









# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),adress VARCHAR(255))")


# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE DATABASE mydatabase")

#for x in mycursor:
 #   print(x)


print(mydb)
