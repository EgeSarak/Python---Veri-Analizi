import matplotlib.pyplot as plt

#stack plot(yığın grafiği)
"""
yil=[2021,2012,2013,2014,2015]
oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,15,15,21]
oyuncu3=[18,20,22,25,19]
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("gol sayısı")
plt.legend()
plt.show()  """


#pie plot(pasta grafiği)
"""
goal_types="penaltı","kaleye atılan şut","serbest vuruş"

goals=[12,35,7]
colors=["y","r","b"]

#plt.pie(goals,labels=goal_types,colors=colors)
plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")

plt.show() """

#bar plot(çubuk grafiği)
"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("gün")
plt.ylabel("Mesafe(km)")
plt.title=("Araç bilgileri")

plt.show()        """

#Histogram grafiği

yaslar=[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,120,126]
yas_gruplari=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("Histogram Grafiği")

plt.show()