import pymongo
from bson.objectid import ObjectId


myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["node-app"]
mycollection=mydb["products"]

filter={"name":"Samsung S5"}

"""1.yöntem"""
#result=mycollection.find(filter)
#for i in result:
#    print(i)

"""2.yöntem"""
#result=mycollection.find_one(filter)
#print(result)

"""id ile çağırmak istersek"""
#result=mycollection.find_one({"_id": ObjectId("623072deff860334501fc223")})
#print(result)

"""mongoDb operatörleri"""

"""$in"""
#result=mycollection.find({
#    "name":{
#        "$in":["Samsung S5","Samsung S6"]      #samsung s5 ve s6 kayıtlarını getir
#    }
#}) 

#for i in result:
#    print(i)

"""$gt (verdiğiniz değerden büyük olan)"""

#result=mycollection.find({
#    "price":{
#        "$gt":2000     #price ı 2000 den büyük olanları getir
#    }
#}) 
#
#for i in result:
#    print(i)
#

"""$gte (verdeiğiniz değerden büyük ve eşit olanları getir)"""

#result=mycollection.find({
#    "price":{
#        "$gte":2000   #price ı 2000 e eşit ve büyük olanları getir
#    }
#}) 
#
#for i in result:
#    print(i)



"""$eq (verdeiğiniz değere eşit olanları getirir)"""

result=mycollection.find({
    "price":{
        "$eq":2000   #price ı 2000 e eşit olanları getir
    }
}) 

for i in result:
    print(i)
