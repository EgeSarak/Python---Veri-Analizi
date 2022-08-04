import mysql.connector

def getProducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    #cursor.execute("select * from Products") #products tablosundan  her şeyi getir
    cursor.execute("select name,price from Products") #products tablosundan name ve price ı getir

    #result=cursor.fetchall() #1 den fazla kayıt almak istediğimiz için 
    result=cursor.fetchone() #sadece bir tane kayıt getirmek istediğimizde kullanırız

    print(f"name: {result[0]} price: {result[1]}")



    #for product in result:
    #    #print(f"name:{product[1]} price: {product[2]}")
    #     print(f"name:{product[0]} price: {product[1]}")


getProducts()        

