#...................................................
# numpy => introduction
#...................................................
# [1] third party modules deals with array and matrices
# [2] stand for numerical python
# [3] open source
# [4] support dealing with multidimensional array and matrices
# [5] has many mathmetical function to deal with this elements
#......................................................
# why use numpy array?
# [1] consume less memory
# [2] very fast compared to python list
# [3] esay to use
# [4] support element wise operation
# [5] elements are stored contiguous متجاورة
#........................................................
# python list:
# [1] Homogenous => contain same type of object
# [2] Heterogenous => can contain different types of object
#...................................................
# in numpy :
# item of the same type
# can be sure the storage size needed for the array
# index from zero
#...................................................
# numpy on the github => https://github.com/numpy/numpy
#...................................................
# pip list => list of python package (one of them numpy)
#........................................................
# Create Arrays :
#........................................................

import numpy as np
# print(np.__version__) # to know the version 
# print(dir(np))

my_list = [1,2,3,4,5]
my_array = np.array(my_list) # array method accept any sequence
print(my_list)  # [1,2,3,4,5]
print(my_array)  # [1 2 3 4 5]
print('*'*50)
# Type 
print(type(my_list))  # <class 'list'>
print(type(my_array))  # <class 'numpy.ndarray'> nd stands for number dimension array ,
#  as one dimension array and two dimension array

print('*'*50)
# indexing : to access element
print(my_list[0])
print(my_array[0])

print('*'*50)
# rank = dimension array 
a = np.array(10) # zero dimension array
# array(row1)
b = np.array([10,20]) # one dimension array = one list in paranthesis
# array([row1,row2,row3,row4,...]) all rows have the same columns number
c = np.array( [ [1,2],[3,4] ] ) # two dimension array = 2 arrays inside great one
# array([[row1,row2,..],[the same number of rows]])
d = np.array([[ [1,2] , [3,4] ] , [ [5,6] , [7,8]]]) # three dimension array =>3square brackets in each side

print(d[0]) # [ [1,2] , [3,4] ]
print(d[1][1]) # [7,8]
print(d[1][1][1]) # 8
print(d[1,1,1]) # three dimension => 8
print(d[1,1,-1])
print('*'*50)
# number of dimensions : ndim => number of dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('*'*50)
# Custom array dimension => number of surrounding square brackets
my_custom_array = np.array([1,2,3],ndmin=3) # number of dimensions are 3 => ndmin
print(my_custom_array)  # [[[1 2 3]]]
print(my_custom_array.ndim)
print(my_custom_array[0]) # remove one square brackets
print(my_custom_array[0][0])
print(my_custom_array[0][0][0])
print('*'*50)

