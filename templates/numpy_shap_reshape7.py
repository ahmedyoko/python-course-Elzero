#...................................................
# Numpy => Array shape and reshape
#...................................................
# shape => return a tuple contain the number of elements in each dimension
#...................................................

import numpy as np 
my_array1 = np.array([1,2,3,4])
print(my_array1.ndim) # number of dimension
print(my_array1.size) # number of item
print(my_array1.shape) # distribution of item in rows and cols, in one dimension gives cols only

print('*'*50)

# two dimension array
my_array2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(my_array2.ndim) # number of dimension
print(my_array2.size) # number of item
print(my_array2.shape) # distribution of item in rows and cols

print('*'*50)

# three dimension array
my_array3 = np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
print(my_array3.ndim) # number of dimension
print(my_array3.size) # number of item
print(my_array3.shape) # distribution of item in rows and cols

print('*'*50)
my_array4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(my_array4.ndim) # number of dimension
print(my_array4.size) # number of item
print(my_array4.shape) # distribution of item in rows and cols
print('*'*50)
reshaped_array4 = my_array4.reshape(2,6)
print(my_array4.ndim) # number of dimension
print(my_array4.size) # number of item
print(my_array4.shape) # distribution of item in rows and cols
print(reshaped_array4)
print('*'*50)
reshaped_array4 = my_array4.reshape(3,4)
print(my_array4.ndim) # number of dimension
print(my_array4.size) # number of item
print(my_array4.shape) # distribution of item in rows and cols
print(reshaped_array4)
print('*'*50)
reshaped_array4 = my_array4.reshape(4,3)
print(my_array4.ndim) # number of dimension
print(my_array4.size) # number of item
print(my_array4.shape) # distribution of item in rows and cols
print(reshaped_array4)

print('*'*50)
# change 2 dimension array to one dimension array by reshaping
my_array5 = np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]])
print(my_array5.ndim) # number of dimension
print(my_array5.size) # number of item
print(my_array5.shape) # distribution of item in rows and cols

print('*'*50)
reshaped_array5 = my_array5.reshape(-1) # change
print(my_array5.ndim) # number of dimension
print(my_array5.size) # number of item
print(my_array5.shape) # distribution of item in rows and cols
print(reshaped_array5)

print('*'*50)
# change to 3 dimension array
reshaped_array5 = my_array5.reshape(2,5,2) # change
print(my_array5.ndim) # number of dimension
print(my_array5.size) # number of item
print(my_array5.shape) # distribution of item in rows and cols
print(reshaped_array5)