from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

#çizgi grafiği
"""
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y)
plt.show() """

"""
x=np.linspace(0,2,100)
plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3,label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("ylabel")
plt.title("simple plot")

plt.legend()

plt.show()  """

"""
#alt alta 2 tane grafik çizdirdik
x=np.linspace(0,2,100)
fig,axes=plt.subplot(2)

axes[0].plot(x,x,color="red")
axes[0].set_title("linear")

axes[1].plot(x,x**2,color="green")
axes[1].set_title("cubic")
plt.show()  """

"""
#alt alta 3 tane grafik çizdirdik
x=np.linspace(0,2,100)
fig,axes=plt.subplot(3)

axes[0].plot(x,x,color="red")
axes[0].set_title("linear")

axes[1].plot(x,x**2,color="green")
axes[1].set_title("quadratic")

axes[2].plot(x,x**3,color="yellow")
axes[2].set_title("cubic")

plt.tight_layout() #layout yazılarını düzenli yazlıp okunmasını sağlar

plt.show() """

"""
x=np.linspace(0,2,100)
fig,axes=plt.subplot(2,2)
fig.suptitle("grafik baslıgı")

axes[0,0].plot(x,x,color="red")
axes[0,1].plot(x,x**2,color="blue")
axes[1,0].plot(x,x**3,color="green")
axes[1,1].plot(x,x**4,color="yellow")

plt.show() """


import pandas as pd
df=pd.read_csv("nba.csv")
df=df.drop(["Number"],axis=1).groupby("Team").mean()
df.head().plot(subplots=True)
plt.legend()
plt.show()