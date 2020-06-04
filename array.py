



'''fact=1
arr=array('i',[1,2,3,4,5,6,7,8,9])
print(arr)
item=int(input('enter the no you want the factorial :'))
for i in range(1,item+1):
    fact=fact*i
print(fact)



dict={'abhishek': ['ç,python'],'junaid':['python']}
print(dict)
print(list(dict.keys()))'''


from numpy import *
fact=1
arr=array([1,2,3,4,5,6,7,8,9])
print(arr)

## array addition

arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,6])
print(arr1)
print(arr2)
arr3 = arr1 + arr2
print(arr3)

print(max(arr3))
print(min(arr3))
print(sum(arr3))
arr4=arr1
print(arr4)
arr4[1]=7
print(arr4)
print(arr1)
arr5=arr2.copy()
arr5[2]=5
print(arr5)
print(arr2)
print('junaid')
print(concatenate([arr1,arr2]))


## adding two arrays by ' for loop '
from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([5,4,3,2,1])

for i in range(len(arr1)):
    arr3 = arr1 + arr2
print('junaid')
print(arr3)
