import numpy as np

result=np.array([1,3,5,7,9])
print(result)

result1=np.arange(1,10)
print(result1)

result2=np.arange(10,100,3)
print(result2)

result3=np.zeros(10)
print(result3)

result4=np.ones(10)
print(result4) 

result5=np.linspace(0,100,5)
print(result5) 

result6=np.linspace(0,5,5)
print(result6) 

result7=np.random.randint(0,10)
print(result7) 

result8=np.random.randint(20)
print(result8)

result9=np.random.randint(1,10,3)
print(result9)

result10=np.random.rand(5)
print(result10)

result11=np.random.randn(5)
print(result11)

np_array=np.arange(0,50)
np_multi=np_array.reshape(5,10)
print(np_multi.sum(axis=1))
print(np_multi.sum(axis=0))

rnd_numbers=np.random.randint(1,100,10)
print(rnd_numbers)
rnd_numbers.max() #en büyük sayı
rnd_numbers.min() #en küçük sayı
rnd_numbers.mean() #ortalaması
rnd_numbers.argmax() #en büyük sayının indeksi
rnd_numbers.argmin()#en küçük sayının indeksi

