#............................................
# Numpy => performance and Memory use
#............................................
# Performance
# Memory use
#............................................

import numpy as np
import time  # to estimate execution time
import sys   # to know the size of elements in byte

elements = 15000000
list1 = range(elements) # range(start=0,end,step=1) the end is obligatory=>(0,149)
list2 = range(elements)
# for element in list1 :
#     print(element)
print('hello')
array1 = np.arange(elements)
array2 = np.arange(elements)
# for element in array1 :
#     print(element)



list_start = time.time()
list_result = [(n1+n2) for n1,n2 in zip(list1,list2)]
# print(list_result)
# print(f'list time : {time.time() -list_start} ')  # list time : 2.717548131942749

# for n1,n2 in zip(list1,list2) :
#     print(n1+n2)
print('array')
array_start = time.time()
array_result = array1+array2
# print(array_result)
# print(f'array time : {time.time() -array_start} ')  # array time : 0.07050323486328125

print('*'*50)
# Memory size
print('memory with array')
my_array = np.arange(100)
print(my_array)
print(my_array.itemsize) # size of each item
print(my_array.size) # number of items in array => 100
print(f'All Bytes : {my_array.itemsize * my_array.size } ')

print('*'*50)
# Memory size
print('memory with list')

my_list = range(100)
print(sys.getsizeof(my_list[0])) # first item size is 24
print(sys.getsizeof(my_list[1])) # second item till the last of list is 28 => print(sys.getsizeof(1))
print(len(my_list))
print(f'All Bytes : {sys.getsizeof(1) * len(my_list) } ')


# number of items in list by length , in array by size


