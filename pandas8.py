import pandas as pd
import numpy as np

personeller={
        "Çalışan":["Ahmet Yılmaz","Caner Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
        "Departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
        "Yaş":[30,25,45,50,23,34,42],
        "Semt":["Kadiköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
        "Maaş":[5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)

df["Maaş"].sum()

df.groupby("Departman").groups
df.groupby(["Departman","Semt"]).groups

#for döngüsü ile
semtler=df.groupby("Semt")

#for name,group in semtler:
#    print(name)
#    print(group)

#departmanlar=df.groupby("Departman")
#for name,group in departmanlar:
#    print(name)
#    print(group)


df.groupby("Semt").get_group("Kadiköy") #kadıköyde oturan kişileri aldık
df.groupby("Departman").get_group("Muhasebe") #muhasebede çalışan kişileri aldık

#çalışanların yaşları toplamı,maaş toplamı gibi bilgiler
df.groupby("Departman").sum()

#yaş,maaş vb ortalamları gelsin
df.groupby("Departman").mean()

#sadece maaş ortalamaları gelsin
df.groupby("Departman")["Maaş"].mean()

#semte göre yaş ortalaması
df.groupby("Semt")["Yaş"].mean()
df.groupby("Semt")["Maaş"].mean()

#semtlere göre çalışan sayısı
df.groupby("Semt")["Çalışan"].count()

#departmana göre maksimum yaş,minimum yas
df.groupby("Departman")["Yaş"].max()
df.groupby("Departman")["Yaş"].min()

#departmana göre maksimum maas,minimum maas
df.groupby("Departman")["Maaş"].max()
df.groupby("Departman")["Maaş"].min()

#Tüm departmanların içinden sectiğimiz departmanın maksimum maaşı
df.groupby("Departman")["Maaş"].max()["Muhasebe"]

#agg metodu kullanarak hesaplama
df.groupby("Departman").agg(np.mean)

#maaş ile iglili hesaplalamrı agg ile tek bir satırda halledebiliyoruz
df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min])

#yukarıdaki işlemi tek bir departman için yapmak istersek
df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]