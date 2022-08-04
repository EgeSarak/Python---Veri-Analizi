import pandas as pd
df=pd.read_csv("TestDoc2_KaggleData_OMDB_Detailed.csv")
df.columns
df.info()

#2
df.head()
#3
df.head(10)
#4
df.tail()
#5
df.tail(10)
#6
df["Title"]
#7
df["Title"].head()
#8
df[["Title","imdbRating"]].head()
#9
df[["Title","imdbRating"]].tail(7)
#10
df[5:10][["Title","imdbRating"]].head()
#11
df[df["imdbRating"] >= 8.0][["Title","imdbRating"]].head(10)

#12


