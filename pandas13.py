import pandas as pd
df=pd.read_csv("GBvideos.csv")
df.info()
df.shape
df.columns
#1
df.head(10)
#2
df[5:].head()
#3
df.columns
len(df.columns)
#4
df.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled','video_error_or_removed', 'description'],axis=1,inplace=True)
#5
df["likes"].mean()
df["dislikes"].mean()
#6
df.head(50)[["title","likes","dislikes"]]
#7
df[df["views"].max() == df["views"]]["title"].iloc[0]
#8
df[df["views"].min() == df["views"]]["title"].iloc[0]
#9
df.sort_values("views",ascending=False).head(10)[["title","views"]]
#10
df.groupby("category_id").mean().sort_values("likes")["likes"]
#11
df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]
#12
df["category_id"].value_counts()
#13
df["title_len"]=df["title"].apply(len)
print(df["title_len"])
#14
df["tag_count"]=df["tags"].apply(lambda x: len(x.split("|")))
#veya
def tagcount(tag):
    return len(tag.split("|"))

df["tag_count"]=df["tags"].apply(tagcount) 
#15
def likedisleoranhesapla(dataset):
    likelist=list(dataset["likes"])
    dislikeslist=list(dataset["dislikes"])

    liste=list(zip(likelist,dislikeslist))

    


