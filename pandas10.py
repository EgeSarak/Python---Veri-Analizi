import pandas as pd

data=pd.read_csv("nba.csv")

data.dropna(inplace=True)
data.columns

#data["Name"]=data["Name"].str.upper() #her satırda ki isimler büyük harfle yazılır
#data["Name"]=data["Name"].str.lower() #her satırda ki isimler küçük harfle yazılır
#data["index"]=data["Name"].str.find("a")
#data=data.Name.str.contains("Jordan")
#data=data[data.Name.str.contains("Jordan")]
#data=data.Team.str.replace(" ","-")
data[["FirstName","LastName"]]=data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)



print(data.head(10)) 
print(data)