from unittest import result
import numpy as np
numbers=np.array([0,5,10,15,20,25,50,75])

numbers[5]
numbers[-1]
numbers[0:3]
numbers[:3]
numbers[3:]
numbers[::] 
numbers[::-1]
numbers[::-2]

numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]]) #iki boyutlu

numbers2[0]
numbers2[2]
numbers2[0,2]
numbers2[0][2]
numbers2[2,1]
numbers2[2][1]
numbers2[:,2]
numbers2[:,0]
numbers2[:,0:2]
numbers2[-1,:]
numbers2[:3,:3]
numbers2[:2,:2]

arr1=np.arange(0,10)
#arr2=arr1 #referans

arr2=arr1.copy()#arr1 içerisindeki tüm bilgiler arr2 içerisine atılacak ancak
                #arr2 içinde yapılan değişkilk arr2'yi etkileycek

print(arr1)
print(arr2)

arr2[0]=20

print(arr1)
print(arr2)







