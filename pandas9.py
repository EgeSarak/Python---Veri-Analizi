from hashlib import new
from multiprocessing.sharedctypes import Value
from operator import index
from unittest import result
import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])
df=df.reindex(["a","b","c","d","e","f","g","h"])

newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"]=newColumn

a=df.drop("column1",axis=1)
a=df.drop(["column1","column2"],axis=1)
a=df.drop("a",axis=0)
a=df.isnull()
a=df.notnull()
a=df.isnull().sum()
a=df["column1"].isnull().sum()
a=df[df["column1"].isnull()]
a=df[df["column1"].isnull()]["column1"]
a=df[df["column1"].notnull()]["column1"]

a=df.dropna() #axis=0 #satırları siler
a=df.dropna(axis=1) #kolonları siler
a=df.dropna(how="any") 
a=df.dropna(how="all") 

a=df.dropna(subset=["column1","column2"],how="all")
a=df.dropna(subset=["column1","column2"],how="any")
a=df.dropna(thresh=2)
a=df.dropna(thresh=3) #en az sayıda normal veri 

a=df.fillna(value="no input")
a=df.fillna(value=1)

df.sum()
df.sum().sum()
df.size
df.isnull().sum()
df.isnull().sum().sum()


def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size-df.isnull().sum().sum()
    return toplam/adet
result=df.fillna(value=ortalama(df))    


print(result)

print(a)






print(df)