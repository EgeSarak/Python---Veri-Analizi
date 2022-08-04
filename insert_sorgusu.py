import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["node-app"]
mycollection=mydb["products"]

#birden fazla kayıt ekleme

productList=[
    {"name":"Samsung S6","price":3000,"decription":"iyi telefon"},
    {"name":"Samsung S7","price":4000,"categories":["telefon","elektronik"]}
]

result=mycollection.insert_many(productList)
print(result.inserted_ids)

# tek bir kayıt ekleme

#product={"name":"Samsung S5","price":2000}
#
#result=mycollection.insert_one(product) #tek bir tane kayıt eklemek için insert_one daha fazla kayıt eklemek için insert_many 
#
#print(result)
#print(type(result))
#print(result.inserted_id) #kimliği görmek istersek