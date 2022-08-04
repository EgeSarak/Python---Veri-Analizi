from unittest import result
import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=["column1","column2","column3","column4","column5"])

result=df
result=df.columns

result=df.head()
result=df.tail()

result=df["column1"].head()
result=df.column1.head()

result=df[["column1","column2"]].head()
result=df[5:15][["column1","column2"]].head()
result=df[5:15][["column1","column2"]].tail()

print(result)

#filtreleme
result=df>50
result=df[df>50]
result=df[df%2==0]
result=df["column1"]>50
result=df[df["column1"]>50]
result=df[(df["column1"] > 50) & (df["column1"] <= 70)]
result=df[(df["column1"] > 50) & (df["column1"] <= 70)]["column1"]
result=df[(df["column1"] > 50) & (df["column2"] <= 70)][["column1","column2"]]
result=df[(df["column1"] > 50) | (df["column2"] > 50)][["column1","column2"]]
result=df.query("column1 >= 50 & column1 % 2 == 0" )[["column1"]]

print(result)  