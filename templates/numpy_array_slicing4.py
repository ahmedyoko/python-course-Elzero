#....................................................
# numpy => array slicing 
#....................................................
import numpy as np

# slicing => [start : end : step] not including end
a = np.array(['A','B','C','D','E','F'])
print(a.ndim)
print(a.size)
print(a[1])
print(a[1:4])

print("*"*50)
print("2 dimensional array")
b = np.array([['A','B','X'],['C','D','Y'],['E','F','Z'],['M','N','O']])
print(b.ndim)
print(b.size)
print(b[3])
print(b[0:3])
# to reach more than one filteration as first 2 elements in b[:3] , write by 2 ways :
# b[:3][:2] or replace comma instead of square brackets => b[:3,:2]
print(b[:3,:2])
print("*"*50)
print(b[-2:,0])
print(b[-2:, : :2]) # steps 2 