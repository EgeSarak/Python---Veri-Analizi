import mysql.connector

def getProductInfo():
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    #sql="select count(*) from products"
    #sql="select count(name) from products"

    #sql="select avg(price) from products"
    #sql="select sum(price) from products"
    #sql="select min(price) from products"
    sql="select max(price) from products"

    cursor.execute(sql)
    result=cursor.fetchone()
  
    print(f"result: {result[0]}")

getProductInfo()    