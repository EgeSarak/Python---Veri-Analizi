import mysql.connector



#sabit olarak bilgileri verdik tabloya ekledik
"""
def insertProduct():
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    sql="insert into products(name,price,imageUrl,description) values (%s,%s,%s,%s)"
    values=("Samsung S5",1000,"1.jpg","iyi telefon")

    cursor.execute(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")        


insertProduct()   """



#kullanıcıdan aldığımız bilgilerli tabloya ekledik
"""
def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    sql="insert into products(name,price,imageUrl,description) values (%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id: {cursor.lastrowid})
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")        

name=input("Ürün adı: ")
price=float(input("Ürün fiyatı: "))
imageUrl=input("Ürün resim adı:")
description=input("ürün açıklaması")


insertProduct(name,price,imageUrl,description) """



def insertProducts(list):
    connection=mysql.connector.connect(host="localhost",user="root",password="Es190897?",database="node-app")
    cursor=connection.cursor()

    sql="insert into products(name,price,imageUrl,description) values (%s,%s,%s,%s)"
    values=list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")        

list=[]
while True:
    name=input("Ürün adı: ")
    price=float(input("Ürün fiyatı: "))
    imageUrl=input("Ürün resim adı:")
    description=input("ürün açıklaması:")

    list.append((name,price,imageUrl,description))

    result=input("devam etmek istiyoru musunuz ? (e/h)")
    if result=="h":
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        insertProducts(list)
