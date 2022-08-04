import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["node-app"]
mycollection=mydb["products"]

#result=mycollection.find_one()
#print(result)


#for i in mycollection.find({},{"_id":0,"name":1,"price":1}):  #id gelmez
#    print(i)

#for i in mycollection.find({},{"_id":0,"name":0}):  #sadece price gelir
#    print(i)    

#for i in mycollection.find({},{"name":1}):  #id ve name gelir,price gelmez
#    print(i)   

#for i in mycollection.find({},{"_id":0,"name":1}):  #sadece name gelir
#    print(i)   



