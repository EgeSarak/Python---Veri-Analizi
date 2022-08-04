import numpy as np
#1
np.array([10,15,30,45,60])

#2
np.arange(5,15)

#3
np.arange(50,100,5)

#4
np.zeros(10)

#5

np.ones(10)

#6
np.linspace(0,100,5)

#7
np.random.randint(10,30,5)

#8
np.random.randn(10)

#9
matrix=np.random.randint(10,50,15).reshape(3,5)
print(matrix)

#10
matrix.sum(axis=0) #sütunları topladık
matrix.sum(axis=1) #satırları topladık

#11
matrix.max()
matrix.min()
matrix.mean()
matrix.ndim
matrix.size
matrix.shape

#12
matrix.argmax()
matrix.argmin()

#13
a=np.arange(10,20)
print(a)

a[0:3]

#14
a[::-1]
#15
print(matrix)
matrix[0]
#16
matrix[1][2]

#17
matrix[:,0]

#18
matrix**2

#19
matrix=np.random.randint(-50,50,15).reshape(3,5)
ciftler=matrix[matrix % 2==0]
sonuc=ciftler[ciftler>0]
print(sonuc)

