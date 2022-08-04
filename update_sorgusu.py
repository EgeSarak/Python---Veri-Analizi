from unittest import result
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["node-app"]
mycollection=mydb["products"]

mycollection.update_one(
    {"name":"Samsung S5"},
    {"$set":{
        "name":"Iphone 6",
        "price":5000
    }}
)

for i in mycollection.find():
    print(i)



    mycollection.update_many(
    {"name":"Samsung S6"},
    {"$set":{
        "name":"Iphone 8",
        "price":5000
    }}
)

for i in mycollection.find():
    print(i)



"""2.yöntem"""

query={"name":"Samsung S6"}

newvalues={"$set":{
    "name":"Iphone 8",
    "price":5000
}}

result=mycollection.update_many(query,newvalues)

print(f"{result.modified_count} adet kayıt güncellendi.")

for i in mycollection.find():
    print(i)
