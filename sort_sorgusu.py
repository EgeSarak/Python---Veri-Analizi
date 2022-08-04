import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myclient["node-app"]
mycollection=mydb["products"]

#result=mycollection.find().sort("name",1) #isimleri azdan çoka sıraladık
#result=mycollection.find().sort("name",-1) #isimleri çoktan aza doğru sıraladık
#result=mycollection.find().sort("price",1) #ücretleri  azdan çoka sıraladık
#result=mycollection.find().sort("price",-1) #ücretleri  çoktan aza sıraladık
result=mycollection.find().sort([("name",1),("price",-1)]) #isimlere göre sıraladık,fiyatları da azalan şekilde sıraladık


for i in result:
    print(i)