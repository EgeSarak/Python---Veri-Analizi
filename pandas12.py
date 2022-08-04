#Uygulama
import pandas as pd
df=pd.read_csv("nba.csv")
df.info()
df.columns
#1
df.head(10)
#2
df.shape # veya
len(df.index)
#3
df["Salary"].mean()
#4
df["Salary"].max()
#5
df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]
#6
df[(df["Age"] >=20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
#7
df[df["Name"]=="John Holland"]["Team"].iloc[0]
#8
df.groupby("Team").mean()["Salary"]
#9
len(df.groupby("Team"))
df["Team"].nunique()
df["Team"].unique()
#10
df["Team"].value_counts()
#11
df=df.dropna() #veya df.dropna(inplace=true)
df[df["Name"].str.contains("and")]

