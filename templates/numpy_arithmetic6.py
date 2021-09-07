#................................................
# numpy => Arithmetic operation :
#................................................
# Addition
# Substraction
# Multiplication
# Dividation
#.......................
# min
# max
# sum
# ravel => return flattened array 1 dimension with the same type
#................................................

import numpy as np

# Arithmetic operation :
my_array1 = np.array([10,20,30]) 
my_array2 = np.array([5,2,4])
print(my_array1 + my_array2) # [15 22 34]
print(my_array1 - my_array2) # [ 5 18 26]
print(my_array1 * my_array2)  # [ 50  40 120]
print(my_array1 / my_array2)  # [ 2.  10.   7.5]

print('*'*50)
# for multidimensional array
my_array3 = np.array([[1,4],[5,9]])
my_array4 = np.array([[2,7],[10,5]])

print(my_array3 + my_array4) # [[3,11],[15,14]]
print(my_array3 - my_array4)
print(my_array3 * my_array4)
print(my_array3 / my_array4)

print('*'*50)
# Min , Max , Sum
my_array5 = np.array([10,20,30])

print(my_array5.min())
print(my_array5.max())
print(my_array5.sum())
print('*'*50)
# 2 dimensional np.array
my_array6 = np.array([[6,4],[3,9]])
print(my_array6.min())
print(my_array6.max())
print(my_array6.sum())

print('*'*50)
# Ravel 
my_array7 = np.array([[6,4],[3,9]])
print(my_array7.ravel())
print('*'*50)
my_array8 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(my_array8.ndim)
print(my_array8.ravel())
x = my_array8.ravel()
print(x.ndim)

