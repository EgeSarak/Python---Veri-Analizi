import mysql.connector
from datetime import datetime

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Es190897?",
    database="schooldb"
)

mycursor=connection.cursor()

sql="insert into Student(StudentNumber,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"

ogrenciler=[
    ("101","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
    ("102","Ali","Can",datetime(2005,6,17),"E"),
    ("103","Canan","Tan",datetime(2005,7,7),"K"),
    ("104","Ayşe","Taner",datetime(2005,9,23),"K"),
    ("105","Bahadır","Toksöz",datetime(2004,7,27),"E"),
    ("106","Ali","Cenk",datetime(2003,8,25),"K")
]

mycursor.executemany(sql,ogrenciler) #liste olduğu için executemany kullandık,yoksa execute kullanıyoruz.

try:
    connection.commit()
    print(f"{mycursor.rowcount} tane kayıt eklendi")
except mysql.connector.Error as err:
    print("hata",err)
finally:
    connection.close()        