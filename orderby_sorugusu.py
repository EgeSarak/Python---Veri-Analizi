import mysql.connector

def getProducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    cursor.execute("select * from products order by name,price")

    result=cursor.fetchall()

    try:
        result=cursor.fetchall()
        for product in result:
         print(f"id: {product[0]} name: {product[1]} price:{product[2]}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")         

getProducts()        