import sqlite3
import pandas as pd



connection=sqlite3.connect("chinook.db")
cursor=connection.cursor()

df=pd.read_sql_query("select * from customers",connection)
df.head()
df.info()





cursor.execute("select * from customers")
result=cursor.fetchall()

for i in result:
    print(i)

connection.close()