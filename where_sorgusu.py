import mysql.connector


def getProducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    cursor.execute("select * from products where name='Samsung S8' or price=3000")

    result=cursor.fetchall()

    for product in result:
        print(f"id: {product[0]} name: {product[1]} price: {product[2]}")

getProducts()    




def getProductBYId(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    sql="select * from products where id=%s"
    params=(id,)

    cursor.execute(sql,params)
    result=cursor.fetchone()
  
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

getProductBYId(3)    