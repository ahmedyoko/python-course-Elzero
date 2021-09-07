#..................................................
# numpy => data types and control array
#..................................................
# https://numpy.org/devdocs/users/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data
#..................................................
# '?' boolean
# 'b' signed byte
# 'B' unsigned byte
# 'i' signed integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex floating-point
# 'm' timedelta
# 'M' datetime
# 'o' (python) objects
# 'S','a' zero-terminated bytes (not recomended)
# 'U' unicode string
# 'V' raw data (void)
#........................................................
import numpy as np

# np.dtype => to know the type of array 
my_array1 = np.array([1,2,3,4])
my_array2 = np.array([1.5,2.3,3.2])
my_array3 = np.array(['osa','b','ahmed'])
# show array data type
print(my_array1.dtype) # int32
print(my_array2.dtype) # float64
print(my_array3.dtype) # <U5 => unicode string => number of characters of greatest string => ahmed

print('*'*50)
# Create array with specific data type 
my_array4 = np.array([1,2,3,4], dtype=float) # you can write dtype="f" or float or "float"
my_array5 = np.array([1.5,2.3,3.2], dtype=int) # int or "int" or "i"
# my_array6 = np.array(['osa','b','ahmed'],dtype=int) # valueError
print(my_array4.dtype)
print(my_array5.dtype)
# print(my_array6.dtype)

print('*'*50)

# change datatype of existing array by method => astype("wanted type")
my_array7 = np.array([0,1,2,3,0,4])
print(my_array7.dtype)
print(my_array7)

print('*'*50)

my_array7 = my_array7.astype("float")
print(my_array7.dtype)
print(my_array7)
print('*'*50)

my_array7 = my_array7.astype("bool")
print(my_array7.dtype)
print(my_array7)

print('*'*50)
# Test capacity : difference between 32 and 64
my_array8 = np.array([100,200,300,400],dtype="f")# float 32
print(my_array8.dtype)
print(my_array8.itemsize)
print('*'*50)
my_array8 = my_array8.astype("float") # float 64
print(my_array8.dtype)
print(my_array8.itemsize)

